# Automating Facebook Page so it logins and posts

from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

username = "username"     # Username
password = "password"     # Password


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver.maximize_window()
# driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

chrome_options.add_experimental_option("detach", True)

webln = webdriver.Chrome(options=chrome_options)  # open chrome
webln.get('https://lms.umt.edu.pk/my')

lname = webln.find_element(By.ID, 'username')
lpass = webln.find_element(By.ID, 'password')
login_button = webln.find_element(
    By.ID, 'loginbtn')

lname.send_keys(username)
lpass.send_keys(password)
print("Sent Credentials")

sleep(1)

login_button.click()

# try:
#     element = WebDriverWait(webln, 20).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="page-container-1"]/div/ul/li[1]/div/div[1]/div/a/text()'))
#     )
# except:
#     print("Something went wrong")
# else:
#     # Logged in

sleep(1)
course = webln.find_element(By.XPATH, '//*[@id="page-container-1"]/div/ul/li[2]/div/div[1]/div/a')
course.click()

sleep(4)

skip_btn = webln.find_element(By.XPATH, '//*[@id="page-course-view-tiles"]/div[6]/div[2]/div/div/div[3]/button[2]')
skip_btn.click()

sleep(1)
youtube_link = webln.find_element(By.XPATH, '//*[@id="module-1410490"]/div/div/a/span')
youtube_link.click()


