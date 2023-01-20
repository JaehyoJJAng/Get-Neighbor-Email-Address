from config.config import get_login_secrets
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict , List , Union

class ChromeDriver:
    @staticmethod
    def set_driver()-> webdriver:
        # options 객체
        chrome_options : Options = Options()

        # headless Chrome 선언
        # chrome_options.add_argument('--headless')

        # 브라우저 꺼짐 방지
        chrome_options.add_experimental_option('detach', True)

        chrome_options.add_argument(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36")

        # 불필요한 에러메시지 없애기
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service : Service = Service(executable_path=ChromeDriverManager().install())
        browser : webdriver = webdriver.Chrome(service=service, chrome_options=chrome_options)
        browser.maximize_window()
        return browser

class Naver:
    def __init__(self) -> None:
        self.id : str = get_login_secrets(key='id')
        self.pw : str = get_login_secrets(key='pw') 
    
    def naver_login(self):
        pass
    
    
def main():
    naver : Naver = Naver()


if __name__ == '__main__':
    main()