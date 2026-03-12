from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
load_dotenv()
from datetime import datetime,timedelta

email=os.getenv('ACCOUNT_EMAIL')
password=os.getenv('ACCOUNT_PASSWORD')
url=os.getenv('GYM_URL')
days=['tue','thu']

user_data_dir=os.path.join(os.getcwd(),'chrome_profile')

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')


driver=webdriver.Chrome(options=chrome_options)
driver.get(url)
wait = WebDriverWait(driver, 10)
def login():
    connect_button=driver.find_element(By.CSS_SELECTOR,value='.Home_heroButton__3eeI3')
    connect_button.click()
    wait.until(EC.presence_of_element_located((By.ID, 'email-input')))

    email_input=driver.find_element(By.ID, value='email-input')
    email_input.clear()
    email_input.send_keys(email)

    password_input=driver.find_element(By.ID, value='password-input')
    password_input.clear()
    password_input.send_keys(password)

    login_button=driver.find_element(By.ID, value='submit-button')
    login_button.click()
    wait.until(EC.presence_of_element_located((By.ID, 'schedule-page')))

    time.sleep(1)
    pyautogui.click(x=1193, y=421)

def book_class(day):
    cont=driver.find_element(By.CSS_SELECTOR, f'div[id*="{day}"]')
    events_day=cont.find_elements(By.CSS_SELECTOR, 'div[id*="class-card"]')
    evening_event=[event for event in events_day if '1800' in event.get_attribute('id')]

    if not evening_event:
        return 0, 0, 0, []
        
    class_data=cont.find_element(By.TAG_NAME, value='h2').text
    class_type=evening_event[0].find_element(By.CSS_SELECTOR, 'h3[id*="class-name"]').text
    class_time=evening_event[0].find_element(By.CSS_SELECTOR, 'p[id*="class-time"]').text
    class_time=class_time.split(': ')[1]

    booked=0
    waitlist=0
    book=0
    detailed_list=[]
    for element in evening_event:
        book_button=element.find_element(By.CSS_SELECTOR, 'button[id*="book"]')
        text=book_button.text
        if text=='Book class':
            book_button.click()
            print(f'✓ Successfully booked: {class_type} on {class_data} at {class_time}')
            booked+=1
            detailed_list.append(f'• [New Booking] {class_type} on {class_data}')
        elif text=='Booked':
            print(f'Alredy booked: {class_type} on {class_data} at {class_time}')
            book+=1
            detailed_list.append(f'• [Booked] {class_type} on {class_data}')
        elif text=='Waitlisted':
            print(f'Waitlisted: {class_type} on {class_data} at {class_time}')
            waitlist+=1
            detailed_list.append(f'• [Waitlisted] {class_type} on {class_data}')
        elif text=='Join Waitlist':
            print(f'✓ Joined waitlist for: {class_type} on {class_data} at {class_time}')
            detailed_list.append(f'• [Added to waitlist] {class_type} on {class_data}')
            book_button.click()

    return booked, waitlist, book, detailed_list

def get_bookings(days):
    total_booked = 0
    total_waitlist = 0
    total_book = 0
    total_detailed = []
    for day in days:
        booked, waitlist, book, detailed_list = book_class(day)
        total_book+=book
        total_booked+=booked
        total_detailed.append(detailed_list)

    print(f"""
    --- BOOKING SUMMARY ---
    New bookings: {total_booked}
    New waitlist entries: {total_waitlist}
    Alredy booked/waitlisted: {total_book}
    Total Tuesday & Thursday 6pm classes: {total_booked + total_waitlist + total_book}

    --- DETAILED CLASS LIST ---
    """)
    for item in total_detailed:
        for line in item:
            print(line)

    bookings_link=driver.find_element(By.CSS_SELECTOR, 'a[id*="my-bookings-link"]')
    bookings_link.click()

    bookings=driver.find_elements(By.CSS_SELECTOR, 'div[id*="booking-card-booking"]')
    today = datetime.today()
    week_later = today + timedelta(days=7)
    booking_list = []
    for booking in bookings:
        strong = booking.find_element(By.TAG_NAME, 'strong')
        date = strong.find_element(By.XPATH, '..').text
        for day in days:
            if day.capitalize() + ',' in date and '6:00 PM' in date:
                date_part = date.replace('When: ', '').split(', ')
                date_str = f"{date_part[1]} {date_part[2]} {today.year}"
                booking_date = datetime.strptime(date_str, "%b %d %I:%M %p %Y")
                if today.date() <= booking_date.date() <= week_later.date():
                    booking_list.append(booking.text)
            
    print(booking_list)

    booking_num=len(booking_list)
    expected = total_booked + total_waitlist + total_book

    if booking_num == expected:
        res=f'✅ SUCCESS'
    else:
        res=f'❌ MISMATCH'

    print(f"""
    --- VERIFICATION RESULT ---
    Expected: {expected} bookings
    Found: {booking_num} bookings
    {res}
    """)

def retry(func, retries=7):
    while retries!=0:
        try:
            func()
            retries=0
            return
        except Exception as e:
            print(e)
            retries-=1
        print(f'Fail after 7 tries')

retry(login)
retry(lambda: get_bookings(days))