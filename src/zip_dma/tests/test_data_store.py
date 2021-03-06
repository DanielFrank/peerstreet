import unittest
import os
from zip_dma.data_store import DataStore

class DataStoreTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.file_location = '/tmp/DataStoreTest.json'
        cls.existingDoc = "test"
        cls.nonExistingDoc = "test2"
        cls.ds = DataStore.get_data_store(cls.file_location)
        cls.ds.create("test")

    @classmethod
    def tearDownClass(cls):
        DataStore.test_clear_instance()
        if os.path.isfile(cls.file_location):
            os.remove(cls.file_location)
    
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

    def test_list_docs(self):
        """Confirm list_docs"""
        doc_list = DataStoreTest.ds.list_docs()
        self.assertEqual(1, len(doc_list))
        self.assertTrue(DataStoreTest.existingDoc in doc_list)
        self.assertFalse(DataStoreTest.nonExistingDoc in doc_list)

    def test_doc_exists(self):
        """Confirm doc_exists"""
        self.assertTrue(DataStoreTest.ds.doc_exists(DataStoreTest.existingDoc))
        self.assertFalse(DataStoreTest.ds.doc_exists(DataStoreTest.nonExistingDoc))
