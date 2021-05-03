from selenium import webdriver
import os
from config import username, password
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random


browser = None


def login_chrome(_username, _password):
    global browser

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    browser.implicitly_wait(5)
    browser.get("https://www.instagram.com")

    time.sleep(random.randint(1, 7))

    _username_ = browser.find_element(By.NAME, "username")
    _username_.clear()
    _username_.send_keys(_username)

    time.sleep(random.randint(1, 2))

    _password_ = browser.find_element(By.NAME, "password")
    _password_.clear()
    _password_.send_keys(_password)

    time.sleep(random.randint(1, 2))

    _login_button = browser.find_element_by_css_selector('''button[type="submit"]''')
    _login_button.click()

    time.sleep(random.randint(1, 2))


def close_browser():
    global browser

    browser.close()


def check_followed(main_user, followed_user):
    global browser

    time.sleep(random.randint(1, 2))

    browser.get(f"https://www.instagram.com/{main_user}/")

    followers_button = browser.find_element_by_css_selector(f'''a[href="/{main_user}/followers/"]''')
    followers_button.click()

    time.sleep(random.randint(1, 2))

    try:
        browser.find_element_by_css_selector(f'''a[title="{followed_user}"]''')
        print("FOUND")
    except NoSuchElementException:
        print("NOT FOUND")


login_chrome(username, password)
time.sleep(5)
check_followed("alexei.pozdnyakov", "nt_crckr")
print("OUT")
time.sleep(100)
close_browser()
