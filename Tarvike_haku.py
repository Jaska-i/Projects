from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#Haettavat keikka numerot
keikat = ["keikka1", "keikka2"] # tähän keikkanumerot stringinä

username = "user" # Tähän käyttäjätunnus
password = "pass" # Tähän salasana
workNum = "111111"
tarvike = []

url = ("https://app.esimerkki.fi/") # tähän osoite

driver = webdriver.Chrome("ChromeDriver\chromedriver")

driver.get(url)

action = ActionChains(driver)# Luo actionchain tuplaklikkausta varten
#Kirjaudu sivulle

driver.find_element(By.NAME,"login_username").send_keys(username)
driver.find_element(By.NAME,"login_password").send_keys(password)
driver.find_element(By.CLASS_NAME,"etusivu_kirjautuminen_ok_button").click()


print("kirjauduttu")

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/nav/div/div[2]/ul/li[6]/a").click()

driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/nav/div/div[2]/ul/li[6]/ul/li[3]/a").click()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[3]/div[2]/ul/li[19]/a").click()#Klikkaa kaikki välilehti

time.sleep(1)

driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[1]/div[4]/div[1]/div/input").click()#Avaa haku kenttä

time.sleep(1)

luku = 0 # luodaan laskuri

#Haetaan kaikilla keikat listan keikkanumeroilla tarvikkeet
for keikkaNumero in keikat:

    luku += 1# Laskuri +1

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[1]/div[4]/div[1]/div/input").send_keys(keikkaNumero)#Syötä työnumero

    time.sleep(1)

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[1]/div[4]/div[1]/div/input").send_keys(Keys.RETURN)# Paina Enter

    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[3]/div[4]/div/div[1]/div/div[2]/table/tbody/tr/td[1]").click()#Avaa keikka

    time.sleep(3)

    oldHandle = driver.window_handles

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[3]/div[4]/div/div[1]/div/div[2]/table/tbody/tr[2]/td/div/div/div[1]/div/a[1]/span/span").click()#Paina muokkaa

    time.sleep(3)

    # Siirry pop-up ikkunaan

    newHandle = driver.window_handles


    # Vaihda webdriver pop up ikkunaan
    driver.switch_to.window(newHandle[0])

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[11]/table/tbody/tr[2]/td/div/div/div[7]/div[2]/div[2]/table/tbody/tr[1]/td/div/button[1]").click()#Avaa tarvikkeet


    x = driver.find_elements(By.CLASS_NAME, "tyolajikkeen_kentan_sisalto")#Hae tarvikkeet

    #Tee tarvikkeista lista

    for y in x:
        i = y.text
        tarvike.append(i)



    #Tallenna tarvike jos se sisältää 7 numeroa

    Sähkötarvike = [] # luo väliaikainen lista tutkittavilla tarvikkeille

    #Käy läpi sivun tarvikkeet ja tallenna ne Sähkötarvike listaan jos ne sisältää 7 numeroa eikä yhtään kirjainta
    #Vain sähkönumerot tallennetaan

    for z in tarvike:


        stre = z
        countl = 0
        countn = 0
        for i in stre:
            if i.isalpha():
                countl += 1

            if i.isdigit():
                countn += 1


        if countn == 7 and countl == 0:
            Sähkötarvike.append(stre)

        


    taloyhtiö = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[11]/table/tbody/tr[2]/td/div/div/div[7]/div[1]/div[2]/span[2]/span[1]/span/span")




    with open("IV-tarvikkeet.txt", "a", encoding='utf-8') as f:
        f.write(taloyhtiö.text + "\n")
        for x in Sähkötarvike:
            f.write(x + "\n")
        f.write("\n")
        f.close()
    

    time.sleep(1)

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/form/div[11]/table/tbody/tr[1]/th/table/tbody/tr/td[2]/i[3]").click()# sulje pop up ikkuna

    time.sleep(1)
    # Vaihda webdriver takaisin pääikkunaan
    driver.switch_to.window(oldHandle[0])

    time.sleep(2)

    action.double_click(driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[1]/div[4]/div[1]/div/input")).perform()#tuplaklikkaa haku ruutuun
    driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td/div/form/div[9]/div[3]/div[1]/div[4]/div[1]/div/input").send_keys(Keys.DELETE)
    time.sleep(2)

    Sähkötarvike = []
    taloyhtiö = []
    tarvike = []

    print("Haettu keikkoja " + str(luku)+"/" + str(len(keikat)))# Monesko keikka menossa

print("Kaikki keikat haettu")

driver.quit()
