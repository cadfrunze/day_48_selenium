from dotenv import load_dotenv
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.webkitgtk.webdriver import WebDriver

load_dotenv()

TARGET:str = os.getenv("target")
PATH: str = os.getenv("path_chrome")

options_chrome: Options = ChromeOptions() 
options_chrome.binary_location = fr"{PATH}"
options_chrome.add_experimental_option("detach", True)

engine: WebDriver = Chrome(options=options_chrome)
engine.get(TARGET)
# print(type(options_chrome))
# print(type(engine))
# print(isinstance(options_chrome, ChromeOptions))