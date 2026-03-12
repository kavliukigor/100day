from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

# price_dollar=driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents=driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f'{price_dollar.text}.{price_cents.text}')
# name=driver.find_element(By.ID, value='productTitle')
# print(name.text)
# img=driver.find_element(By.CSS_SELECTOR, value='.imgTagWrapper img')
# img_url=img.get_attribute('src')
# print(img_url)
events_find=driver.find_elements(By.CSS_SELECTOR, value='.medium-widget.event-widget.last li')
events_list=[]
events_dict={}
for event in events_find:
    events_list.append(event.text)
for i, event in enumerate(events_list):
    part=event.split('\n')
    events_dict[i]={'time':part[0], 'event':part[1]}
    
print(events_dict)
    
driver.quit()