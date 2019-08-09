from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

app = Flask(__name__)

import json
import os
import re
import sys

import pymysql

cnx = pymysql.connect(unix_socket='/cloudsql/testcolla:southamerica-east1:mutant', user='root', password='root', db='test')

@app.route('/test', methods=['GET'])
def test():
    return app.make_response(('api Test OK! ', 200))
        
@app.route('/stats', methods=['GET','POST']) 
def stats():
    try:
        sql_query = """
            SELECT SUM(isMutant = 1) AS mutant, SUM(isMutant = 0) AS human,
                (CASE WHEN SUM(isMutant = 0) > 0 
                 THEN SUM(isMutant = 1) / SUM(isMutant = 0)
                 ELSE 0
                END)
            FROM dna;
        """
        cur = cnx.cursor()
        cur.execute(sql_query)
        records = cur.fetchall()
        cur.close()
        rta = {"count_mutant_dna":str(records[0][0]),"count_human_dna":str(records[0][1]),"ratio":str(records[0][2])}
       
        return app.make_response((json.dumps(rta), 200))
    except Exception as e:
        return app.make_response((str(e), 500))
    
@app.route('/mutant', methods=['GET','POST'])
def isMutant():
    REGEX_DATA_CHECK = "^([ATGC]*)$"
    validate_data = re.compile(REGEX_DATA_CHECK)
    
    #DATA FORMAT CHECK
    try:
        matrix = request.json.get("dna")
        
    except:
        return app.make_response(('', 403)) 


    try:
        
        #DATA INPUT CHECK
        if type(matrix) in (tuple, list):
            for each in matrix:
                #is nxn
                if len(each) == len(matrix):
                    #is not A,T,G,C    
                    if not validate_data.search(each):
                        return app.make_response(('', 403))
                else:
                    return app.make_response(('', 403))
        else:
            return app.make_response(('', 403))
            
    
        #IF DATA INPUT IS CORRECT
        cant = __search(matrix) + __search(__vertical(matrix)) + __search(__oblique(matrix)) + __search(__oblique(__rotate(matrix)))    
        if cant <= 1:
            cur = cnx.cursor()
            cur.execute("INSERT INTO dna(dna,isMutant) VALUES ('"+json.dumps(matrix) +"',0)")
            cnx.commit()
            return app.make_response(('', 403))
        else:
            cur = cnx.cursor()
            cur.execute("INSERT INTO dna(dna,isMutant) VALUES ('"+json.dumps(matrix) +"',1)")
            cnx.commit()
            return app.make_response(('', 200))
       
        
    except Exception as e:
        print (str(e))
        return app.make_response((str(e), 500))
        

#generate the strings of the columns
def __vertical(matrix):
    m = []
    
    
    for each in matrix:
        index = 0
        for chart in each:
            try:
                m[index] += chart
            except:
                m.insert(index,chart)
            index +=1
    return m
    
#generate the strings of the left diagonal
def __oblique(matrix):
    cache = {}
    m = []
    
    y = 0
    key = ""
    for each in matrix:
        x = 0
        for chart in each:
            key = str(x-y) + str(y-y)
            if key in cache:
                cache[key] = cache[key] + chart
            else:
                cache[key] = chart
            x +=1
        y +=1    
    
    for each in cache:
        m.append(cache[each])
    
    return m

#generate inverted vertical array chains
def __rotate(matrix):
    m = []
    for each in matrix:
        m.append(each[::-1])
    return m
 
#search secuences.
def __search(matrix):
    REGEX_SEC_CHECK = '([ATGC])\\1{3}'
    validate_sec = re.compile(REGEX_SEC_CHECK)
        
    cant = 0
    for each in matrix:
        if validate_sec.search(each):
            cant +=1
    return cant


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
