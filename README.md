# mutant
Test, isMutant

########################### NIVEL 1 ########################### 
Se desarrollo un script python donde permite al ejecutarlo ingresar por consola un string, interpreta ese string y devuelve, 
    true si es mutante, 
    false si no es mutante, o el string es incorrecto, para este ultimo punto se interpreto de esa manera ya que los requerimientos no especifican la respuesta para el caso de datos incorrectos.
    devuelve un mensaje. si no puede interpretar el ADN, es decir una cadena incorrecta.
    
archivo codigo fuente: mutant.py
    
########################### NIVEL 2 y 3 ########################### 
Teniendo en cuenta el script de python anterior se implemento una api REST en GOOGLE APP ENGINE, con flask, con tres metodos, los dos mencionados en el ejercicio y un tercer metodo de control de funcionamiento

https://testcolla.appspot.com/test
https://testcolla.appspot.com/mutant
https://testcolla.appspot.com/stats

A su vez se utilizo para el punto 3 una base de datos Mysql corriendo en GOOGLE SQL CLOUD, se adjunta el modelo de la misma (bd.sql)
Tambien se ralizo un script de python que genera a partir de un nro de pruebas ingrasado por consola y un N maximo, pruebas random de la api (test.py), este test, imprime en consola el ADN generado, y el codigo de estado de respuesta segun los requerimientos del programa. 

archivo codigo fuente api: main.py
