import unittest
import os
from itertools import islice
from zip_dma.data_store import DataStore
from zip_dma.model.map.cbsa_msa_id_map import CbsaMsaIdMap

class CbsaMsaIdMapTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.file_location ="/tmp/CbsaMsaIdMapTest.json"
        temp = DataStore.get_data_store(cls.file_location)
        cls.cbsa_map = CbsaMsaIdMap.get_map()
        cls.cbsa = "35004"
        cls.msa_id  = "35620"
        cls.cbsa_not_loaded = "35005"

    @classmethod
    def tearDownClass(cls):
        CbsaMsaIdMap.test_clear_instance()
        DataStore.test_clear_instance()
        if os.path.isfile(cls.file_location):
            os.remove(cls.file_location)
    
    def test_set_and_get(self):
        """Test setting a cbsa and getting the msa_id"""
        CbsaMsaIdMapTest.cbsa_map.set(CbsaMsaIdMapTest.cbsa, CbsaMsaIdMapTest.msa_id)
        self.assertEqual(CbsaMsaIdMapTest.msa_id, CbsaMsaIdMapTest.cbsa_map.get(CbsaMsaIdMapTest.cbsa))
        
        
    def test_get_if_non_existant_cbsa(self):
        """Test asking for a nonexisting cbsa"""
        self.assertIsNone(CbsaMsaIdMapTest.cbsa_map.get(CbsaMsaIdMapTest.cbsa_not_loaded))