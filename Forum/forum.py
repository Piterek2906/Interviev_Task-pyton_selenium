import Forum.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

class Forum(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\selenium drivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Forum, self).__init__()
        self.implicitly_wait(15)


    def land_page(self):
        self.get(const.BASE_URL)

    def wpisz_imie(self, imie_nazwisko):
        pole_imie = driver.find_element(By.NAME,'your-name')
        pole_imie.send_keys(imie_nazwisko)


    def wpisz_email(self, email):
        pole_email = driver.find_element(By.NAME,'your-email')
        pole_email.send_keys(email)

    def wpisz_temat(self,temat):
        pole_temat = driver.find_element(By.NAME,'your-subject')
        pole_temat.send_keys(temat)

    def wpisz_tekst(self,tekst):
        pole_tekst = driver.find_element(By.NAME,'your-message')
        pole_tekst.send_keys(tekst)
