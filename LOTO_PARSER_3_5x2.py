import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def parsing_3x5_3(driver):
    # Откройте веб-страницу
    url = "https://www.stoloto.ru/5x2/archive/"
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
    for i in range(1, 8):  # Добавляем заголовки для чисел с 1 по 7
        headers.append(f"Число {i}")
    ws.append(headers)

    # Найдите итерации с данными
    main_divs = driver.find_elements(By.CLASS_NAME, "sc-1103baef-1")
    for main_div in main_divs:
        date = main_div.find_element(By.CLASS_NAME, "sc-b80da79c-2").text
        draw_number = int(main_div.find_element(By.CLASS_NAME, "sc-431aa42b-0").text)
        payouts = int(main_div.find_element(By.CLASS_NAME, "sc-b80da79c-5").text.replace(" ", ""))
        print(date," - ",draw_number," - ",payouts)
        numbers_li = main_div.find_elements(By.CLASS_NAME, "sc-7e65da55-0")

        # Преобразование в целые числа с обработкой возможных ошибок
        numbers = []
        for num in numbers_li:
            try:
                num_int = int(num.text)
                numbers.append(num_int)
            except ValueError:
                pass  # Пропустить недопустимые значения

        # Добавьте данные в Excel, разделяя числа слэшем
        data_row = [date, draw_number, payouts] + numbers
        ws.append(data_row)

    # Сохраните файл Excel
    wb.save("results3.xlsx")
