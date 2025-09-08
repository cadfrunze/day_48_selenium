from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as econ
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

def kill_popup(waiting: WebDriverWait) -> None:
    try: 
        kill_popup: WebElement = waiting.until(econ.element_to_be_clickable(mark=(By.CSS_SELECTOR, ".pum-close.popmake-close")))
        kill_popup.click()
    except TimeoutException:
        pass
    except StaleElementReferenceException:
        pass
