ARCHIVO_PEDIDOS = "pedidos.csv"
ARCHIVO_CLIENTES = "clientes.csv"

# mensajes que le indicaran al usuario si realizo la acción correctamente o no.

def error_eliminar_mal_ingresado():
    print("ERROR, para usar eliminar de debe ingresar:  eliminar ID")

def listar_tabla():
    print("TIPO\tCANTIDAD\tID\tNOMBRE")

"""
Recibe el ID, el tipo de verdura y la cantidad para imprimirlos
"""
def imprimir_listar(nombre: str, id_pedido: str, tipo_pedido: str, cant_pedido: str):
    print(f"{tipo_pedido}\t{cant_pedido}\t\t{id_pedido}\t{nombre}")

"""
Recibe el ultimo ID de 'clientes.csv' y lo comparará con el id ingresado.
Dado que ya se comprobo que el ID no existe esta comparación solo servirá para
imprimir uno de 2 mensajes: sí el ID aun no existe o sí se elimino.
"""
def mensaje_de_error_id(ultimo_id: str, id_ingresado: str):
    if(int(ultimo_id) > int(id_ingresado)):
        print("ERROR, el ID ingresado es de un elemento que se ha eliminado.")
    if (int(ultimo_id) < int(id_ingresado)):
        print("Error, el id ingresado es de un elemento aun inexistente, para crearlo utilice agregar.")

def no_existe_pedidos_crear():
    print(f"No se encuentra el archivo {ARCHIVO_PEDIDOS}, se procederá a crearlo.")

def no_existe_clientes_crear():
    print(f"No se encuentra el archivo {ARCHIVO_CLIENTES}, se procederá a crearlo.")

def nunca_se_crearon_archivos():
    print("No se encontro archivo, para crearlo utilice 'agregar'.")

def no_se_puede_crear_archivo_aux():
    print("No se puede crear un archivo nesesario para la ejecucion.")

"""
Recibe el argv para imprimirlo por pantalla.
"""
def usted_ingreso(argv: list):
    print(f"Usted ingreso: {argv}.")

def explicar_agregar():
    print(f"ERROR, para agregar correctamente.\nSe debe ingresar agregar numero_de_verduras tipo_verdura nombre_cliente.")

def explicar_listar():
    print("ERROR, para listar correctamente se debe ingresar listar ID o listar.")

def explicar_modificar():
    print("ERROR, para listar correctamente se debe ingresar modificar ID cantidad_verduras tipo_verduras.")

def id_negativo():
    print("ERROR, se ingreso un ID negativo.")

def cantidad_negativa():
    print("ERROR, se ingreso una cantidad de verduras negativa.")

def verdura_incorrecta():
    print("La verdura seleccionada es incorrecta")

def correctamente_agregado():
    print("Se agregó correctamente")

def correctamente_modificado():
    print("Se modificó correctamente")

def correctamente_eliminado():
    print("Se eliminó correctamente")

def no_se_ingreso_comando_correcto():
    print("ERROR, no se ingreso un comando correcto.\nPara realizarlo correctamente ingrese:\n'agregar'\n'listar'\n'modificar'\n'eliminar' ")