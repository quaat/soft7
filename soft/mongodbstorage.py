from soft.storagestrategy import Strategy
from soft.dataspace.database import Database
from pymongo import MongoClient
from typing import List
import os

MONGODB_HOST = os.environ.get('MONGODB_HOST', 'mymongodb')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT', 27017))
MONGODB_USER = os.environ.get('MONGODB_USER')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')

client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT, username=MONGODB_USER, password=MONGODB_PASSWORD)

db = client.soft
entity = {
    "something": "foo",
    "bar": "test"
}
id = db.soft_entities.insert_one(entity).inserted_id

class MongoWriter(Strategy):
    
    def __init__(self, uri):
        super().__init__()
        self.client = MongoClient(uri)
        self.db = self.client.soft

        
    def read(self, database: Database):
        pass


    def write(self, databases: List[Database]):
        transaction_id = str(uuid4())
        transaction_info = {
            'transaction_id': transaction_id,
            'parent_transaction_id': None,
            'timestamp': str(datetime.utcnow())
        }
        data = {'__meta__': transaction_info}
        for db in [databases[name] for name in databases]:
            data[db.name] = {}
            for doc in [db.document(docid) for docid in db.documents]:
                data[db.name][doc.id] = doc.data                         
        
        p = urlparse(self.uri)
        file_path = os.path.abspath(os.path.join(p.netloc, p.path))
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)
        return transaction_info        