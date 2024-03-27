import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains


username = ""
password = ""


upload_files_path = os.path.join(os.path.abspath(__file__ + "/../"), "UploadItem")


scheduled_time = datetime(2024, 3, 20, 10, 33, 0)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=en-US')

def make_tiktok_post():
    driver = uc.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    driver.maximize_window()

    driver.get("https://www.tiktok.com/tr-TR/")
    driver.implicitly_wait(20)


    login(driver)


    for upload_item in os.listdir(upload_files_path):
        upload_media(driver, upload_item)

def login(driver):

    button = driver.find_element(By.XPATH, "(//div[@role='link'])[2]")
    button.click()

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'E-posta veya kullanıcı adıyla giriş yapın')])[1]")))
    login_button.click()

    email_or_username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='E-posta veya kullanıcı adı'])[1]")))
    email_or_username_input.send_keys(username)

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Şifre'])[1]")))
    password_input.send_keys(password)

    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='submit'][contains(text(),'Giriş yapın')])[1]")))
    submit_button.click()

    print('Waiting 30s for manual login...')
    time.sleep(30)

def upload_media(driver, upload_item):

    div_upload = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1qup28j-DivUpload e18d3d944'])[1]")))

    ActionChains(driver).move_by_offset(50, 50).click().perform()
    div_upload.click()

    select_file_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "(//button[@aria-label='Select file'])[1]")))
    select_file_button.click()

    time.sleep(2)
    pyautogui.typewrite(os.path.join(upload_files_path, upload_item))
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)

    caption_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Caption']")))
    caption_div.clear()
    caption_div.send_keys("Bu bir açıklama")
    time.sleep(2)

    submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='css-y1m958'])[1]")))
    submit_button.click()
def wait_until_schedule():

    while datetime.now() < scheduled_time:
        time.sleep(10)
    make_tiktok_post()

if __name__ == "__main__":
    wait_until_schedule()




