import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def parsing_keno2_2(driver):
    # Откройте веб-страницу
    url = "https://www.stoloto.ru/keno2/archive"
    driver.get(url)

    # Прокрутите страницу вниз 4 раза с задержкой 1 секунда между каждой прокруткой
    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    # Инициализируйте новый файл Excel
    wb = openpyxl.Workbook()
    ws = wb.active

    # Напишите заголовки таблицы Excel
    headers = ["Дата", "Тираж", "Выплаты"]
    for i in range(1, 21):  # Добавляем заголовки для чисел с 1 по 20
        headers.append(f"Число {i}")
    ws.append(headers)

    counter = 0

    # Найдите итерации с данными
    main_divs = driver.find_elements(By.CLASS_NAME, "sc-ccabec07-0")
    for main_div in main_divs:
        date = main_div.find_element(By.CLASS_NAME, "sc-b80da79c-2").text
        print("counter - ", counter)
        draw_number = int(main_div.find_element(By.CLASS_NAME, "sc-431aa42b-0").text)  # Преобразование в целое число
        payouts = int(main_div.find_element(By.CLASS_NAME, "sc-b80da79c-5").text.replace(" ", ""))

        numbers_spans = main_div.find_elements(By.CLASS_NAME, "sc-719b8b0-1")
        numbers = [int(span.text) for span in numbers_spans]  # Преобразование в целые числа

        # Добавьте данные в Excel
        data_row = [date, draw_number, payouts] + numbers
        ws.append(data_row)
        counter += 1

    # Сохраните файл Excel
    wb.save("results2.xlsx")
