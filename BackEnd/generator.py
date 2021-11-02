from random import randint, random
from datetime import datetime
from pymongo import MongoClient
import random as rand

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

UTM = [
    "UF" + str(randint(1000, 3000))
]

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

inicio = datetime(1900, 1, 1)
fin = datetime(2021, 11, 1)
date_random = inicio + (fin-inicio) * rand.random()

ITEMS_COUNT = 300

for i in range(ITEMS_COUNT):
    item = {
        "num_register": randint(0, 1000),
        "date": date_random,
        "author": author,
        "location": location,
        "UTM": UTM,
        "lithology": lithology,
        "coverage": randint(0, 100),
        "altitude": randint(1000, 2000),
        "plot_slope": randint(0, 100),
        "altitude_veg": randint(0, 3000),
        "plot_area": randint(0, 3000),
        "plot_orientation": plot_orientation,
        "community": community,
        "abies_pinsapo": specie,
        "pinus_halepensis": specie,
        "juniperus_plumosa": specie,
        "juniperus_oxycedrus": specie,
        "ceratonia_siliqua": specie,
        "chaualiop_limitis": specie,
        "ranunculus_aqualitis": specie,
        "acu_frentence": specie,
        "sorbus_aria": specie,
        "digitalis_obscura": specie,
        "athamanta_vayredana": specie,
        "centaurea_clementei": specie,
        "campanula_mollis": specie,
        "silene_andryalifolia": specie,
        "sedum_dasphyllum": specie,
        "chaenorrhinum_villosum": specie,
        "rhamnus_myrtifolius": specie,
        "teucrium_similatum": specie,
        "cephalaria_leucantha": specie,
        "helictotrichon_filifolium_arundanum": specie,
        "thrincia_sp": specie,
        "sanguisorba_minor": specie,
        "scabiosa_turolensis_grosii": specie
    }

    conn.Flora.Data.insert_one(item)
    print("Inserting item {i}/{ITEMS_COUNT}", end="\r")
