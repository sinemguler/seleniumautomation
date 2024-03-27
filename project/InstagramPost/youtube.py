import undetected_chromedriver as uc
import os
import time
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

scheduled_time = datetime(2024, 3, 20, 10, 2, 0)
upload_files_path = os.path.join(os.path.abspath(__file__ + "/../"), "UploadItem")

chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--lang=en-US')


def make_youtube_post():
    driver = uc.Chrome(executable_path="chromedriver.exe",
                       options=chrome_options)

    driver.maximize_window()

    if __name__ == '__main__':
        chrome_options.add_argument('proxy-server=')
        chrome_options.add_argument(
            "user-data-dir=")
        chrome_options.binary_location = "chrome.exe"
        username = ""
        password = ""

        driver.get("https://www.youtube.com/")

        driver.find_element_by_css_selector('#buttons ytd-button-renderer a').click()

        driver.find_element_by_id('identifierId').send_keys(username)
        time.sleep(2)
        driver.find_element_by_id('identifierNext').click()
        time.sleep(2)

        password_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))

        password_field.send_keys(password)

        password_next_button = driver.find_element(By.CSS_SELECTOR, '#passwordNext')
        password_next_button.click()
        driver.implicitly_wait(10)
        time.sleep(2)

        driver.get("https://www.youtube.com/upload")
        driver.implicitly_wait(10)

        dosya_sec_button = driver.find_element_by_xpath("(//div[normalize-space()='Dosya seç'])[1]")
        dosya_sec_button.click()

    for upload_item in os.listdir(upload_files_path):
        time.sleep(2)
        dosya_yolu = os.path.join(upload_files_path, upload_item)
        pyautogui.typewrite(dosya_yolu)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)

        aciklama_input = driver.find_element(By.XPATH, "(//div[@id='textbox'])[1]")
        aciklama_input.clear()
        aciklama = "Bu bir açıklamadır. Selenium ile eklenmiştir."
        aciklama_input.send_keys(aciklama)
        time.sleep(2)

        title_input = driver.find_element(By.XPATH, "(//div[@id='textbox'])[2]")
        title_input.clear()
        title = "Bu bir açıklama"
        title_input.send_keys(title)
        time.sleep(2)

        off_radio_div = driver.find_element_by_xpath("(//div[@id='offRadio'])[1]")
        off_radio_div.click()

        next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
        next_button.click()
        time.sleep(5)

        next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
        next_button.click()
        time.sleep(5)

        next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
        next_button.click()
        time.sleep(50)


        radio_button = driver.find_element(By.XPATH, '//*[@id="privacy-radios"]/tp-yt-paper-radio-button[3]')
        radio_button.click()
        time.sleep(10)

        done_button = driver.find_element(By.XPATH, '//*[@id="done-button"]')
        done_button.click()

        close_button = driver.find_element(By.XPATH, "//*[@id='close-button']/div")
        close_button.click()


def wait_until_schedule():
    while datetime.now() < scheduled_time:
        time.sleep(10)
    make_youtube_post()


wait_until_schedule()
