import csv


def ObtenerDatos():
    cant = 0
    edadPorEquipo = {} # edadPorEquipo guarda por cada equipo la lista [cantidad de socios, suma de edades, edad maxima, edad minima]
    nombresRiver = {} # guarda la cantidad de apariciones de cada nombre
    cienPrimeros = []

    with open('socios.csv') as file:
        for line in file:
            cant = cant + 1
            lineSeparada = line.split('\r')[0].split(';')
            equipo = lineSeparada[2]
            edad = int(lineSeparada[1])
            nombre = lineSeparada[0]
            listaEdad = edadPorEquipo.get(equipo, [0, 0, 0, 200]) # Si no existe la key devuelve la lista
            # Ver si el nuevo es maximo o minimo
            minimo = listaEdad[3]
            maximo = listaEdad[2]
            if edad < minimo:
                minimo = edad
            if edad > maximo:
                maximo = edad
            edadPorEquipo[equipo] = [listaEdad[0]+1, listaEdad[1]+edad, maximo, minimo]
            # Si es de River gaurdo la ocurrencia del nombre
            if equipo == 'River':
                cantOcurrencias = nombresRiver.get(nombre, 0)
                nombresRiver[nombre] = cantOcurrencias + 1
            # buscar si esta casado y es universitario
            if lineSeparada[3] == 'Casado' and lineSeparada[4] == 'Universitario' and len(cienPrimeros) < 100:
                cienPrimeros.append((nombre, edad, equipo))
    return edadPorEquipo, nombresRiver, cienPrimeros, cant


def ProcesarDatos(porSocios, nombres, porEdad):
    # Busco los 5 nombres
    nombresOrdenados = [('a', 0)]
    for nombre in nombres:
        cant = nombres[nombre]
        for i in range(len(nombresOrdenados)):
            if cant > nombresOrdenados[i][1]:
                nombresOrdenados.insert(i, (nombre, cant))
                break
    # 
    return nombresOrdenados[:5]




datos = ObtenerDatos()
datosOrdenados = ProcesarDatos(datos[0], datos[1], datos[2])
# Mostrar la informacion
print 'La cantidad total de personas registradas es:', datos[3]
print 'El promedio de edad de os socios de Racing es de', 999 # TODO
print 'El listado de las primeras 100 personas casadas y con estudios universitarios esta en el archivo llamado primeras100.txt' # TODO
print 'Los 5 nombres mas comunes de River son:' # TODO
for nom in datosOrdenados:
    print(nom)
print 'El listado de equipos:'
print 'Equipo   Prom   Max   Min' 
d = {'a': (0, 0, 0, 200)}
for equipo in d:
    edades = d[equipo]
    print equipo, edades[1], edades[2], edades[3]