import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By


def parsing_zabava1(driver):
    # Откройте веб-страницу
    url = "https://www.stoloto.ru/zabava/archive"

    '''
    url = "https://www.stoloto.ru/zabava/archive"
    url = "https://www.stoloto.ru/keno2/archive"
    url = "https://www.stoloto.ru/5x2/archive/"
    url = "https://www.stoloto.ru/dvazhdydva/archive/"
    '''
    driver.get(url)

    # Инициализируйте новый файл Excel
    wb = openpyxl.Workbook()
    ws = wb.active

    # Напишите заголовки таблицы Excel
    headers = ["Дата", "Тираж"]
    for i in range(1, 13):
        headers.append(f"Число {i}")
    ws.append(headers)

    # Найдите итерации с данными
    month_divs = driver.find_elements(By.CLASS_NAME, "month")
    for month_div in month_divs:
        elem_divs = month_div.find_elements(By.CLASS_NAME, "elem")
        for elem_div in elem_divs:
            draw_date = elem_div.find_element(By.CLASS_NAME, "draw_date").text
            draw_number = elem_div.find_element(By.CLASS_NAME, "draw").find_element(By.TAG_NAME, "a").text
            numbers_spans = elem_div.find_elements(By.CLASS_NAME, "zone")

            print(numbers_spans)
            print("ПОСЛЕ")

            # Извлеките числа, игнорируя пустые строки
            numbers = [int(num.text.strip()) if num.text.strip() else None for span in numbers_spans for num in span.find_elements(By.TAG_NAME, "b")]
            print(numbers)
            # Добавьте данные в Excel, включая 12 номеров в числовом формате
            data_row = [draw_date, int(draw_number)] + numbers + [None] * (12 - len(numbers))
            ws.append(data_row)

    # Сохраните файл Excel
    wb.save("results1.xlsx")