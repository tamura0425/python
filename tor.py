from selenium import webdriver
from http://selenium.webdriver.chrome.options import Options
import subprocess
import time

tor = f' ""'

p = subprocess.Popen(tor)
options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')

driver = http://webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)
driver.get()
