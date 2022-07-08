from pymongo import MongoClient


#Para que nuestro sistema funcione en consola, debemos entrar a la carpeta que contiene nuestro archivo python, y ahi ejecutar el comanndo python nombrearchivo.py
def menu (): #declarando la función menú
    print ("Sistema de consultas de futbolistas") #imprimiento mensaje en pantalla
    while True: #asignando un ciclo while, que no se detendrá hasta que funcione el break
        print ("""
        1) Consulta General de futbolistas
        2) Consultar futbolista por pais
        3) Mostrar jugadores que cumplan con 2 condiciones (and)
        4) Mostrar jugadores que cumplan con al menos una condicion (or)
        5) Actualizar documento de futbolista
        6) Incrementar o decrementar Salario para todos los jugadores
        7) Modificar el dorsal, si el valor ingresado es superior al actual, se actualiza.
        8) Modificar o insertar un nuevo campo
        9) Insertar nuevo futbolista
        10) Borrar Futbolista
        11) Salir """) ##generando mediante print un menú interactivo, que tendrá 6 opciones

        opcion = input("Ingrese la opción a realizar: ") #asignando una variable, que será puesta por el usuario,  esto se hace mediante el "input"
        if opcion == '1': # Si el valor puesto por el usuario es un 1
            consultar_futbolistas() #llamando a la funcion consultar_futbolistas.



        elif opcion == '2':# Si el valor puesto por el usuario es un 2
            pais = input("Ingrese el país para filtrar: ")
            consultar_por_pais(pais)



        elif opcion == '3': # Si el valor puesto por el usuario es un 3
            pais = input ("Ingrese el país del jugador: ")
            equipo = input ("Ingrese el equipo del jugador a consultar: ")
            consultar_con_and (pais, equipo)



        elif opcion == '4': # Si el valor puesto por el usuario es un 4
            equipo = input("Ingrese el equipo del jugador a consultar: ")
            salario = int(input("Ingrese el salario del jugador a consultar: "))
            consultar_con_or (equipo, salario)



        elif opcion == '5':# Si el valor puesto por el usuario es un 5
            nombre = input("Ingrese el nombre del futbolista a actualizar: ")
            apellido = input ("Ingrese el nuevo apellido del futbolista a actualizar: ")
            pais = input("Ingrese el nuevo país del futbolista: ")
            dorsal = int(input("Ingrese el nuevo dorsal del jugador: "))
            equipo = input ("Ingrese el nuevo equipo del jugador: ")
            salario = int(input("Ingrese el nuevo salario del jugador: "))
            Frase = input ("Ingrese una nueva frase del jugador: ")
            datosActualizados = actualizarFutbolista (nombre, apellido, pais, dorsal, equipo, salario, Frase)
            print ("Datos actualizados: ", datosActualizados)



        elif opcion == '6': # Si el valor puesto por el usuario es un 6
            nuevoSalario = int(input("Ingrese cúanto desea aumentar o disminuir el salario de todos los jugadores, puede usar valores positivos o negativos: ")) #el valor ingresado debe ser un valor numerico
            datosActualizados = incrementarValor(nuevoSalario)
            print("Datos Actualizados: ", datosActualizados)



        elif opcion == '7':
            maxDorsal = int(input("Ingrese la nueva dorsal para todos los futbolistas, solo se actualiza si es superior a la actual: "))
            datosActualizados = aumentarDorsal(maxDorsal)
            print ("Datos actualizados: ",datosActualizados)




        elif opcion == '8': # Si el valor puesto por el usuario es un 7
            nombreCampo = input ("Ingrese el nombre del jugador cuyo documento desea ser modificado: ")
            nuevoCampo = input("Ingrese el campo que desea modificar u agregar: ")
            nuevoValor = input("Ingrese el valor del campo: ")
            datosActualizados = actualizarDocumento(nombreCampo, nuevoCampo, nuevoValor)
            print ("Datos actualizados: ", datosActualizados)



        elif opcion == '9':# Si el valor puesto por el usuario es un 8
            nombre = input("Ingrese el nombre del futbolista a insertar: ")
            apellido = input ("Ingrese el nuevo apellido del futbolista a actualizar: ")
            pais = input("Ingrese el nuevo país del futbolista: ")
            dorsal = int(input("Ingrese el nuevo dorsal del jugador: "))
            equipo = input ("Ingrese el nuevo equipo del jugador: ")
            salario = int(input("Ingrese el nuevo salario del jugador: "))
            campeonMundial = bool (input ("Ingrese si el futbolista fue campeon mundial, True si fue, False si no."))
            Frase = input ("Ingrese una nueva frase del jugador: ")
            futbolistaInsertado = insertarFutbolista(nombre, apellido, pais, dorsal, equipo, salario, campeonMundial, Frase)
            print ("Futbolistas insertados : ", futbolistaInsertado)

            

        elif opcion == '10':# Si el valor puesto por el usuario es un 9
            nombre = input ("Ingrese el nombre del futbolista a eliminar: ")
            registrosBorrados = borrarFutbolista(nombre)
            print ("Futbolistas eliminados: ", registrosBorrados)



        elif opcion == '11': # Si el valor puesto por el usuario es un 10
            print ("Hasta Luego!")
            break #ejecutará un break, luego de mostrar un mensaje que dice "Hasta Luego"



        else:
            print ("Opcion no válida, vuelve a intentarlo.")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES

def get_db (): #conexion a la base de datos.
    try: 
        client = MongoClient("mongodb://localhost:27017") #el argumento, indica nuestro usuario y nuestro puerto de mongodb
        db = client.deportistas
    except ConnectionError:
        print ("Error de conexión")
    
    return db



def consultar_futbolistas (): #Funcion para mostrar todos los documentos de nuestra coleccion a elegir.
    db = get_db() #conexión a la base de datos a través de la funcion definida anteriormente, get_db
    futbolistas = db.futbolistas.find({}, {"_id": 0}) # llamando a la función find, que nos permitirá visualizar el contenido de nuestra coleccion
    print ("{:*^105}".format('')) #asteriscos para la presentacion
    for futbolista in futbolistas:
        print(futbolista)



def consultar_por_pais (pais): #Funcion para mostrar todos los documentos de nuestra coleccion a elegir, filtrando por pais.
    db = get_db()
    futbolistas = db.futbolistas.find({"pais":{"$regex": pais, "$options":"i"}}, {"_id":0}) # llamando a la función find, que nos permitirá visualizar el contenido de nuestra coleccion (jugadores filtrados por pais, independiente de si esta en mayus o minus)
    print ("{:*^105}".format('')) #asteriscos para la presentacion
    for futbolista in futbolistas: #ciclo for, para visualizar todas nuestras respuestas.
        print (futbolista)
    return futbolistas



def consultar_con_and (pais, equipo): #funcion para evaluar dos condiciones true (con un and)
    db = get_db() #conexion a la base de datos
    futbolistas = db.futbolistas.find({"$and": [{"pais": {"$regex": pais, "$options":"i"}}, {"equipo": {"$regex": equipo, "$options":"i"}}]}) # funcion find, con un and, que evaluará si ambas condiciones son true para que muestre documento
    print ("{:10} {:10} {:10} {:5} {:20} {:5} {:20} {:50}".format("Nombre", "Apellido", "Pais", "N°", "Equipo","salario", "¿Campeón Mundial?", "Frase")) #cabecera del resultado, con un formato definido
    print ("{:*^105}".format('')) #asteriscos para la presentacion
    for futbolista in futbolistas: #ciclo for, para visualizar todas nuestras respuestas.
        print ("{:<10} {:<10} {:<10} {:<5} {:<20} {:,.0f} {:>5} {:>50}".format(futbolista["nombre"], futbolista["apellido"], futbolista["pais"], 
        futbolista["dorsal"], futbolista ["equipo"], futbolista["salario"], futbolista["campeonMundial"], futbolista["Frase"]))
    return futbolistas



def consultar_con_or (equipo, salario): #funcion que evaluará con un or
    db = get_db()
    futbolistas = db.futbolistas.find({"$or": [{"equipo": {"$regex": equipo, "$options":"i"}}, {"salario": {"$gte":salario}}]}) #codigo mongodb con el or
    print ("{:10} {:10} {:10} {:5} {:20} {:5} {:20} {:50}".format("Nombre", "Apellido", "Pais", "N°", "Equipo","salario", "¿Campeón Mundial?", "Frase")) #cabecera del resultado, con un formato definido
    print ("{:*^105}".format('')) #asteriscos para la presentacion
    for futbolista in futbolistas: #ciclo for, para visualizar todas nuestras respuestas.
        print ("{:<10} {:<10} {:<10} {:<5} {:<20} {:,.0f} {:>5} {:>50}".format(futbolista["nombre"], futbolista["apellido"], futbolista["pais"], 
        futbolista["dorsal"], futbolista ["equipo"], futbolista["salario"], futbolista["campeonMundial"], futbolista["Frase"]))
    return futbolistas



def actualizarFutbolista (nombre, apellido, pais, dorsal, equipo, salario, Frase): #funcion para actualizar un futbolista
    db = get_db()
    resultado = db.futbolistas.update_one( #codigo dentro de mongo para actualizar campos. 
        {"nombre": nombre}, #campo a actualizar (dependerá del nombre que insertemos)
        {
            '$set' : { #valores a ser reemplazados.
                "apellido": apellido,
                "pais": pais,
                "dorsal": int(dorsal), #int obliga a que el usuario ingrese valores numericos, de lo contrario lanza error el programa
                "equipo": equipo,
                "salario": int(salario),
                "Frase": Frase
            }
        })
    return resultado.modified_count #indica el numero de registros que fueron modificados



def actualizarDocumento (nombreCampo, nuevoCampo, nuevoValor): #funcion para agregar o actualizar un campo
    db = get_db()
    resultado = db.futbolistas.update_one( #actualiza solo un valor con update_one
        {"nombre": nombreCampo},
        {
            '$set' : {nuevoCampo:nuevoValor} #mediante $set podremos actualizar o generar un nuevo campo.
        }
    )
    return resultado.modified_count #devuelve la cantidad de campos actualizados



def incrementarValor (nuevoSalario): #funcion para aumentar o disminuir el salario
    db = get_db() 
    resultado = db.futbolistas.update_many( #el codigo puesto actualiza todos los documentos, esto se realiza mediante {}
        {},
        {
            "$inc":{"salario": nuevoSalario} #inc, incrementa o decrementa, dependiendo siel valor es positivo o negativo
        }
    )
    return resultado.modified_count #cuantos documentos han sido actualizados



def aumentarDorsal (maxDorsal): #Funcion para aumentar dorsal, solo si el valor ingresado es superior al actual
    db = get_db()
    resultado = db.futbolistas.update_many(
        {},
        {
            "$max": {"dorsal":maxDorsal}
        }
    )
    return resultado.modified_count #Cuantos documentos han sido actualizados



def borrarFutbolista (nombre): #funcion para borrar un futbolista
    db = get_db() #conexion a la base de datos mongo
    resultado = db.futbolistas.delete_one({"nombre": nombre}) #codigo dentro de mongo para eliminar un documento
    return resultado.deleted_count #indica el numero de registros que se borraron

    

def insertarFutbolista(nombre, apellido, pais, dorsal, equipo, salario, campeonMundial, Frase):
    db = get_db() #conexion a la base de datos mongo
    resultado = db.futbolistas.insert_one( #codigo dentreo de mongo para insertar un documento
        {"nombre": nombre, #valores campo valor a insertar.
        "apellido": apellido,
        "pais": pais,
        "dorsal": int(dorsal),
        "equipo": equipo,
        "salario": int(salario),
        "campeonMundial": campeonMundial,
        "Frase": Frase
        }
    )
    return resultado.inserted_id




## main 
menu() #llamando a nuestra función
