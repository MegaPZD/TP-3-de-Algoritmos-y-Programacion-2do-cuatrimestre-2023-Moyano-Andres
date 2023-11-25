import sys
import csv
import os
import biblioteca_mensajes as men

ARCHIVO_PEDIDOS = "pedidos.csv"
ARCHIVO_CLIENTES = "clientes.csv"
ARCHIVO_AUX = "soy_auxiliar.csv"
ID = 0
LISTAR_PARAMETRO_DEFECTO = 0
TOMATE = 'T'
ZANAHORIA = 'Z'
BROCOLI = 'B'
LECHUGA = 'L'
APPEND = 'a'
ESCRITURA = 'w'
LECTURA = 'r'
AGREGAR = 'agregar'
MODIFICAR = 'modificar'
ELIMINAR = 'eliminar'
LISTAR = 'listar'
LISTAR_TIPO = 1
LISTAR_CANTIDAD = 2
CONSOLA_NUMERO_VERDURAS = 2
DELIMITADOR_CSV = ';'
MODIFICAR_WRITER = 1
POSICION_OPERACION = 1
MODIFICAR_ID = 2
MODIFICAR_CANTIDAD = 3
MODIFICAR_TIPO = 4
CONSOLA_ID = 2
AGREGAR_CANTIDAD = 2
AGREGAR_TIPO = 3
AGREGAR_NOMBRE = 4
ERROR_SUPERIOR_LISTAR = 3
ERROR_SUPERIOR_AGREGAR = 5
ERROR_TOPE_ELIMINAR = 3
ERROR_SUPERIOR_MOSTRAR = 5

"""
pre: Requiere que el id sea mayor extricto que 0 y que el comando eliminar sea
ingresado correctamente (eliminar ID) (se asume que no hay restricción para
ingresar en la carpeta donde se almacenan los archivos requeridos para el TP3).

post: Devuelve verdadero si el id existe en el archivo de clientes.csv, sino es
así devolverá falso y se mostrará uno de dos mensajes de error: sí el id fue
eliminado o sí aun no esta creado.
"""
def id_eliminado(id: str) -> bool:

    exite_id = False
    ultimo_id_elemento = "0"

    try:
        archivo_clientes = open(ARCHIVO_CLIENTES, LECTURA)
    except:
        men.nunca_se_crearon_archivos()
        return
    
    reader = csv.reader(archivo_clientes, delimiter = DELIMITADOR_CSV)
    for elemento in reader:
        if(id == elemento[ID]):
            exite_id = True
        ultimo_id_elemento = elemento[ID]
    archivo_clientes.close()

    if(exite_id == False):
        men.mensaje_de_error_id(ultimo_id_elemento, id)

    return exite_id

"""
Post: Devuelve verdadero sí: tipo_verdura es 'T', 'Z', 'B' o 'L'. Sí no es uno 
de estos caracteres devolverá falso.
"""
def verificar_verdura_correcta(tipo_verdura: str) -> bool:
    verdura_correcta = False
    if tipo_verdura is TOMATE or tipo_verdura is ZANAHORIA or tipo_verdura is BROCOLI or tipo_verdura is LECHUGA:
        verdura_correcta = True
    return verdura_correcta

"""
Pre: Requiere que el comando agregar sea correctamente usado (agregar 
numero_verduras tipo_verdura nombre_persona) y que el numero de verduras sea
positivo.

Post: Agrega una linea a los archivos 'clientes,csv' y 'pedidos.csv' respetando
sus respectivos formatos. Sí estos no existen, los crea (se asume que no hay 
restricción para ingresar en la carpeta donde se almacenan los archivos 
requeridos para el TP3).
"""
def agregar(numero_verduras: str, tipo_verdura:str, nombre: str):
    
    ultima_linea = 0
    se_pudo_abrir_archivo_clientes = False
    se_pudo_abrir_archivo_pedidos = False
    
    try:
        archivo_clientes = open(ARCHIVO_CLIENTES, LECTURA)
        se_pudo_abrir_archivo_clientes = True
        
    except:
        men.no_existe_clientes_crear()
        archivo_clientes = open(ARCHIVO_CLIENTES, ESCRITURA) 
        archivo_clientes.close()
        ultima_linea = 1

    try:
        archivo_pedidos = open(ARCHIVO_PEDIDOS, LECTURA)
        se_pudo_abrir_archivo_pedidos = True

    except:
        men.no_existe_pedidos_crear()
        archivo_pedidos = open(ARCHIVO_PEDIDOS, ESCRITURA) 
        archivo_pedidos.close()

    if(se_pudo_abrir_archivo_clientes == True and se_pudo_abrir_archivo_pedidos == True):
        lector = csv.reader(archivo_clientes, delimiter= DELIMITADOR_CSV)
        for linea in lector:
            if(int(linea[ID]) > ultima_linea):
                ultima_linea = int(linea[ID])
        ultima_linea += 1
    
    archivo_clientes = open(ARCHIVO_CLIENTES, APPEND)
    archivo_clientes.write(str(ultima_linea) + DELIMITADOR_CSV + nombre + "\n")

    archivo_pedidos =  open(ARCHIVO_PEDIDOS, APPEND)
    archivo_pedidos.write(str(ultima_linea) + DELIMITADOR_CSV + tipo_verdura + DELIMITADOR_CSV + numero_verduras + "\n")

    archivo_pedidos.close()
    archivo_clientes.close()

"""
Pre: Requiere que el comando listar sea usado correctamente (listar ID o
listar), que el ID sea positivo y que exista. Si no existe el archivo 
'pedidos.csv' listar no se ejecutará (se asume que no hay restricción para
ingresar en la carpeta donde se almacenan los archivos requeridos para el TP3).

Post: Mostará por pantalla los pedidos de una o todas las ID, dependiendo de si
se ingreso listar o listar ID.
"""
def listar(a_listar: str = LISTAR_PARAMETRO_DEFECTO):

    try:
        archivo_pedidos = open(ARCHIVO_PEDIDOS, LECTURA)
    except:
        men.nunca_se_crearon_archivos()
        return
    
    reader = csv.reader(archivo_pedidos, delimiter = DELIMITADOR_CSV)

    if(a_listar == LISTAR_PARAMETRO_DEFECTO):
        men.listar_tabla()
        for lineas in reader:
            men.imprimir_listar(lineas[ID], lineas[LISTAR_TIPO], lineas[LISTAR_CANTIDAD])        
    else:
        men.listar_tabla()
        for lineas in reader:
            if(lineas[ID] == a_listar):
                    men.imprimir_listar(lineas[ID], lineas[LISTAR_TIPO], lineas[LISTAR_CANTIDAD])        

"""
Pre: Requiere que el comando eliminar sea usado correctamente (eliminar ID), 
que el ID sea positivo y que exista (se asume que no hay restricción para 
ingresar en la carpeta donde se almacenan los archivos requeridos para el TP3).

Post: Elimina uno o varios pedidos y su ID y cliente de 'pedidos.csv' y 
'clientes.csv' respectivamente.
"""
def eliminar(indice: str):

    try:
        clientes_modificar = open(ARCHIVO_CLIENTES, LECTURA)
    except:
        men.nunca_se_crearon_archivos()
        return
    try:
        archivo_aux = open(ARCHIVO_AUX, ESCRITURA)
    except:
        men.no_se_puede_crear_archivo_aux()
        clientes_modificar.close()
        return
    
    lector = csv.reader(clientes_modificar, delimiter= DELIMITADOR_CSV)
    escritor = csv.writer(archivo_aux, delimiter= DELIMITADOR_CSV)

    for linea in lector:
        if indice != linea[ID]:
            escritor.writerow(linea)

    clientes_modificar.close()
    archivo_aux.close()
    os.rename(ARCHIVO_AUX, ARCHIVO_CLIENTES)

    try:
        pedidos_modificar = open(ARCHIVO_PEDIDOS, LECTURA)    
    except:
        men.nunca_se_crearon_archivos()
        return
    try:
        archivo_aux = open(ARCHIVO_AUX, ESCRITURA)
    except:
        men.no_se_puede_crear_archivo_aux()
        pedidos_modificar.close()
        return

    lector = csv.reader(pedidos_modificar, delimiter= DELIMITADOR_CSV)
    escritor = csv.writer(archivo_aux, delimiter= DELIMITADOR_CSV)

    for linea in lector:
        if indice != linea[ID]:
            escritor.writerow(linea)

    pedidos_modificar.close()
    archivo_aux.close()
    os.rename(ARCHIVO_AUX, ARCHIVO_PEDIDOS)

"""
Pre: Requiere que el comando modificar sea usado correctamente (modificar ID
cantidad_verdura tipo_verdura), que el ID sea positivo y que exista y tambien el
tipo de verdura debe ser 'T', 'Z', 'B' o 'L' (se asume que no hay restricción para 
ingresar en la carpeta donde se almacenan los archivos requeridos para el TP3).

Post: Modifica el archivo agregando un nuevo pedido para determinado ID. Si el
pedido a modificar tiene el mismo tipo_verdura que uno existe, este ultimo se
sobreescribirá.
"""
def modificar(id: str, cantidar_verdura: str, tipo_verdura: str):

    modificado_correctamente = False
    se_encontro_id = False

    try:
        pedidos_modificar = open(ARCHIVO_PEDIDOS, LECTURA)
    except:
        men.nunca_se_crearon_archivos()
        return
    try:
        archivo_aux = open(ARCHIVO_AUX, ESCRITURA)
    except:
        men.no_se_puede_crear_archivo_aux()
        pedidos_modificar.close()
        return
    
    lector = csv.reader(pedidos_modificar, delimiter= DELIMITADOR_CSV)
    escritor = csv.writer(archivo_aux, delimiter= DELIMITADOR_CSV)

    for linea in lector:
        if id in linea[ID]:
            se_encontro_id = True
            if(tipo_verdura == linea[MODIFICAR_WRITER]):
                escritor.writerow([id, tipo_verdura, cantidar_verdura])
                modificado_correctamente = True
            else:
                escritor.writerow(linea)

        elif se_encontro_id == True and modificado_correctamente == False:
            escritor.writerow([id, tipo_verdura, cantidar_verdura])
            escritor.writerow(linea)
            modificado_correctamente = True
        else:
            escritor.writerow(linea)

    if(modificado_correctamente == False):
        escritor.writerow([id, tipo_verdura, cantidar_verdura])

    pedidos_modificar.close()
    archivo_aux.close()
    os.rename(ARCHIVO_AUX, ARCHIVO_PEDIDOS)

"""
Pre: Se asume que el usuario sabe que poner los parametros y en que orden 
ingresarlos para este comando, necesariamnete puede ingresar todos.

Post: Gestiona los parametros ingresados por el usuario para agregar, 
si este ingreso de forma incorrecta uno de sus parametros o hay faltante de estos se le hará
saber por consola, en cambio si los ingreso de forma correcta se posederá a realizar 
la acción correspondiente a este comando.
"""
def gestion_agregar(argv: list):
        #errores
        if(len(argv) < ERROR_SUPERIOR_AGREGAR or len(argv) > ERROR_SUPERIOR_AGREGAR):
            men.explicar_agregar()
            men.usted_ingreso(argv)
        elif ((argv)[CONSOLA_NUMERO_VERDURAS] < "0"):
            men.cantidad_negativa()
            men.usted_ingreso(argv)
        elif(verificar_verdura_correcta((argv)[AGREGAR_TIPO]) == False):
            men.explicar_agregar()
            men.verdura_incorrecta()
        #fin errores
        else:
            agregar((argv)[AGREGAR_CANTIDAD], (argv)[AGREGAR_TIPO], (argv)[AGREGAR_NOMBRE])
            men.correctamente_agregado()
   
"""
Pre: Se asume que el usuario sabe que poner los parametros y en que orden 
ingresarlos para este comando, necesariamnete puede ingresar todos.

Post: Gestiona los parametros ingresados por el usuario para modificar, 
si este ingreso de forma incorrecta uno de sus parametros o hay faltante de estos se le hará
saber por consola, en cambio si los ingreso de forma correcta se posederá a realizar 
la acción correspondiente a este comando.
"""
def gestion_modificar(argv: list):
    #errores
    if(len(argv) is not ERROR_SUPERIOR_MOSTRAR):
        men.explicar_modificar()
        men.usted_ingreso(argv)
    elif ((argv)[CONSOLA_ID] < "0"):
        men.id_negativo()
        men.usted_ingreso(argv)
    elif (id_eliminado((argv)[CONSOLA_ID]) == False):
        men.usted_ingreso(argv)
    elif(verificar_verdura_correcta((argv)[MODIFICAR_TIPO]) == False):
        men.explicar_modificar()
        men.verdura_incorrecta()
    #fin errores
    else:
        modificar((argv)[MODIFICAR_ID], (sys.argv)[MODIFICAR_CANTIDAD], (sys.argv)[MODIFICAR_TIPO])
        men.correctamente_modificado()

"""
Pre: Se asume que el usuario sabe que poner los parametros y en que orden 
ingresarlos para este comando, necesariamnete puede ingresar todos.

Post: Gestiona los parametros ingresados por el usuario para eliminar, 
si este ingreso de forma incorrecta uno de sus parametros o hay faltante de estos se le hará
saber por consola, en cambio si los ingreso de forma correcta se posederá a realizar 
la acción correspondiente a este comando.
"""
def gestion_eliminar(argv: list):
    #errores
    if len(argv) is not  ERROR_TOPE_ELIMINAR:
        men.error_eliminar_mal_ingresado()
    elif ((argv)[CONSOLA_ID] < "0"):
        men.id_negativo()
        men.usted_ingreso(argv)
    elif (id_eliminado((argv)[CONSOLA_ID]) == False):
        men.usted_ingreso(argv)
    #fin errores
    else:
        eliminar((sys.argv)[CONSOLA_ID])
        men.correctamente_eliminado()

"""
Pre: Se asume que el usuario sabe que poner los parametros y en que orden 
ingresarlos para este comando, necesariamnete puede ingresar todos.

Post: Gestiona los parametros ingresados por el usuario para listar, 
si este ingreso de forma incorrecta uno de sus parametros o hay faltante de estos se le hará
saber por consola, en cambio si los ingreso de forma correcta se posederá a realizar 
la acción correspondiente a este comando.
"""
def gestion_listar(argv: list):
    if(POSICION_OPERACION + 1 >= len(sys.argv)):
        listar()            
    #errores
    elif (len(argv) > ERROR_SUPERIOR_LISTAR):
        men.explicar_listar()
        men.usted_ingreso(argv)
    elif ((argv)[CONSOLA_ID] < "0"):
        men.id_negativo()
        men.usted_ingreso(argv)
    elif (id_eliminado((argv)[CONSOLA_ID]) == False):
        men.usted_ingreso(argv)
    #fin errores
    else:
        listar((argv)[CONSOLA_ID])

"""
Pre: Se asume que el argv recibido tiene por lo menos longitud de 2

Post: Gestiona que comando fue ingresado en consola, para cada comando
gestion_parametros_consola enviará los datos del argv a una función auxiliar.
"""
def gention_parametros_consola(argv: list):

    #agregar
    if (sys.argv)[POSICION_OPERACION] == AGREGAR:
        gestion_agregar(argv)
    
    #eliminar
    elif((argv)[POSICION_OPERACION] == ELIMINAR):
        gestion_eliminar(argv)

    #listar
    elif((argv)[POSICION_OPERACION] == LISTAR):
        gestion_listar(argv)

     #modificar   
    elif((sys.argv)[POSICION_OPERACION] == MODIFICAR):
        gestion_modificar(argv)
    else:
        men.no_se_ingreso_comando_correcto()