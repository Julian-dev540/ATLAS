print("========ATLAS V0.1.0========") 

print("Bienvenido a ATLAS tu asistente virtual")

nombre=input("Cual es tu nombre:").capitalize()

print(f"Mucho gusto {nombre} bienvenido al programa")

print("Voy a recopilar tus datos para tenerlos en cuenta")

edad = int(input("Edad: " ))
if edad <= 17:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
        
    
ciudad = input ("Ciudad: ").upper()

altura = float(input ("Altura: "))

if altura <= 1.60:
    print("Si eres adolecente estas bajito, si eres menor estas bien")
else:
    print("Eres alto muy bien")     
   

print("Muy bien los datos del usuario son: ")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")
print(f"Altura: {altura}")


letras_nombre=len(nombre)
print(f"Tu nombre tiene {letras_nombre} letras")

   
print("Tienes algunos objetivos en mente")  
 
objetivo1 = input("Objetivo 1: ")
objetivo2 = input("Objetivo 2: ")
objetivo3 = input("Objetivo 3: ")

print(f"Cuanto tiempo estimas para tu primer objetivo: {objetivo1}")

tiempo1 = input(">")

print(f"En {tiempo1} lo vas a lograr")
print("Tus objetivos son muy importantes pero pasemos a tus cuentas")

ahorro_meta= int(input("Cual es tu meta de ahorro: "))
dinero_en_mano = int(input("Cuanto dinero tienes en este momento: "))
ganancias_mensuales = int(input("Cuanto ganas al mes: "))

dinero_faltante= ahorro_meta-dinero_en_mano

print(f"Te falta ${dinero_faltante} para llegar a la meta")

if ganancias_mensuales > 0:
   print("Muy bien vamos a hacer una cuenta")
elif ganancias_mensuales == 0 : 
    print("si ganas $0 mensual no llegaras a la meta")
else:
 print("si ganas numero negativo no llegaras a la meta")

if ganancias_mensuales > 0 :
 meses=dinero_faltante//ganancias_mensuales
 años=meses//12

if ganancias_mensuales > 0: 
  print(f"Para llegar a ${ahorro_meta} ganando ${ganancias_mensuales} mensual tardaras {meses} meses aproximadamente {años} años")
  
print("Que piensas sobre mi version 0.1.0")

opinion_usuario= input(">")

print("Ten en cuenta que si te lo propones lo puedes logras y esta es una prueba de eso")

print("Todo esto surgio de un simple print")

print("Esto es todo por ahora seguire trabajando en mi siguiente version")

print("=========Siguiente Version=======")

print("Version 0.1.1")

print("Estado: En desarrollo")

print("Escribe un numero para mas informacion o escribe una letra para salir del programa")

mas_info =input(">")

numero= mas_info.isnumeric()


if numero == True:
    print("Autor: Julian")
    print("Fecha de creacion: 2026-06-30")
    print("Programa finalizado")
else: 
      print("Programa finalizado")

    

    

