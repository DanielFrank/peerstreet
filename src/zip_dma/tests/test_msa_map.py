import unittest
import csv
import io
from ..msa import MSA
from ..msa_map import MsaMap

class MsaMapTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.msa_map = MsaMap.get_map()
    
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