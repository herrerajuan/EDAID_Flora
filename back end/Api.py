from flask import Flask, render_template, redirect, request
from flask_pymongo import pymongo

client = pymongo.MongoClient("mongodb+srv://soledad03:coronavirusbdb@cluster0.epzrv.mongodb.net/test")
mongo_db = client.get_database('Flora')
mongo_col = pymongo.collection.Collection(mongo_db, 'Flora')

app = Flask(_name_)

@app.route('/')
def pagina_principal():
    return render_template("AplicaciónFlora.html")