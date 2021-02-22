from soft.storagestrategy import Strategy
from soft.dataspace.database import Database
from typing import List
from uuid import uuid4
from datetime import datetime
import json

import os
from urllib.parse import urlparse

class JSONWriter(Strategy):
    
    def __init__(self, uri):
        super().__init__()
        self.uri = uri

    def read(self, database: Database):
        pass
    
    def write(self, databases: List[Database]):
        transaction_info = {
            'transaction_id': str(uuid4()),
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
