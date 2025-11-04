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

#RAMIRO:
# AGREGAR PAIS
def agregar_pais(paises):
    print("\n--- Agregar nuevo país ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    
    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie (km²): "))
    except ValueError:
        print("❌ La población y superficie deben ser números enteros.")
        return
    
    continente = input("Continente: ").strip()
    if not continente:
        print("❌ El continente no puede estar vacío.")
        return

    pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    paises.append(pais)
    guardar_paises(paises)
    print(f"✅ País {nombre} agregado correctamente.")
# BUSCAR PAIS
def buscar_pais(paises):
    termino = input("Ingrese el nombre del país a buscar: ").strip().lower()
    resultados = [p for p in paises if termino in p["nombre"].lower()]
    
    if resultados:
        print("\n--- Resultados ---")
        mostrar_lista(resultados)
        return resultados
    else:
        print("❌ No se encontraron países con ese nombre.")
        return []
# ACTULIZAR PAIS   
def actualizar_pais(paises):
    resultados = buscar_pais(paises)
    if not resultados:
        return

    if len(resultados) > 1:
        print("⚠ Se encontraron varios países. Especifique el nombre exacto.")
        return

    pais = resultados[0]
    try:
        nueva_poblacion = int(input("Nueva población: "))
        nueva_superficie = int(input("Nueva superficie (km²): "))
        pais["poblacion"] = nueva_poblacion
        pais["superficie"] = nueva_superficie
        guardar_paises(paises)
        print("✅ Datos actualizados correctamente.")
    except ValueError:
        print("❌ Debe ingresar números válidos.")
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

