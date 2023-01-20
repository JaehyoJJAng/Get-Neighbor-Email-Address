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
import time
import pyperclip as pc
import pyautogui
import sys

class ChromeDriver:
    @staticmethod
    def set_driver():
        # options 객체
        chrome_options : Options = Options()

        # 브라우저 꺼짐 방지
        chrome_options.add_experimental_option('detach', True)

        service : Service = Service(executable_path=ChromeDriverManager().install())
        browser : webdriver.Chrome = webdriver.Chrome(service=service, options=chrome_options)
        browser.maximize_window()
        return browser

class Naver:
    def __init__(self) -> None:
        self.id : str = get_login_secrets(key='id') # Login ID
        self.pw : str = get_login_secrets(key='pw') # Login PW
        self.browser  = ChromeDriver().set_driver() # Web Driver
    
    def run(self):
        # 네이버 로그인
        self.naver_login()
        
                
    def naver_login(self)-> None:
        """ 네이버 로그인 처리 """
        # 네이버 로그인 페이지 이동
        URL : str = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
        self.browser.get(URL)
        self.browser.implicitly_wait(5)  # 웹페이지가 로딩 될 때 까지 5초는 기다림

        # ID 입력
        try:
            elem_id = self.browser.find_element(By.CSS_SELECTOR,'input#id')
            elem_id.click()
            pc.copy(self.id)
            time.sleep(0.2)
            pyautogui.hotkey('ctrl','v')
        except:
            print('아이디 입력 실패!')
            sys.exit()
                            
        # PW 입력
        try:
            elem_pw = self.browser.find_element(By.CSS_SELECTOR,'input#pw')
            elem_pw.click()
            pc.copy(self.pw)
            time.sleep(0.2)
            pyautogui.hotkey('ctrl','v')
        except:
            print('패스워드 입력 실패!')
            sys.exit()
        
        # 로그인
        try:
            time.sleep(0.8)
            login_btn = self.browser.find_element(By.CSS_SELECTOR, "button.btn_login")
            login_btn.click()
        except:
            print('로그인 클릭 실패!')
            sys.exit()
        
        # 인증 대기시간 할당
        time.sleep(10)
        
def main():
    # Create Naver Instance
    naver : Naver = Naver()
    
    # Run
    naver.run()
if __name__ == '__main__':
    main()