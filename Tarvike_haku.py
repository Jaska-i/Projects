from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#Haettavat keikka numerot
keikat = ['1073140', '1070868', '1070609', '1070474', '1068225', '1066885', '1065529', '1064301', '1062212', '1061460', '1061422', '1061078', '1058759', '1058357', '1058344', '1058341', '1057221', '1054974', '1052606', '1049873', '1049700', '1049036', '1048690', '1048146', '1047778', '1010584', '1043287', '1042628', '1041013', '1040337', '1030880', '1028727', '1028189', '1026445', '1026061', '1025332', '1024778', '1023658', '1017370', '1017163', '1013238', '1012639', '1008359', '1008244', '1007504', '1006206', '1002657', '1001879', '997406', '997344', '992844', '992781', '992692', '992599', '988981', '988963', '986733', '985865', '985401', '984841', '981656', '981076', '980541', '980358', '980011', '979654', '979020', '978477', '976617', '976327', '976323', '975775', '974978', '974857', '973312', '972486', '972198', '970338', '970226', '968399', '967887', '966443', '962408', '961782', '961724', '957703', '950578', '947389', '947364', '946730', '945030', '942369', '942347', '940786', '940759', '940122', '939643', '939239', '935100', '930025', '929652', '927639', '921067', '917528', '917018', '908201', '903390', '896519', '896071', '895185', '895156', '894518', '892861', '891685', '891477', '890822', '884171', '882820', '881866', '880257', '879482', '877816', '876700', '874861', '872764', '871890', '869393', '867250', '846962', '846487', '845305', '838861', '838695', '836955', '835501', '834434', '834070', '833264', '832665', '832174', '831745', '831733', '831704', '831255', '830757', '828185', '827348', '824951', '824950', '824925', '824215', '823534', '821622', '820679', '820503', '819140', '817094', '816237', '814855', '811758', '811756', '810764', '810748', '810696', '810694', '809190', '809070', '807933', '807071', '806189', '805940', '802943', '802842', '802839', '801212', '800817', '800397', '799959', '799619', '799555', '798949', '796268', '796079', '794050', '793873', '789926', '789420', '786508', '786439', '782493', '775399', '774653', '772977', '770731', '770457', '770409', '766966', '761916', '760437', '753903', '753891', '753790', '748750', '748319', '747845', '747355', '743001', '742957', '742954', '738471', '738248', '733203', '715907', '712612', '709945', '709400', '709235', '708721', '706773', '705650', '705638', '705394', '703668', '702480', '701738', '700953', '700923', '699559', '699557', '699082', '697046', '696561', '696107', '694156', '693220', '693100', '689878', '686362', '686110', '685752', '684260', '682316', '681480', '679645', '674888', '669524', '668943', '665204', '664143', '663687', '663398', '662781', '661969', '661523', '658706', '658354', '658279', '657174', '655978', '655257', '654850', '653831', '652835', '649156', '649008', '647487', '646517', '645807', '642917', '642869', '640495', '640234', '638562', '638528', '638278', '637994', '632156', '631071', '626484', '621865', '621831', '619498', '309150', '308811']

username = "" # Tähän käyttäjätunnus
password = "" # Tähän salasana
workNum = "1070474"
tarvike = []

url = ("https://app.firasor.fi/")

driver = webdriver.Chrome("G:\ChromeDriver\chromedriver")

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
