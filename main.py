import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_PATH = "C:\developer\chromedriver.exe"
SER = Service(CHROME_PATH)
OP = webdriver.ChromeOptions()
OP.add_argument("--start-maximized")

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_PATH = "C:\developer\chromedriver.exe"
TWITTER_EMAIL = "email@gmail.com"
TWITTER_PASS = "12345678"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(service=SER, options=OP)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a").click()
        time.sleep(60)
        self.down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        try:
            self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        except selenium.common.exceptions.NoSuchElementException:
            time.sleep(3)
            self.driver.find_element(By.LINK_TEXT, "Sign in").click()

        time.sleep(5)
        email = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        pas = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pas.send_keys(TWITTER_PASS)
        pas.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Provider why my speed Down: {self.down} & Up:{self.up} while promise speed is 150mbps")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span').click()


tw_bot = InternetSpeedTwitterBot()
tw_bot.get_internet_speed()
time.sleep(5)
tw_bot.tweet_at_provider()