import unittest
from ..data_store import DataStore

class DataStoreTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.existingDoc = "test"
        cls.nonExistingDoc = "test2"
        cls.ds = DataStore.getDataStore()
        cls.ds.create("test")
    
    def test_set_and_get(self):
        """Test setting a key and getting the value"""
        DataStoreTest.ds.set(DataStoreTest.existingDoc, "a", 12)
        DataStoreTest.ds.set(DataStoreTest.existingDoc, "b", 55)
        self.assertEqual(12, DataStoreTest.ds.get(DataStoreTest.existingDoc, "a"))
        self.assertEqual(55, DataStoreTest.ds.get(DataStoreTest.existingDoc, "b"))
        
        
    def test_get_if_non_existant_key_on_existing_doc(self):
        """Test asking for a nonexisting key on an existing document"""
        self.assertIsNone(DataStoreTest.ds.get(DataStoreTest.existingDoc, "does-not-exist"))

    def test_get_on_non_existing_doc(self):
        """Test asking for a nonexisting key on an existing document"""
        self.assertIsNone(DataStoreTest.ds.get(DataStoreTest.nonExistingDoc, "key-does-not-matter"))
