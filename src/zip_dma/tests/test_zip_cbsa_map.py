import unittest
import csv
import io
from itertools import islice
from ..zip_cbsa_map import ZipCbsaMap

class ZipCbsaMapTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.zip_map = ZipCbsaMap.get_map()
        cls.fileContents = """ZIP,CBSA,RES_RATIO,BUS_RATIO,OTH_RATIO,TOT_RATIO
00501,35004,0.000000000,1.000000000,0.000000000,1.000000000
00601,00260,1.000000000,1.000000000,1.000000000,1.000000000
"""
    def parse_string_as_csv(self, s):
        return csv.DictReader(io.StringIO(s))
    
    def get_one_dict(self, s):
        contents = self.parse_string_as_csv(s)
        for row in islice(contents, 1):
            return row
    
    def test_load_line(self):
        """Test loading a line and getting the value"""
        ZipCbsaMapTest.zip_map.load_line(self.get_one_dict(ZipCbsaMapTest.fileContents))
        self.assertEqual(ZipCbsaMapTest.zip_map.get("00501"), "35004")

    def test_load_file(self):
        """Test loading a file and getting the value"""
        ZipCbsaMapTest.zip_map.load_file(self.parse_string_as_csv(ZipCbsaMapTest.fileContents))
        self.assertEqual(ZipCbsaMapTest.zip_map.get("00501"), "35004")
        self.assertEqual(ZipCbsaMapTest.zip_map.get("00601"), "00260")
        
    def test_unfound_zip(self):
        """Test getting the value of an unavailable zip"""
        self.assertEqual(ZipCbsaMapTest.zip_map.get("00000"), ZipCbsaMap.NO_RESULT)