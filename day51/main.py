import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import os
load_dotenv()

class InstaBot:
    def __init__(self):
        self.instagram=os.getenv('INSTAGRAM')
        self.mail=os.getenv('USER_EMAIL')
        self.password=os.getenv('PASSWORD')
        self.followers_link=os.getenv('FOLLOWERS_URL')

        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.user_data_dir = os.path.join(os.getcwd(), 'chrome_profile')
        self.chrome_options.add_argument(f'--user-data-dir={self.user_data_dir}')
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        self.driver=webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.instagram)

        self.wait = WebDriverWait(self.driver, 2)
        self.long_wait=WebDriverWait(self.driver, 5)
    def login(self):
        email_input=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        email_input.send_keys(self.mail)

        password_input=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        password_input.send_keys(self.password)

        enter_button=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Увійти']")))
        enter_button.click() 

        main_screen=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='html-div']")))
        button=main_screen.find_element(By.CSS_SELECTOR, "div[role='button']")
        button.click()

    def loged(self):
        not_now = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Не зараз']")))
        not_now.click()

    def followers(self):
            self.driver.get(self.followers_link)
            subscribers = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Читачі')]")))
            subscribers.click()
            try:
                modal = self.long_wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))
                last_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
                while True:
                    modal = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                    time.sleep(2)
                    modal = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
                    new_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
                    if new_height == last_height:
                        break
                    last_height = new_height
            except TimeoutException:
                pass
    
    def follow(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Стежити']")))
            buttons = self.driver.find_elements(By.XPATH, "//div[text()='Стежити']")
            for button in buttons:
                try:
                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(1)
                except:
                    cancel = self.driver.find_element(By.XPATH, "//button[text()='Скасувати']")
                    cancel.click()
        except TimeoutException:
            self.driver.quit()

    def main(self):
        try:
            self.login()
        except TimeoutException:
            pass
        try:
            self.loged()
        except TimeoutException:
            pass
        self.followers()
        self.follow()
        
bot=InstaBot()
bot.main()