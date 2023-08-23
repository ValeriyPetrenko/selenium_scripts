import time
# Импортируем "Time" для создание пауз при загрузке страницы. Так как необходимый нам элемент может не прогрузиться на момент начала скрипта.
from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортируем основные модули необходимые для работы.
from selenium.webdriver.common.keys import Keys
# Keys тут необходим для ввода текста путём имитации нажатия Enter.
import requests
# С помощью "Requests" получим ответ на GET-запрос и в случае возникновение проблем будем знать код ответа.
driver = webdriver.Chrome()
# Создаём переменную "driver" в которой указываем название браузера.
response = requests.get("https://www.livelib.ru/")
print(response)
# Создаём GET-запрос и выводим ответ от сервера в окно терминала.
driver.get("https://www.livelib.ru/") # Указываем полный URL адрес.
driver.maximize_window()
# Переходим в полноэкранный режим, для удобства при дальнейшем создании скриншота.
time.sleep(5)
driver.find_element(By.ID, "header-top-search-form").click()
# Заранее с помощью DevTools находим название необходимого элемента. Находим его, после имитируем нажатие левой кнопки мыши.
time.sleep(5)
driver.find_element(By.CLASS_NAME, "ll-input-search").send_keys("мастер и маргарита")
# Вводим текст, заведомо написав название книги в нижнем регистре.
time.sleep(5)
driver.find_element(By.CLASS_NAME, "ll-input-search").send_keys(Keys.ENTER)
# Имитируем нажатие клавиши Enter.
time.sleep(5)
driver.find_element(By.CLASS_NAME, "btn-search-new").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CLASS_NAME, "btn-search-new").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CLASS_NAME, "btn-search-new").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CLASS_NAME, "btn-search-new").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CLASS_NAME, "btn-search-new").send_keys(Keys.ARROW_DOWN)
# Имитируем нажатие клавиши "Вниз" несколько раз чтобы увидеть результат поиска.
time.sleep(5)
driver.get_screenshot_as_file("C:\Проекты\search.png")
# Сохраняем резултьтат теста, сохранив скриншот. Путь к файлу можно изменить на любую папку в вашей файловой системе.
time.sleep(5)
