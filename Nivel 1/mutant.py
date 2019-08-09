import logging
import json
import os
import re

from logging.handlers import RotatingFileHandler

#SETUP LOG
LOGFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"log.log")
LOGLEVEL = logging.INFO
LOGFORMAT='%(asctime)s %(levelname)s [%(name)s] %(message)s'

logger = logging.getLogger(LOGFILE)
logger.setLevel(LOGLEVEL)

handler = RotatingFileHandler(LOGFILE, maxBytes=20*1024,backupCount=3)
formatter = logging.Formatter(LOGFORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("------------------------------")
logger.info('log ok') 
               
               
class Mutant:
    def __init__(self):
        self.INPUT_DATA_ERROR_MSG = "input data is not correct "
        self.DATA_SEARCH_MSG = "found sequence "
        REGEX_DATA_CHECK = "^([ATGC]*)$"
        REGEX_SEC_CHECK = '([ATGC])\\1{3}'
        
        self.validate_data = re.compile(REGEX_DATA_CHECK)
        self.validate_sec = re.compile(REGEX_SEC_CHECK)
        
        logger.info("init ok")
        
        DNA = raw_input("Por favor ingrese ADN: ")
        try:
            matrix = json.loads(DNA)
            print(self.isMutant(matrix))
        except:
            print("ADN incorrecto")
            
                
    def isMutant(self, matrix):
        rta = True
        try:
            #DATA INPUT CHECK
            #is array
            if type(matrix) in (tuple, list):
                for each in matrix:
                    #is nxn
                    if len(each) == len(matrix):
                        #is not A,T,G,C    
                        if not self.validate_data.search(each):
                            rta = False
                            logger.info(self.INPUT_DATA_ERROR_MSG)
                            break
                    else:
                        rta = False
                        logger.info(self.INPUT_DATA_ERROR_MSG)
                        break
            else:
                rta = False
                logger.info(self.INPUT_DATA_ERROR_MSG)
        
        
            #IF DATA INPUT IS CORRECT
            if rta:
                cant = self.__search(matrix) + self.__search(self.__vertical(matrix)) + self.__search(self.__oblique(matrix)) + self.__search(self.__oblique(self.__rotate(matrix)))    
                if cant <= 1:
                    rta = False
            
            return rta
        except Exception, e:
            logger.error(str(e))
            
    
    #generate the strings of the columns
    def __vertical(self, matrix):
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
    def __oblique(self, matrix):
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
    def __rotate(self, matrix):
        m = []
        for each in matrix:
            m.append(each[::-1])
        return m
     
    #search secuences.
    def __search(self, matrix):
        cant = 0
        for each in matrix:
            if self.validate_sec.search(each):
                cant +=1
                logger.info(self.DATA_SEARCH_MSG + each)
        return cant
        
        
if __name__ == '__main__':
    Mutant()  