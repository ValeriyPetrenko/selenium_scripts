from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
# Импортируем необходимые библиотеки.
driver = webdriver.Chrome()
driver.implicitly_wait(20)
# В этот раз устанавливаем максимальное время ожидания загрузки страницы, передав значение драйверу.
response = requests.get("https://www.livelib.ru/")
print(response)
# Создаём переменную с Webdriver и другую переменную с URL для проверки ответа от сервера.
driver.get("https://www.livelib.ru/")
driver.maximize_window()
# Передаём Selenium наш URL с которым предстоит работать. Указываем полноэкранный режим работы браузера.
login_button = driver.find_element(By.CLASS_NAME, "page-header__login")
if login_button is None:
    print("Элемент не найден.")
else:
    driver.find_element(By.CLASS_NAME, "page-header__login").click()
# Проверяем есть ли необходимая кнопка "Войти" на странице. Если она есть, скрипт продолжится и нажмёт на необходимый элемент.
driver.find_element(By.ID, "checkin-email").click()
# С помощью DevTools заранее находим элемент и нажимаем на кнопку "Войти".
driver.find_element(By.ID, "checkin-email").send_keys("оченькрутойимэйл@нонарусском.да")
time.sleep(5)
driver.find_element(By.ID, "checkin-email").send_keys(Keys.ENTER)
# Вводим заведомо неверный адрес электронной почты на русском языке.
driver.get_screenshot_as_file("C:\Проекты\login.png")
# Указываем необходимый путь для сохранения скриншота.
