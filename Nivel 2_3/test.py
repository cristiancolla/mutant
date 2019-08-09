import json
import requests
import random
import sys

URL = "https://testcolla.appspot.com/mutant"

try:
    cant = int(raw_input("Por favor ingrese candidad de pruebas "))
except:
    print("Ingrese un Numero")
    sys.exit()

try:    
    filas = int(raw_input("Por favor ingrese el N maximo: "))
except:
     print("Ingrese un Numero")
     sys.exit()

for h in range(cant):
    n = random.randint(1,filas)
    dna = []
    for x in range(n):
        sec =""
        for i in range(n):
            sec +=random.choice("ACTG")
        dna.append(sec)
    print ("------------------------------------------------------")    
    print("secuencia adn random")
    print(dna)    
         
    PARAMS = {'dna':dna}
    headers = {'content-type': 'application/json'}
        
    r = requests.post(URL, data=json.dumps(PARAMS), headers=headers)
       
    print("status code:" + str(r.status_code))
    
#[/root/.config/gcloud/application_default_credentials.json]
#ya29.GlteB7KLxEgY35hNwP4Qb6_KdrLX5EixGNEhDa7iHnWomXaB8ukSTTuTYatB0Jbx462W-dGHRTZXlMuwPKhAEMxlUwYzLL7WRoVzY9rW3j1YsRRqR1Oxe9C6Y5kY
#https://cloud.google.com/python/getting-started/using-cloud-sql
#connectionName: testcolla:southamerica-east1:mutant