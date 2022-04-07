#made by Axxira
#Gausa di otak atik dek nanti rusak

from operator import ne
import time
import pyautogui
from selenium import webdriver

username = "03202100xx" #ISI NIM DISINI
password = "password"  #ISI PASSWORD DISINI
isikontak   = "Ayah - 0813xxxxxxxx" #ISI KONTAK DISINI
#[1]Sinopharm
#[2]Sinovac
#[3]AstraZeneca
#[4]Pfizer
#[5]Modersa
vaksin = 2    #Pilih list di atas, default 2 (sinovac)
pilih1_number = 2
pilih2_number = 1

path = "chromedriver.exe"

web = webdriver.Chrome(path)
web.get('https://satgas-covid19.polman.astra.ac.id/mahasiswa/Page_Login.aspx')


time.sleep(2)

loginuser = web.find_element_by_xpath('//*[@id="txtUsername"]')
loginuser.send_keys(username)

loginpass = web.find_element_by_xpath('//*[@id="txtPassword"]')
loginpass.send_keys(password)

loginbtn = web.find_element_by_xpath('//*[@id="btnLogin"]')
loginbtn.click()

time.sleep(2)

absenbtn = web.find_element_by_xpath('//*[@id="btnAbsensi"]')
absenbtn.click()

salin = web.find_element_by_xpath('//*[@id="MainContent_divAddStep1"]/div/div[2]/div[3]/div[1]/div/label')
salin.click()

pilih1 = web.find_element_by_xpath('//*[@id="addTemanAstra"]')
pilih1.click()

for _ in range (pilih1_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

time.sleep(1)

kontak = web.find_element_by_xpath('//*[@id="MainContent_addKontakLain"]')
kontak.clear()
kontak.send_keys(isikontak)

kendaraan = web.find_element_by_xpath('//*[@id="addKendaraanUmum"]')
kendaraan.click()

for _ in range (pilih1_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

kesehatan = web.find_element_by_xpath('//*[@id="addRumahSakit"]')
kesehatan.click()

for _ in range (pilih1_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

next1 = web.find_element_by_xpath('//*[@id="MainContent_linkSubmitAdd"]')
next1.click()

time.sleep(2)
kesehatan1 = web.find_element_by_xpath('//*[@id="addSehatSelf"]')
kesehatan1.click()

for _ in range (pilih2_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

kesehatan2 = web.find_element_by_xpath('//*[@id="addSehatFamily"]')
kesehatan2.click()

for _ in range (pilih2_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

covid1= web.find_element_by_xpath('//*[@id="addCovidSelf"]')
covid1.click()

for _ in range (pilih1_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

covid2= web.find_element_by_xpath('//*[@id="addCovidAround"]')
covid2.click()

for _ in range (pilih1_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

vaksin1 = web.find_element_by_xpath('//*[@id="addMenerimaVaksin"]')
vaksin1.click()

for _ in range (pilih2_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

vaksin2 = web.find_element_by_xpath('//*[@id="addSuntikanVaksin"]')
vaksin2.click()

for _ in range (vaksin):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

vaksin3 = web.find_element_by_xpath('//*[@id="addNamaVaksin"]')
vaksin3.click()

for _ in range (pilih1_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

sertifikat = web.find_element_by_xpath('//*[@id="addSertifikatVaksin"]')
sertifikat.click()

for _ in range (pilih2_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

penyakit = web.find_element_by_xpath('//*[@id="MainContent_divAddStep2"]/div/div[2]/div[9]/div/div[7]/label')
penyakit.click()

next2 = web.find_element_by_xpath('//*[@id="MainContent_linkSubmitAdd"]')
next2.click()

time.sleep(2)

magang = web.find_element_by_xpath('//*[@id="addIsMagang"]')
magang.click()

for _ in range (pilih1_number):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

next3 = web.find_element_by_xpath('//*[@id="MainContent_linkSubmitAdd"]')
next3.click()

time.sleep(2)

ask1 = web.find_element_by_xpath('//*[@id="MainContent_gridPertanyaan_radioPertanyaanTidak_0"]')
ask1.click()

ask2 = web.find_element_by_xpath('//*[@id="MainContent_gridPertanyaan_radioPertanyaanTidak_1"]')
ask2.click()

ask3 = web.find_element_by_xpath('//*[@id="MainContent_gridPertanyaan_radioPertanyaanTidak_2"]')
ask3.click()

ask4 = web.find_element_by_xpath('//*[@id="MainContent_gridPertanyaan_radioPertanyaanTidak_3"]')
ask4.click()

ask5 = web.find_element_by_xpath('//*[@id="MainContent_gridPertanyaan_radioPertanyaanTidak_4"]')
ask5.click()

ask6 = web.find_element_by_xpath('//*[@id="MainContent_gridPertanyaan_radioPertanyaanTidak_5"]')
ask6.click()

ask7 = web.find_element_by_xpath('//*[@id="MainContent_gridPertanyaan_radioPertanyaanTidak_6"]')
ask7.click()

next4 = web.find_element_by_xpath('//*[@id="MainContent_linkSubmitAdd"]')
next4.click()


print("Absen Selesai Gan..")