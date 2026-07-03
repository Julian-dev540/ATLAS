
informacion_del_usuario = {
    "nombre": "julian",
    "edad": 16,
    "ciudad": "bogota",
    "genero": "masculino",
}

informacion_del_programa = {
    "nombre": "ATLAS",
    "version": "0.0.2",
    "autor": "Julian",
    "fecha_de_creacion": "2026-06-30",
}

lista_de_objetivos =["N250", "ATLAS", "Meta de dinero", "Meta de aprendizaje"]

tupla_del_programa = ("ATLAS", "Asistente virtual", "Julian", "2026-06-30")

conjunto_de_funciones_futuras = {"Saludar al usuario","Responder preguntas","Aprender de las interacciones"}

print("=======ATLAS V0.0.2=======")

print(f"Nombre del Asistente: {informacion_del_programa['nombre']}")
print(f"Versión: {informacion_del_programa['version']}")
print(f"Autor: {informacion_del_programa['autor']}")
print(f"Fecha de Creación: {informacion_del_programa['fecha_de_creacion']}")

print("=======Usuario=======")

print(f"Información del primer usuario")
print(f"Nombre: {informacion_del_usuario['nombre']}")
print(f"Edad : {informacion_del_usuario['edad']}")
print(f"Ciudad: {informacion_del_usuario['ciudad']}")
print(f"Género: {informacion_del_usuario['genero']}")

print("=======Objetivos=======")

print(f"Objetivo 1: {lista_de_objetivos[3]}")
print(f"Objetivo 2: {lista_de_objetivos[2]}")
print(f"Objetivo 3: {lista_de_objetivos[0]}")
print(f"Objetivo 4: {lista_de_objetivos[1]}")

print("=======Tupla del Programa=======")
print(f"Nombre: {tupla_del_programa[0]}")
print(f"Descripción: {tupla_del_programa[1]}")
print(f"Creador: {tupla_del_programa[2]}")
print(f"Fecha de Creación: {tupla_del_programa[3]}")

print("=======Funciones Futuras=======")

print(f"Función 1: {list(conjunto_de_funciones_futuras)[0]}")
print(f"Función 2: {list(conjunto_de_funciones_futuras)[1]}")
print(f"Función 3: {list(conjunto_de_funciones_futuras)[2]}")

print("=======Estado del Programa=======")
print("Estado: En desarrollo")
print("Siguiente versión: v0.1.0")

print("=======Condiciones del Usuario=======")

if informacion_del_usuario['nombre'] == "julian":
    print("bienvenido, julian.")
else:
    print("bienvenido, usuario no reconocido.")

if informacion_del_usuario['edad'] < 18:
    print("El usuario es menor de edad.")
else:
    print("El usuario es mayor de edad.")

if informacion_del_usuario['ciudad'] == "bogota":
    print("El usuario vive en Bogotá.")
else:
    print("El usuario no vive en Bogotá.")

print("=======Cuentas de usuario=======")

dinero_en_cuenta = 200000
dinero_a_ganar = 25000000
ganancias_mensuales = 200000
dinero_a_gastar = 50000

if dinero_en_cuenta > dinero_a_gastar:
    print("El usuario tiene buena margen de ahorro.")
elif dinero_en_cuenta < dinero_a_gastar:
    print("El usuario necesita ahorrar")  

print("=======Estado del usario y programa======") 

if informacion_del_usuario["edad"] >= 18 and dinero_en_cuenta >= 25000000:
   print("puedes comprar la N250")
else:
    print("Todavia no puedes comprar la N250")
    
if "Meta de aprendizaje" in lista_de_objetivos or "ATLAS" in lista_de_objetivos:
    print("El usuario esta en camino de aprendizaje")
else:
    print("El usuario no esta en programacion")
    
if not ("Saludar al usuario" or "Responder preguntas" or "Aprender de las interacciones" in conjunto_de_funciones_futuras):
    print("No van a ser funciones futuras")
else:
    print("son funciones futuras del programa")
    
print("=======Cuentas de la N250=======")

print(f"Dinero en la cuenta: ${dinero_en_cuenta}")
print(f"Meta de dinero: ${dinero_a_ganar}")
print(f"Gastos mensuales: ${dinero_a_gastar}")
print(f"Ganancias por mes: ${ganancias_mensuales}")

dinero_faltante_para_la_meta = dinero_a_ganar - dinero_en_cuenta 
gastos_en_un_año = dinero_a_gastar * 12 
dinero_en_2_años = ganancias_mensuales * 24 + dinero_en_cuenta

print(f"Dinero que Falta para la meta: ${dinero_faltante_para_la_meta}")
print(f"Gastos en un año: ${gastos_en_un_año}")
print(f"Dinero ganado en 2 años: ${dinero_en_2_años}")


    

    
