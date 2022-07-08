import pprint #este fichero muestra de forma mas formateada los print
from pymongo import MongoClient

client = MongoClient ("localhost", 27017) #Asignando a la variable client nuestro nobmre de usuario y puerto para la conexión a nuestra bd

db = client.deportistas #conexion a la base de datos
futbolistas = db.futbolistas.find_one() #muestra el primer documento insertado en la coleccion futbolistas de nuestra bd


#futbolistas= db.futbolistas
#pprint.pprint(futbolistas.find_one({"pais":"Chile"})) #printeando nuestro resultado en formato json

futbolistas = db.futbolistas.find({"pais": "Francia"}, {"_id":0 }) #creando consulta para mostrar todos los futbolistas de francia, sin mostrar el campo _id
for futbolista in futbolistas: #con el ciclo for, nos permite visualizar en pantalla ols resultados.
    pprint.pprint(futbolista)