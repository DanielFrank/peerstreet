import csv
from zip_dma.data_store import DataStore
from zip_dma.zip_cbsa_map import ZipCbsaMap
from zip_dma.cbsa_loader import CbsaLoader

zip_cbsa_map = ZipCbsaMap.get_map()

with open('../zip_to_cbsa.csv', encoding='utf-8-sig') as zip_csv_file:
    zipreader = csv.DictReader(zip_csv_file)
    zip_cbsa_map.load_file(zipreader)
    
with open('../cbsa_to_msa.csv', encoding='iso-8859-1') as cbsa_msa_file:
    cbsareader = csv.DictReader(cbsa_msa_file)
    CbsaLoader.load_file(cbsareader, overwrite=True)
        
