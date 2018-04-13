from zip_dma.data_store import DataStore
from zip_dma.msa import MSA

class MsaMap:
    
    __instance = None
    DOC_NAME = "MsaMap"
    
    @classmethod
    def get_map(cls):
        if cls.__instance is None:
            cls.__instance = MsaMap()
        return cls.__instance
    
    def __init__(self):
        self.data_store = DataStore.get_data_store()
        if (not self.data_store.doc_exists(MsaMap.DOC_NAME)):
            self.data_store.create(MsaMap.DOC_NAME)
    
    def get(self, cbsa):
        temp_dict = self.data_store.get(MsaMap.DOC_NAME, cbsa)
        if temp_dict is None:
            return None
        return MSA.decode(temp_dict)
    
    def store(self, cbsa, msa):
        self.data_store.set(MsaMap.DOC_NAME, cbsa, msa.encode())
    
    #TODO Throw error if MSA doesn't exist
    def update_pop(self, cbsa, year, pop):
        msa = self.get(cbsa)
        if msa is None:
            return
        msa.set_population(year, pop)
        self.store(cbsa, msa)