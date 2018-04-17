import unittest
import os
from ..data_store import DataStore
from ..msa import MSA
from ..msa_map import MsaMap

class MsaMapTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.file_location = '/tmp/MsaMapTest.json'
        temp = DataStore.get_data_store(cls.file_location)
        cls.msa_map = MsaMap.get_map()
        
    @classmethod
    def tearDownClass(cls):
        MsaMap.test_clear_instance()
        DataStore.test_clear_instance()
        if os.path.isfile(cls.file_location):
            os.remove(cls.file_location)        
    
    def test_set_and_get(self):
        """Test storing an msa"""
        msa = MSA("TEST")
        msa.set_population(2014, 1000)
        msa.set_population(2013, 23456)
        MsaMapTest.msa_map.store("12432", msa)
        msa2 = MsaMapTest.msa_map.get("12432")
        self.assertEqual(msa2.msa_name, "TEST")
        self.assertEqual(msa2.get_population(2013), 23456)
        self.assertEqual(msa2.get_population(2014), 1000)
        
        
    def test_get_msa(self):
        """Test asking for a nonexisting msa"""
        self.assertIsNone(MsaMapTest.msa_map.get("NonExistent"))