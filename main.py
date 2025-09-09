from kill_popup import kill_popup
from service_messages import send_messages
from dotenv import load_dotenv
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.webkitgtk.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as econ
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
load_dotenv()

TARGET:str = os.getenv("target")
PATH: str = os.getenv("path_chrome")
DEVICE: str = 's24+'
GIGABYTE: str = 'gb'
NO_TEL: str = os.getenv("nr_telefon")


options_chrome: Options = ChromeOptions() 
options_chrome.binary_location = fr"{PATH}"
options_chrome.add_experimental_option("detach", True)

engine: WebDriver = Chrome(options=options_chrome)
engine.get(TARGET)
engine.fullscreen_window()
waiting: WebDriverWait = WebDriverWait(engine, 10)

kill_popup(waiting)

while True:
    try:
        search_box = engine.find_element(by=By.CLASS_NAME, value='s')
        search_box.click()
        search_box.clear()
        search_box.send_keys(f'{DEVICE}\n')
    except TimeoutException:
        with open('not_work.txt', "w", encoding='utf-8') as doc:
            doc.write(engine.page_source)
        engine.refresh()
        sleep(2)
    except ElementNotInteractableException as e:
        with open('not_work.txt', "w", encoding='utf-8') as doc:
            doc.write(str(e))
    else:
        break

kill_popup(waiting)

all_items: list[WebElement] = [item for item in engine.find_elements(By.CLASS_NAME, "product-wrapper") if DEVICE in item.text.lower() and GIGABYTE.upper() in item.text] 

if len(all_items) > 0:
    for item in all_items:
        descr: str = item.find_element(By.TAG_NAME, 'h3').text
        price: str = item.find_element(By.CLASS_NAME, "wrap-price").find_element(By.TAG_NAME, 'bdi').text
        link: str = item.find_element(By.CLASS_NAME, 'wd-entities-title').find_element(By.TAG_NAME, 'a').get_attribute('href')
        send_messages(f'+4{NO_TEL}', descr, price, link)
        all_items.clear()
try:
    pages_brut: list[WebElement] = engine.find_elements(By.CLASS_NAME, 'page-numbers')
except ElementNotInteractableException:
    engine.quit()
else:
    pages_nav: list[WebElement] = list()
    page2_items: list[WebElement] = list()
    for page in pages_brut:
        try:
            type(int(page.text))
        except ValueError:
            pass
        else:
            pages_nav.append(page)
    for next_page in range(1, len(pages_nav)):
        new_link: str = pages_nav[next_page].get_attribute('href')
        engine.get(new_link)
        sleep(5)
        all_items = [item for item in engine.find_elements(By.CLASS_NAME, "product-wrapper") if DEVICE in item.text.lower() and GIGABYTE.upper() in item.text]

if len(all_items) > 0:
    for item in all_items:
        descr: str = item.find_element(By.TAG_NAME, 'h3').text
        price: str = item.find_element(By.CLASS_NAME, "wrap-price").find_element(By.TAG_NAME, 'bdi').text
        link: str = item.find_element(By.CLASS_NAME, 'wd-entities-title').find_element(By.TAG_NAME, 'a').get_attribute('href')
        send_messages(f'+4{NO_TEL}', descr, price, link)
        all_items.clear()
        