import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_integers_numbers(numbers):
    list_str_numbers = numbers.split()

    int_numbers = []
    for numb in list_str_numbers:
        int_numbers.append(int(numb))

    return int_numbers

def parsing_dvazhdydva_4(driver):
    # Откройте веб-страницу
    url = "https://www.stoloto.ru/dvazhdydva/archive/"
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
    for i in range(1, 5):  # Добавляем заголовки для чисел с 1 по 14
        headers.append(f"Число {i}")
    ws.append(headers)

    #получаем все div'ы с данными
    elements_divs = driver.find_elements(By.CLASS_NAME, "elem")

    #проходимся по всем дивам и извлекаем из них данные
    for element_div in elements_divs:
        #получаем дату
        date = element_div.find_element(By.CLASS_NAME, "draw_date").text
        #получаем тираж
        draw = element_div.find_element(By.CLASS_NAME, "draw").text
        #получаем выплату в int также если есть слово Суперприз\nразыгран убираем его
        payout = int(element_div.find_element(By.CLASS_NAME, "prize").text.replace(" ", "").replace("Суперприз\nразыгран", ""))
        #получаем числа в строчном типе
        str_numbers = element_div.find_element(By.CLASS_NAME, "numbers").text
        #изменяем тип чисел на integer
        numbers = get_integers_numbers(str_numbers)

        print(date, draw, payout, numbers)


        # Добавьте данные в Excel, разделяя числа слэшем
        data_row = [date, draw, payout] + numbers
        ws.append(data_row)

    # Сохраните файл Excel
    wb.save("results4.xlsx")
