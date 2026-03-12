from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://ozh.github.io/cookieclicker/')
time.sleep(2)

language=driver.find_element(By.CLASS_NAME, value='langSelectButton.title')
language.click()


time.sleep(2)
start_time=time.time()
last_upgrade_check = time.time()
while True:
    
    try:
        cookie=driver.find_element(By.ID, value='bigCookie')
        cookie.click()
        if time.time() - last_upgrade_check > 2:
            last_upgrade_check = time.time()
            count = driver.find_element(By.ID, 'cookies')
            count_final = int(count.text.split('\n')[0].split(' ')[0])
            upgrades = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked')
            enable = []
            for upgrade in upgrades:
                price = upgrade.find_element(By.CLASS_NAME, 'price').text.strip()
                price = int(price.replace(',', ''))
                if price <= count_final:
                    enable.append((price, upgrade))
            if enable:
                enable.sort()
                enable[-1][1].click()
        
        if time.time() - start_time > 300:
            print(driver.find_element(By.ID, 'cookies').text)
            driver.quit()
            break
            
    except:
        print('Вікно закрито')
        break