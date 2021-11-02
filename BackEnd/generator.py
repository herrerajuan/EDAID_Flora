from random import randint, randrange, choice
from datetime import datetime, timedelta
from pymongo import MongoClient
import random as rand

from pymongo.results import InsertOneResult

try:
    conn = MongoClient(
        "mongodb+srv://soledad03:coronavirusbdb@cluster0.epzrv.mongodb.net/Flora?ssl=true&ssl_cert_reqs=CERT_NONE"
    )
    print("Connected to MongoDB")
except:
    print("Could not connect to MongoDB")


author = [
    "BC",
    "FS",
    "M. López, Marin",
    "Molero Mesa, Esteve"
]

location = [
    "MA. Tolox",
    "MA. PN. Sª de las Nieves. Tolox. Carril base del Torrecillas"
]

UTM = ["UF" + str(i) for i in range(1000, 3000)]

lithology = [
    "Domias",
    "Caliza",
    "Mármol",
    "Dolomía",
    "Domias-Caliza"
]

plot_orientation = [
    "N",
    "W",
    "E",
    "S",
    "NE",
    "SE",
    "NW",
    "NS"
]

community = [
    "Abeto pinsapo",
    "Athamantetum vayredanae"
]

specie = [
    "-",
    "+",
    randint(1, 10)
]

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
    
date_random = []
for i in range(0,300):
    d1 = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
    date_random.append(random_date(d1, d2))
    print(date_random)

ITEMS_COUNT = 300

for i in range(ITEMS_COUNT):
    item = {
        "num_register": randint(0, 1000),
        "date": choice(date_random),
        "author": choice(author),
        "location": choice(location),
        "UTM": choice(UTM),
        "lithology": choice(lithology),
        "coverage": randint(0, 100),
        "altitude": randint(1000, 2000),
        "plot_slope": randint(0, 100),
        "altitude_veg": randint(0, 3000),
        "plot_area": randint(0, 3000),
        "plot_orientation": choice(plot_orientation),
        "community": choice(specie),
        "abies_pinsapo": choice(specie),
        "pinus_halepensis": choice(specie),
        "juniperus_plumosa": choice(specie),
        "juniperus_oxycedrus": choice(specie),
        "ceratonia_siliqua": choice(specie),
        "chaualiop_limitis": choice(specie),
        "ranunculus_aqualitis": choice(specie),
        "acu_frentence": choice(specie),
        "sorbus_aria": choice(specie),
        "digitalis_obscura": choice(specie),
        "athamanta_vayredana": choice(specie),
        "centaurea_clementei": choice(specie),
        "campanula_mollis": choice(specie),
        "silene_andryalifolia": choice(specie),
        "sedum_dasphyllum": choice(specie),
        "chaenorrhinum_villosum": choice(specie),
        "rhamnus_myrtifolius": choice(specie),
        "teucrium_similatum": choice(specie),
        "cephalaria_leucantha": choice(specie),
        "helictotrichon_filifolium_arundanum": choice(specie),
        "thrincia_sp": choice(specie),
        "sanguisorba_minor": choice(specie),
        "scabiosa_turolensis_grosii": choice(specie)
    }

    conn.Flora.Flora.insert_one(item)
    print("Inserting item {i}/{ITEMS_COUNT}", end="\r")
