import csv


def ObtenerDatos():
    cant = 0
    edadPorEquipo = {} # edadPorEquipo guarda por cada equipo la lista [cantidad de socios, suma de edades, edad maxima, edad minima]
    nombresRiver = {} # Guarda la cantidad de apariciones de cada nombre
    cienPrimeros = []

    with open('socios.csv') as file:
        for line in file:
            cant = cant + 1
            lineSeparada = line.split('\r')[0].split(';')
            equipo = lineSeparada[2]
            edad = int(lineSeparada[1])
            nombre = lineSeparada[0]
            listaEdad = edadPorEquipo.get(equipo, (0, 0, 0, 200)) # Si no existe la key devuelve la lista como inicializacion
            # Ver si el nuevo es maximo o minimo
            minimo = listaEdad[3]
            maximo = listaEdad[2]
            if edad < minimo:
                minimo = edad
            if edad > maximo:
                maximo = edad
            edadPorEquipo[equipo] = (listaEdad[0]+1, listaEdad[1]+edad, maximo, minimo)
            # Si es de River gaurdo la ocurrencia del nombre
            if equipo == 'River':
                cantOcurrencias = nombresRiver.get(nombre, 0)
                nombresRiver[nombre] = cantOcurrencias + 1
            # Buscar si esta casado y es universitario
            if lineSeparada[3] == 'Casado' and lineSeparada[4] == 'Universitario' and len(cienPrimeros) < 100:
                cienPrimeros.append((nombre, edad, equipo))
    return edadPorEquipo, nombresRiver, cienPrimeros, cant


def ProcesarDatos(porSocios, nombres, porEdad):
    # Buscar los 5 nombres
    nombresOrdenados = [('minimo', 0)] #agregoun minimo para asi agregar todos los nombres a la lista
    for nombre in nombres:
        cant = nombres[nombre]
        for i in range(len(nombresOrdenados)):
            if cant > nombresOrdenados[i][1]:
                nombresOrdenados.insert(i, (nombre, cant))
                break
    # Ordenar los equipos segun cantidad de socios
    equiposOrdenados = [('minimo', 0, 0, 0, 0)]
    for equipo in porSocios:
        socios = porSocios[equipo]
        promedioEdad = socios[1]/socios[0]
        if equipo == 'Racing': # Si es Racing me guardo el promedio
            promRacing = promedioEdad
        for i in range(len(equiposOrdenados)):
            if socios[0] > equiposOrdenados[i][1]:
                equiposOrdenados.insert(i, (equipo, socios[0], promedioEdad, socios[2], socios[3]))
                break
    # Ordenar la lista de 100
    cienOrdenados = [('maximo', 100, 'maximo')]
    for p in porEdad:
        edad = p[1]
        for i in range(len(cienOrdenados)):
            if edad < cienOrdenados[i][1]:
                cienOrdenados.insert(i, (p[0], edad, p[2]))
                break
    cienOrdenados = cienOrdenados[:len(porEdad)] # Saco el maximo
    with open('primeras100.txt', 'w') as file:
        for dato in cienOrdenados:
            file.write(dato[0]+' '+str(dato[1])+' '+dato[2]+'\n')
    return nombresOrdenados[:5], equiposOrdenados[:len(porSocios)], promRacing




datos = ObtenerDatos()
datosOrdenados = ProcesarDatos(datos[0], datos[1], datos[2])
# Mostrar la informacion
print 'La cantidad total de personas registradas es:', datos[3]
print '\n'
print 'El promedio de edad de los socios de Racing es de', datosOrdenados[2]
print '\n'
print 'El listado de las primeras 100 personas casadas y con estudios universitarios sale en el archivo llamado primeras100.txt'
print '\n'
print 'Los 5 nombres mas comunes de River son:'
for nom in datosOrdenados[0]:
    print(nom[0])
print '\n'
print 'El listado de equipos:'
print 'Equipo Prom Max Min'
for equipo in datosOrdenados[1]:
    print equipo[0], equipo[2], equipo[3], equipo[4]