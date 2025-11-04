archivo="paises.csv"

def inicializar_archivo():
    try:
        with open (archivo, "r", encoding="utf-8") as f:
            pass
        print("Archivo paises.csv encontrado")
    except FileNotFoundError:
        with open (archivo,"w", encoding="utf-8") as f:
            f.write("nombre,poblacion,superficie,continente\n")
        print("Archivo paises.csv creado correctamente")

def cargar_paises():

    paises=[]

    try:
        with open (archivo, "r", encoding="utf-8") as f:
            next(f)
            for linea in f:
                linea=linea.strip()
                if not linea:
                    continue
                partes=linea.strip(",")
                if len (partes) !=4:
                    print(f"Linea con formato incorrecto: {linea}")
                    continue
                nombre,poblacion,superficie,continente=partes

                try: 
                    pais={
                        "nombre":nombre,
                        "poblacion":int(poblacion),
                        "superficie":int(superficie),
                        "continente":continente
                    }
                    
                    paises.append(pais)
                except ValueError:
                    print(f"Error en los datos numericos de: {nombre}")
    except FileNotFoundError:
        print("Archivo no encontado, se creara uno nuevo al guardar")
    
    return paises 

def guardar_paises(paises):

    with open (archivo,"w", encoding="utf-8") as f:
        f.write("nombre,poblacion,superficie,continente,\n")
        for p in paises:
            linea= f"{p['nombre']},{p['poblacion']},{p['superficie']},{p['continente']}\n"
            f.write(linea)

#AYE:

# def agregar_paises
# def actualizar_pais
# def buscar_pais

def mostrar_lista(paises):
    
    for p in paises:
        print(f"{p['nombre']} - {p['poblacion']} hab - {p['superficie']} km² - {p['continente']}")

def obtener_nombre(p):
    return p["nombre"]

def obtener_poblacion(p):
    return p["poblacion"]

def obtener_superficie(p):
    return p["superficie"]

def ordenar_por_nombre(paises):
    paises.sort(key=obtener_nombre)
    mostrar_lista(paises)


def ordenar_por_poblacion(paises):
    paises.sort(key=obtener_poblacion)
    mostrar_lista(paises)


def ordenar_por_superficie(paises, descendente=False):
    paises.sort(key=obtener_superficie, reverse=descendente)
    mostrar_lista(paises)

#AYE:
# def mostrar_estadisticas

#LUCIA 
# def menu

#AYE llamada de funciones en bucle while

#######finalizado#########

