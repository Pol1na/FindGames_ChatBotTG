from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def find_game(name_game):

    chromedriver = 'C:\\Users\\Pol1na\\Desktop\\selenium\\chromedriver'
    driver = webdriver.Chrome(chromedriver)
    delay = 3 # секунды
    # options = webdriver.ChromeOptions()
    # binary_yandex_driver_file = 'yandexdriver.exe'
    # driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
    driver.get('https://iwillplay.ru/')
    try:
        textarea = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/section[1]/div[1]/div/div/div[2]/form/div/div[2]/input')))
        textarea.send_keys(name_game)
    except TimeoutException:
        print ("Loading took too much time!")

    button_first = driver.find_element_by_name('search-btn')
    button_first.click()
    games = {}
    for game in driver.find_elements_by_class_name('name'):
        games[game.text] = game
    return games, driver


def get_url(game, driver):
    button_second = game
    button_second.click()
    current_URL = driver.current_url
    # button_third = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div/div[4]/div[1]/div/div[8]/a')
    # button_third.click()
    driver.quit()
    return current_URL