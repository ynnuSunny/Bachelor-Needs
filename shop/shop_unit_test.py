import unittest
import views

class TestDBConnect(unittest.TestCase):
    def test_DBConnect(self):
        self.assertIsInstance(DBConnect.getInstance(), MongoClient)
        self.assertNotIsInstance(DBConnect.getInstance(), DBConnect)
    
    def test_showPostCategory(self):
        self.assertIsInstance(showPostCategory, django.http.response.HttpResponse)
        self.assertNotIsInstance(showPostCategory, DBConnect)
    
    def test_deletePost(self):
        self.assertIsInstance(deletePost, django.http.response.HttpResponse)
        self.assertNotIsInstance(deletePost, MongoClient)
        
    
    


if(__name__=='main'):
    unittest.main()