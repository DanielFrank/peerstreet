from zip_dma.data_store import DataStore

#TODO: Confirm zips are in correct format (for set and get)
#TODO: Check that file has expected headers

class ZipCbsaMap:
    
    __instance = None
    DOC_NAME = "ZipCbsaMap"
    NO_RESULT = "99999"
    ZIP_COLUMN = "ZIP"
    CBSA_COLUMN = "CBSA"
    
    @classmethod
    def get_map(cls):
        if cls.__instance is None:
            cls.__instance = ZipCbsaMap()
        cls.__instance.__check_doc()
        return cls.__instance
    
    def __init__(self):
        self.data_store = DataStore.get_data_store()
        
    def __check_doc(self):
        if (not self.data_store.doc_exists(ZipCbsaMap.DOC_NAME)):
            self.data_store.create(ZipCbsaMap.DOC_NAME)
    
    def get(self, zipcode):
        answer = self.data_store.get(ZipCbsaMap.DOC_NAME, zipcode)
        if answer is None:
            return ZipCbsaMap.NO_RESULT
        return answer
    
    def set(self, zipcode, cbsa):
        self.data_store.set(ZipCbsaMap.DOC_NAME, zipcode, cbsa)
    
    #Loads zip_dict
    def load_line(self, zip_dict):
        zipcode = zip_dict[ZipCbsaMap.ZIP_COLUMN]
        cbsa = zip_dict[ZipCbsaMap.CBSA_COLUMN]
        self.set(zipcode, cbsa)
     
    #Loads file that's been parsed by csv.DictReader
    #Assumes overwriting existing data
    def load_file(self, zip_cbsa_dict_reader):
        self.data_store.create(ZipCbsaMap.DOC_NAME)
        for row in zip_cbsa_dict_reader:
            self.load_line(row)
        self.data_store.save()