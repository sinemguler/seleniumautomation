import undetected_chromedriver as uc
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

scheduled_time = datetime(2024, 2, 28, 13, 56, 0)

upload_files_path = os.path.join(os.path.abspath(__file__ + "/../"), "UploadItem")
print(os.listdir(upload_files_path)) #belirtilen dizindeki dosyaların ve klasörlerin listesini ekrana yazdırır.

chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--lang=en-US')


def make_instagram_post():
    driver = uc.Chrome(executable_path="chromedriver.exe", options=chrome_options)

    driver.maximize_window()

    if __name__ == '__main__':
        chrome_options.add_argument('proxy-server=')
        username = ""
        password = ""

    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(10)

    username_input = driver.find_element_by_name("username")
    username_input.send_keys(username)

    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)

    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    save_info_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save info']")))
    save_info_button.click()

    not_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
    not_now_button.click()

    # profile_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Profile')])[1]")))
    # profile_element.click()

    new_post_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@aria-label='New post'])[1]")))
    new_post_button.click()

    select_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Select from computer']")))
    select_button.click()

# file_list = os.listdir(upload_files_path)
# if not file_list:
#     print("UploadItem dizininde dosya bulunamadı.")
#     driver.quit()
#     exit()
#
# first_file = os.path.join(upload_files_path, file_list[0])
# file_input = driver.find_element(By.XPATH, "//input[@type='file']")
# file_input.send_keys(first_file)
#
# time.sleep(5)

    for index, upload_item in enumerate(os.listdir(upload_files_path)): # ile belirlediğimiz dizindeki dosyaların listesini alırız. enumerate fonksiyonu ile her dosyanın indeksini ve adını alırız. Her bir öğe için, index değişkenine indeks değeri atanır ve upload_item değişkenine o öğenin adı atanır.
        time.sleep(2)
    pyautogui.typewrite(f"{upload_files_path}\{upload_item}") #pyautogui kütüphanesi ile klavye girişi yaparak dosya yükleme alanına yazar
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    if index + 1 != len(os.listdir(upload_files_path)): #eğer henüz son dosyaya gelinmemişse (indeks + 1, toplam dosya sayısına eşit değilse), yeni bir gönderi yapmak için gereken işlemleri gerçekleştirir.
        driver.find_element_by_xpath("//*[@aria-label='Open media gallery']").click()
        driver.find_element_by_xpath("//*[@aria-label='Plus icon']").click()

    ok_button = driver.find_element_by_xpath("//button[text()='OK']")
    ok_button.click()

    driver.find_element_by_xpath("(//div[contains(text(),'Next')])[1]").click()
    driver.find_element_by_xpath("(//div[contains(text(),'Next')])[1]").click()

    caption_input = driver.find_element(By.XPATH, "(//div[@aria-label='Write a caption...'])[1]")
    caption_input.send_keys("Barış alper yılmaz #galatasaray #barışalperyılmaz")

    share_button = driver.find_element(By.XPATH, "(//div[contains(text(),'Share')])[1]")
    share_button.click()

    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.XPATH, "(//div[@class='_ac7a'])[1]"), "Reel shared")) #belirli bir web öğesinde belirli bir metnin görünmesini bekler

    driver.find_element_by_xpath("(//*[name()='svg'][@aria-label='Close'])[1]").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@alt,'trendstopiccc')]")))

    driver.refresh()

def wait_until_schedule():
    while datetime.now() < scheduled_time:
        time.sleep(10)
    make_instagram_post()

wait_until_schedule()
