import re
from zip_dma.data_store import DataStore
from zip_dma.model.msa import MSA
from zip_dma.model.map.msa_map import MsaMap
from zip_dma.model.map.cbsa_msa_id_map import CbsaMsaIdMap

class CbsaLoader:
    
    CBSA_COLUMN = "CBSA"
    MDIV_COLUMN = "MDIV"
    NAME_COLUMN = "NAME"
    LSAD_COLUMN = "LSAD"
    METRO_VALUE = "Metropolitan Statistical Area"
    POPULATION_REGEX = "^POPESTIMATE(\d{4})$"
    POPULATION_YEAR_MIN = 2014
    
    #Assumes getting csv.DictReader iter
    @classmethod
    def load_file(cls, csv, overwrite=False):
        ds = DataStore.get_data_store()
        cls.msa_map = MsaMap.get_map()
        cls.cbsa_msa_map = CbsaMsaIdMap.get_map()
        for row in csv:
            cls.load_row(row, overwrite)
        ds.save()
    
    @classmethod
    def load_row(cls, row, overwrite):
        if row[cls.LSAD_COLUMN] == cls.METRO_VALUE:
            cls.load_msa(row, overwrite)
            return
        if row[cls.MDIV_COLUMN] != "":
            cls.load_cbsa_msa_map(row)
    
    @classmethod
    def load_msa(cls, row, overwrite):
        msa = None
        if (not overwrite):
            msa = cls.msa_map.get(row[cls.CBSA_COLUMN])
        if msa is None:
            msa = MSA(row[cls.NAME_COLUMN])
        cls.load_msa_pop(msa, row)
        cls.msa_map.store(row[cls.CBSA_COLUMN], msa)
        cls.cbsa_msa_map.set(row[cls.CBSA_COLUMN], row[cls.CBSA_COLUMN])
    
    @classmethod
    def load_msa_pop(cls, msa, row):
        for col in row:
            match = re.search(cls.POPULATION_REGEX, col)
            if match is None:
                continue
            yr = int(match.group(1))
            if yr < cls.POPULATION_YEAR_MIN:
                continue
            msa.set_population(yr, int(row[col]))
 
    @classmethod
    def load_cbsa_msa_map(cls, row):
        cls.cbsa_msa_map.set(row[cls.MDIV_COLUMN], row[cls.CBSA_COLUMN])
