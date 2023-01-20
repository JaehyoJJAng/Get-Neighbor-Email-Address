from __init__ import Naver
from typing import Dict,List
from selenium.webdriver.common.by import By
import unittest


class NaverTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.naver : Naver = Naver()
    
    def test_naver_login(self):
        self.naver.naver_login()
        
        query_box : str = self.naver.browser.find_element(By.CSS_SELECTOR,'div.group_nav a.nav').text
        self.assertTrue(query_box)
    
    def test_get_address_book(self):
        self.naver.naver_login()        
        neighbor_datas : List[Dict[str,str]] = self.naver.get_address_book()        
        for neighbor_data in neighbor_datas:
            for key,value in neighbor_data.items():
                self.assertTrue(value)            
    
if __name__ == '__main__':
    unittest.main()