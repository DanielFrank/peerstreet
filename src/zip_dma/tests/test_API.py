import unittest
import json

from zip_dma.index import app

class ApiTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    def zip_test(self, zip_code, expected_cbsa="99999", expected_msa="N/A", expected_pop_2014="N/A", expected_pop_2015="N/A"):
        data = self.make_call(zip_code)
        self.assertEqual(data["Zip"], zip_code)
        self.assertEqual(data["CBSA"], expected_cbsa)
        self.assertEqual(data["MSA"], expected_msa)
        self.assertEqual(data["Pop2014"], expected_pop_2014)
        self.assertEqual(data["Pop2015"], expected_pop_2015)
        
        
    def make_call(self, zip_code):
        response = self.app.get("/zipToDMA/" + zip_code)
        self.assertEqual(response.status_code, 200)
        return json.loads(response.data.decode())
    
    def test_invalid_zip(self):
        """Confirm error if invalid zip"""
        data = self.make_call("12121212")
        self.assertTrue("error" in data)
    
    
    def test_cbsa_not_msa_cbsa(self):
        """Test zip where cbsa is not the MSA's CBSA"""
        self.zip_test("90266","31084","Los Angeles-Long Beach-Anaheim, CA", 13254397, 13340068)

    def test_cbsa_msa_cbsa(self):
        """Test zip where cbsa is the MSA's CBSA"""
        self.zip_test("32003","27260","Jacksonville, FL", 1421004, 1449481)

    def test_cbsa_with_no_msa(self):
        """Test zip where cbsa has no MSA"""
        self.zip_test("88340","10460")

    def test_zip_ith_no_cbsa(self):
        """Test zip with no CBSA"""
        self.zip_test("88338")
