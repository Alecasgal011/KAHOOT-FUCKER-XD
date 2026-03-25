import os
import subprocess
import random
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def banner():
    os.system("clear")
    print("""
██╗  ██╗       ███████╗██╗     ███████╗███╗   ██╗
██║ ██╔╝       ██╔════╝██║     ██╔════╝████╗  ██║
█████╔╝        █████╗  ██║     █████╗  ██╔██╗ ██║
██╔═██╗        ██╔══╝  ██║     ██╔══╝  ██║╚██╗██║
██║  ██╗  ██╗  ███████╗███████╗███████╗██║ ╚████║
╚═╝  ╚═╝  ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝
          >> BY: Alecasgal :D <<
----------------------------------------------
""")
NombresToWapos = ["Kepa jamecho", "Missué Villos", "Kepo Jhon", "Elva Ginazo", "Benito Camela", "Jeffrey Epstein", "Free Maduro", "Laver Gamez Torba"]
LosElegidos = random.sample(NombresToWapos, 5) #son 12 gb no ocupará mucho seguro :D (matame)
def SeMeten(NombreDelBot, PinDeLobby):
    driver = None
    try:
        conf = Options()
        conf.add_argument('--headless')
        conf.add_argument('--no-sandbox')
        conf.add_argument('--disable-dev-shm-usage')
        servicio = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=servicio, options=conf)
        wait = WebDriverWait(driver, 20)
        driver.get("https://kahoot.it")
        time.sleep(5)
        print(f"Google para {NombreDelBot}")
        cuadro_pin = wait.until(EC.presence_of_element_located((By.ID, "game-input")))
        cuadro_pin.send_keys(PinDeLobby)
        cuadro_pin.send_keys(Keys.ENTER)
        time.sleep(2)
        Nick = wait.until(EC.presence_of_element_located((By.ID, "nickname")))
        Nick.send_keys(NombreDelBot)
        Nick.send_keys(Keys.ENTER)

        print(f"{NombreDelBot} se ha metido :D")
        while True:
            time.sleep(60)
    except Exception as e:
        print(f" [!] {NombreDelBot} se ha colgado por el Wi-Fi :(")
    finally:
        if driver:
            driver.quit()

banner()
PinDeLobby = input("[?] Pin del kahoot --> ")
print("\n [!] ATAQUE!!!")
time.sleep(1)
os.system("clear")
banner()
print(f"    [>] | TARGET LOCKED | {PinDeLobby}")
print("   -------------------------------------------\n")

for n in LosElegidos:
    hilo = threading.Thread(target=SeMeten, args=(n, PinDeLobby))
    hilo.start()
    time.sleep(0.5)
print("\n  [*] Los Bots ya van por ahi ;)")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n [!] MIERDA MIERDA CORTA CORTA")
    time.sleep(1)
    os.system("clear")
