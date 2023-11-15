from LOTO_PARSER_1_zabava import *
from LOTO_PARSER_2_keno2 import *
from LOTO_PARSER_3_5x2 import *
from LOTO_PARSER_4_dvazhdydva import *

import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == "__main__":
    # Установите размер окна браузера на 1600x800
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,800")

    # Инициализируйте драйвер Selenium
    driver = webdriver.Chrome(options=chrome_options)

    while True:
        parsing_zabava1(driver)

        time.sleep(1)

        parsing_keno2_2(driver)

        time.sleep(1)

        parsing_3x5_3(driver)

        time.sleep(1)

        parsing_dvazhdydva_4(driver)

        time.sleep(300)