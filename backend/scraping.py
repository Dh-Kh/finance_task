from typing import Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

#потом отключить службу постгрес
def get_price(url: str) -> Union[str, None]:
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-blink-features=AutomationControlled')
    #maybe no need to use webdriver.Remote make researches about it
    driver = webdriver.Remote(
        #service=Service(ChromeDriverManager().install()), 
        command_executor="http://127.0.0.1:4444/ui",
        options=options
    )
    driver.get(url)
    wait = WebDriverWait(driver, 3)
    try:
        current_price = wait.until(
            EC.visibility_of_element_located((
                By.XPATH, '//div[@class="YMlKec fxKbKc"]'
            )
        ))
        return current_price.text
    except TimeoutException:
        return None
    driver.close()
    driver.quit()



