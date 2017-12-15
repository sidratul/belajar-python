import unittest
from db.unfinished_url_dao import UnfinishedUrlDao

class TestMainBs(unittest.TestCase):

    un_dao = UnfinishedUrlDao()

    def test_insert_unfinished(self):
        count = self.un_dao.insert("abc",10)        
        self.assertEqual(1,count)

    def test_delete(self):
        count = self.un_dao.delete_by_url("abcdasdsd")
        self.assertEqual(0,count)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()