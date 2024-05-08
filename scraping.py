from typing import Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

def get_price(url: str) -> Union[str, None]:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    try:
        current_price = wait.until(
            EC.visibility_of_element_located((
                By.XPATH, '//div[@class="YMlKec fxKbKc"]'
            )
        ))
        return current_price.text
    except TimeoutException:
        return None


