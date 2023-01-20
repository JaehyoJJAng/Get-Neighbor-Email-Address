from __init__ import Naver
from typing import Dict,List,Union
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
    
if __name__ == '__main__':
    unittest.main()