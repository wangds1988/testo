from time import sleep
from selenium import webdriver


class BasePage():
    driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait(self, time_):
        sleep(time_)

    # 退出
    def quit(self):
        self.driver.quit()
