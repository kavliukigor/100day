from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import os
from dotenv import load_dotenv
import time
load_dotenv()

tinder=os.getenv('TINDER')
email=os.getenv('EMAIL_REGISTER')
password=os.getenv('PASSWORD')
phone=os.getenv('PHONE')
user_data_dir=os.path.join(os.getcwd(),'chrome_profile')

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

driver=webdriver.Chrome(options=chrome_options)
driver.get(tinder)

wait = WebDriverWait(driver, 10)

def login():
    time.sleep(1)
    pyautogui.click(x=1044,y=768)
    pyautogui.click(x=721, y=767)
    time.sleep(1)
    pyautogui.click(x=822,y=708)
    driver.switch_to.window(driver.window_handles[1])
    try:
        email_input=driver.find_element(By.TAG_NAME, 'input')
        email_input.send_keys(email)

        ok_button=driver.find_element(By.XPATH, "//span[text()='Далі']")
        ok_button.click()

        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
        password_input=driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_input.send_keys(password)

        ok_button=driver.find_element(By.XPATH, "//span[text()='Далі']")
        ok_button.click()

        driver.switch_to.window(driver.window_handles[0])
    except:
        time.sleep(1)
        pyautogui.click(x=822,y=708)
        driver.switch_to.window(driver.window_handles[0])
    finally:    
        phone_enter=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='phone_number']")))
        phone_enter.send_keys(phone)
        cont_button=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q532679399"]/div/div[1]/div[2]/div/div[3]/button/div[2]/div[2]')))
        cont_button.click()

def like():
    try:
        time.sleep(1)
        disband=driver.find_element(By.XPATH,'//*[@id="q532679399"]/div/div[2]/div/div[2]/div[1]/div[2]/button')
        disband.click()
    except NoSuchElementException:
        pass
    try:
        time.sleep(3)
        allow_button=driver.find_element(By.CSS_SELECTOR, "button[aria-label='Дозволити']")
        allow_button.click()  
    except NoSuchElementException:
        try:
            time.sleep(2)
            not_now_button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Нагадати мені пізніше']")))
            not_now_button.click()
        except (NoSuchElementException, TimeoutException):
            pass
    
    likes=100
    while likes!=0:
        likes-=1
        try:
            try:
                back_button = driver.find_element(By.CSS_SELECTOR, "button[class*='close']")
                back_button.click()
            except NoSuchElementException:
                pass
            like_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='sparks-like-default']")))
            like_button.click()
        except NoSuchElementException:
            time.sleep(2)
        except ElementClickInterceptedException:
            try:
                close_button = driver.find_element(By.CSS_SELECTOR, "button[aria-hidden='false']")
                close_button.click()
            except NoSuchElementException:
                pass
            try:
                close=driver.find_element(By.XPATH, '//*[@id="q532679399"]/div/div/div[2]/button[2]/div[2]/div[2]')
            except NoSuchElementException:
                pass
        except StaleElementReferenceException:
            time.sleep(2)

time.sleep(3)
if driver.current_url == tinder:
    login()
elif 'recs' in driver.current_url:
    like()