from dotenv import load_dotenv
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.webkitgtk.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as econ
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
load_dotenv()

TARGET:str = os.getenv("target")
# PATH: str = os.getenv("path_chrome")

options_chrome: Options = ChromeOptions() 
# options_chrome.binary_location = fr"{PATH}"
options_chrome.add_experimental_option("detach", True)

engine: WebDriver = Chrome(options=options_chrome)
engine.get(TARGET)
engine.fullscreen_window()
# print(type(options_chrome))
# print(type(engine))
# print(isinstance(options_chrome, ChromeOptions))
waiting: WebDriverWait = WebDriverWait(engine, 10)

try: 
    kill_popup: WebElement = waiting.until(econ.element_to_be_clickable(mark=(By.CSS_SELECTOR, ".pum-close.popmake-close")))
    kill_popup.click()
except TimeoutException as e:
    pass

while True:
    try:
        
        search_box = engine.find_element(by=By.CLASS_NAME, value='s')
        search_box.click()
        search_box.clear()
        search_box.send_keys("s24\n")
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
