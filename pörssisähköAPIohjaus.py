import requests
import pandas as pd
from datetime import datetime, timedelta

url =  "https://api.spot-hinta.fi/Today"

heat=False

format = '%Y/%m/%d %H:%M:%S'

response = requests.get(url)

if response.status_code == 200:
    x = response.text # hae tiedot netistä
else:
    print(f"Error{response.status_code}")

df = pd.read_json(x) # tiedot pandas taulukoksi

df['DateTime'] = df['DateTime'].dt.strftime(format) # päivä ja aika oikeaan muotoon


print(df.to_string())




def neljäHalvinta(): # Funktio etsii neljän halvimman tunnin index numerot ja palauttaa ne listana 

    #Haetaan halvimmat tunnit rank numeron perusteella
    id1 = df.index[df['Rank'] == 1].tolist()
    id2 = df.index[df['Rank'] == 2].tolist()
    id3 = df.index[df['Rank'] == 3].tolist()
    id4 = df.index[df['Rank'] == 4].tolist()


    halvat = [id1[0],id2[0],id3[0],id4[0]] # Halvat hinnat listaksi

    return halvat

def kaksiHalvinta(): # Funktio etsii kahden halvimman tunnin index numerot ja palauttaa ne listana 

    #Haetaan halvimmat tunnit rank numeron perusteella
    id1 = df.index[df['Rank'] == 1].tolist()
    id2 = df.index[df['Rank'] == 2].tolist()



    halvat = [id1[0],id2[0]] # Halvat hinnat listaksi

    return halvat



def onkoHalpaJakso(halpaLista): # Funktio looppaa index listan tunnit läpi ja laittaa lämmityksen päälle jos on halpa jakso nyt

    global heat

    for y in halpaLista: #Loopataan halvat hinnat. Onko halpa jakso nyt


        d = df["DateTime"].values[y] # hae halpa hinta solusta id:n perusteella

        hinta = str(df["PriceWithTax"].values[y])
        hinta = hinta[:5]

        current_time = datetime.now() # hae aika nyt
        current_time = current_time.strftime(format)


        current = datetime.strptime(current_time, format) # Aika oikeaan muotoon
        CompareDate = datetime.strptime(d, format) # Aika oikeaan muotoon
        plusHour = CompareDate+timedelta(hours=1) # Vertailu aika + 1h
        

        if current>CompareDate and current<plusHour: # Jos tämän hetkinen aika on halvan sähkön tunnin sisällä lämmitys päälle
            print("Halpa sähkö päälle")
            heat=True
            break

        else:
            print("Kallis sähkö, pois päältä. Hinta nyt yli " + hinta + " euroa")
            heat=False





neljäH = neljäHalvinta() # Lista muuttujaksi

kaksiH = kaksiHalvinta()  # Lista muuttujaksi


onkoHalpaJakso(kaksiH) # Käynnistetään funktio halutulla listalla



#testataan onko lämmitys nyt päällä ja ilmoitetaan käyttäjälle

if heat:

    print("Ohjelma loppunut lämmitys on päällä")
          
else:
    print("Ohjelma loppunut lämmitys on pois")