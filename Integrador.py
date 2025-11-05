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

def agregar_pais(paises):
    print("\n--- Agregar nuevo país ---")
    nombre = input("Nombre: ").strip()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie (km²): ").strip()
    continente = input("Continente: ").strip()

    if nombre == "" or poblacion == "" or superficie == "" or continente == "":
        print("Error: no se permiten campos vacíos.")
        return

    if poblacion.isdigit() and superficie.isdigit():
        pais = {
            "nombre": nombre,
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente
        }
        paises.append(pais)
        guardar_paises(paises)
        print("País agregado correctamente.")
    else:
        print("Error: la población y la superficie deben ser números enteros.")
def buscar_pais(paises):
    print("\n--- Buscar país ---")
    texto = input("Ingrese el nombre del país a buscar: ").lower().strip()
    encontrados = []

    for p in paises:
        if texto in p["nombre"].lower():
            encontrados.append(p)

    if len(encontrados) == 0:
        print("No se encontraron países con ese nombre.")
    else:
        print("\nResultados encontrados:")
        for pais in encontrados:
            print(pais["nombre"], "-", pais["poblacion"], "hab -", pais["superficie"], "km² -", pais["continente"])
    
    return encontrados

def actualizar_pais(paises):
    print("\n--- Actualizar datos de un país ---")
    resultados = buscar_pais(paises)

    if len(resultados) == 1:
        pais = resultados[0]
        nueva_poblacion = input("Nueva población (dejar vacío si no desea cambiar): ").strip()
        nueva_superficie = input("Nueva superficie (km², dejar vacío si no desea cambiar): ").strip()

        if nueva_poblacion != "":
            if nueva_poblacion.isdigit():
                pais["poblacion"] = int(nueva_poblacion)
            else:
                print("Error: la población debe ser un número entero.")
                return

        if nueva_superficie != "":
            if nueva_superficie.isdigit():
                pais["superficie"] = int(nueva_superficie)
            else:
                print("Error: la superficie debe ser un número entero.")
                return
        guardar_paises(paises)
        print("Datos actualizados correctamente.")

    elif len(resultados) > 1:
        print("Se encontraron varios países, especifique el nombre exacto.")
    else:
        print("No se pudo actualizar porque no se encontró el país.")

def mostrar_estadisticas(paises):
    print("\n--- Estadísticas ---")

    if len(paises) == 0:
        print("No hay datos disponibles.")
        return

    pais_mayor = paises[0]
    pais_menor = paises[0]
    for p in paises:
        if p["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = p
        if p["poblacion"] < pais_menor["poblacion"]:
            pais_menor = p

    suma_poblacion = 0
    suma_superficie = 0
    for p in paises:
        suma_poblacion = suma_poblacion + p["poblacion"]
        suma_superficie = suma_superficie + p["superficie"]

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] = continentes[cont] + 1
        else:
            continentes[cont] = 1

    print("País con mayor población:", pais_mayor["nombre"], "(", pais_mayor["poblacion"], ")")
    print("País con menor población:", pais_menor["nombre"], "(", pais_menor["poblacion"], ")")
    print("Promedio de población:", round(promedio_poblacion, 0))
    print("Promedio de superficie:", round(promedio_superficie, 0))
    print("\nCantidad de países por continente:")
    for cont in continentes:
        print("-", cont + ":", continentes[cont])
def menu():
    paises = cargar_paises()

    while True:
        print("\nMENÚ ")
        print("1. Agregar país")
        print("2. Buscar país")
        print("3. Ordenar por nombre")
        print("4. Ordenar por población")
        print("5. Ordenar por superficie (descendente)")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregar_pais(paises)
            case "2":
                buscar_pais(paises)
            case "3":
                ordenar_por_nombre(paises)
            case "4":
                ordenar_por_poblacion(paises)
            case "5":
                ordenar_por_superficie(paises, descendente=True)
            case "6":
                mostrar_estadisticas(paises)
            case "7":
                print("Muchas gracias, hasta pronto.")
                break
            case _:
                print("Opción inválida.Intente nuevamente.")