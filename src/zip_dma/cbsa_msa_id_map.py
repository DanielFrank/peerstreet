from zip_dma.data_store import DataStore

#TODO: Confirm cbsas are in correct format (for set and get)

class CbsaMsaIdMap:
    
    __instance = None
    DOC_NAME = "CbsaMsaIdMap"
    
    @classmethod
    def get_map(cls):
        if cls.__instance is None:
            cls.__instance = CbsaMsaIdMap()
        return cls.__instance
    
    def __init__(self):
        self.data_store = DataStore.get_data_store()
        if (not self.data_store.doc_exists(CbsaMsaIdMap.DOC_NAME)):
            self.data_store.create(CbsaMsaIdMap.DOC_NAME)
    
    #Returns None if not found
    def get(self, cbsa):
        return self.data_store.get(CbsaMsaIdMap.DOC_NAME, cbsa)
    
    def set(self, cbsa, msa_id):
        self.data_store.set(CbsaMsaIdMap.DOC_NAME, cbsa, msa_id)
