import os
from selenium import webdriver
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()

class Filler:
    def __init__(self):
        self.form=os.getenv('FORM')
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)

        self.driver=webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.form)

        self.wait = WebDriverWait(self.driver, 2)
        pass

    def fill(self, links, prices, adresses):
        for i in range(len(links)):
            addres_input=self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            addres_input.send_keys(adresses[i])

            price_input=self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            price_input.send_keys(prices[i])

            link_input=self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            link_input.send_keys(links[i])

            send_button=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Надіслати']")))
            send_button.click()

            another_answer=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Надіслати іншу відповідь']")))
            another_answer.click()

