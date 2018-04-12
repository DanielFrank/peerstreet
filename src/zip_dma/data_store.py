import pickledb

class DataStore:
    
    __instance = None
    __fileLocation = '/tmp/pickle.json'
    
    @classmethod
    def get_data_store(cls):
        if cls.__instance is None:
            cls.__instance = DataStore(cls.__fileLocation)
        return cls.__instance
    
    def __init__(self, file_location):
        self.db = pickledb.load(file_location, False)
    
    def get(self, doc, key):
        try:
            return self.db.dget(doc, key)
        except KeyError:
            return None
            
    def create(self,doc):
        self.db.dcreate(doc)
    
    def set(self, doc, key, value):
        return self.db.dadd(doc, (key, value))
    
    def list_docs(self):
        return self.db.getall();
    
    def doc_exists(self, doc):
        return doc in self.list_docs()
    
    def save(self):
        self.db.dump()
