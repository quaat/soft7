from soft.storagestrategy import Strategy
from soft.dataspace.database import Database
from typing import List
from urllib.parse import urlparse

class SQLiteReader(Strategy):
    def __init__(self, uri):
        super().__init__()
        self.uri = uri
    
    def generate_entity(self, table):
        conn = sqlite3.connect(file)
        cursor = conn.execute(f"PRAGMA table_info({table});")

        entity = {    
            "uri": f"com.sintef.soft/ontology/v1/generated_from_sqlite_{str(uuid4()).replace('-','_')}",
            "dimensions": {},
            "properties": {}
        }

        for row in cursor:
            entity['properties'][row[1]] = {'type': row[2],
                                            'label': row[1],
                                            'description': ''
                                           }
        return entity        
        
    def read(self, database: Database):
        p = urlparse(self.uri)
        assert p.scheme == 'sqlite3'
        query = """SELECT * FROM COMPANY"""
        conn = sqlite3.connect(p.path)
        print ("Opened database successfully");
        conn.execute(query)

    def write(self, databases: List[Database]):
        pass