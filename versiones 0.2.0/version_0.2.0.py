print("========ATLAS=========")
print("Bienvenido a ATLAS")
print("Versión 0.2.0")
salir = False
while salir == False:
   print("======Menu De ATLAS========")
   print("1. Registro De usuario")
   print("2. Información Del Programa")
   print("3. Información Del Usuario")
   print("4. Calculadora")
   print("5. Cuentas Del Usuario")
   print("6. Salir") 
   opcion = int(input("Elige Una Opción: "))
   if opcion == 1:
       print("=========Registro De Usuario========")
       nombre = input("Escribe tu nombre: ").capitalize()
       print(f"Bienvenido {nombre} a tu asistente virtual")
       edad = int(input("Edad: "))
       ciudad = input("Ciudad: ").upper()
       correo = input("Correo: ")
       contraseña = input("Contraseña: ")
       datos = {
           "Nombre": nombre,
           "Edad": edad,
           "ciudad": ciudad,
           "correo": correo,
           "contraseña" : contraseña,
       }
       print("======Registro Exitoso========")
       print("======Datos======")
       for dato in datos.items():
           valor = dato[1]
           print(valor)
   elif opcion == 2:
       print("=======Información De ATLAS=======")
       print("Versión: 0.2.0")
       print("Estado: En desarrollo")
       print("Fecha De Creación: 26/06/30")
       print("Creador: Julián Martínez")
       print("Nombre Del Programa: ATLAS")
       print("Siguente Versión: 0.2.1")
       print("=======Funciones=======")
       funciones = ("Registrar Al Usuario","Calculadora","Saludar Al Usuario","Llevar Cuentas")
       for funcion in funciones:
           print(funcion)
   elif opcion == 3:
       print("======Información Del Usuario=======")
       print("Dime Tus metas y objetivos")
       num_obj = int(input("Escribe cuantos objetivos tienes: "))
       objetivos = list()
       for obj in range(num_obj):
           objs = input("Escribe tus objetivos: ")
           objetivos.append(objs)
       print("Tus objetivos: ") 
       for obj in objetivos:
           print(obj)
   elif opcion == 4:
       salir_de_calculadora = False
       while salir_de_calculadora == False:
           print("=====OPERACIONES=====")
           print("1. Suma")
           print("2. Resta")
           print("3. División")
           print("4. Multiplicación")
           print("5. Potencia")
           print("6. Salir de la calculadora")
           opcion_cal = int(input("Escribe la opción: "))
           if opcion_cal == 1 :
               print("======SUMA======")
               Num_1 = int(input("Primer Número: "))
               Num_2 = int(input("Segundo Número: "))
               resultado = Num_1 + Num_2
               print(f"Resultado: {resultado}")
           elif opcion_cal == 2 :
              print("======Resta======")
              Num_1 = int(input("Primer Número: "))
              Num_2 = int(input("Segundo Número: "))
              resultado = Num_1 - Num_2
              print(f"Resultado: {resultado}")
           elif opcion_cal == 3 :
              print("======División======")
              Num_1 = int(input("Primer Número: "))
              Num_2 = int(input("Segundo Número: "))
              if Num_2 == 0:
                  print("Error")
              else:
                  resultado = Num_1 / Num_2
                  print(f"Resultado: {resultado}")
           elif opcion_cal == 4 :
                print("======Multiplicación======")
                Num_1 = int(input("Primer Número: "))
                Num_2 = int(input("Segundo Número: "))
                resultado = Num_1 * Num_2
                print(f"Resultado: {resultado}")
           elif opcion_cal == 5 :
                          print("======Potencia======")
                          Num_1 = int(input("Primer Número: "))
                          Num_2 = int(input("Segundo Número: "))
                          resultado = Num_1 ** Num_2
                          print(f"Resultado: {resultado}")
           elif opcion_cal == 6:
               salir_de_calculadora = True
   elif opcion == 5:
       salir_cuentas = False
       while salir_cuentas == False: 
           print("1. Hacer Cuentas")  
           print("2. salir")
           opcion_cuentas = int(input("Elige la opción: "))
           if opcion_cuentas == 1:
              print("=====Lleva Las Cuentas De Tu Dinero========")
              ahorros = int(input("Cuantos ahorros tienes: "))
              meta = int(input("Cual es tu meta de ahorro: "))
              ganancia_mensual = int(input("Cuanto ganas al mes: "))
              if ganancia_mensual== 0:
                  print("ERROR")
              else:
                  print("======Tus cuentas=====")
                  print(f"En este momento tienes: ${ahorros}")
                  print(f"Quieres llegar a: ${meta}")
                  print(f"Al mes ganas: ${ganancia_mensual}")
                  cuenta = meta - ahorros
                  meses = meta / ganancia_mensual
                  if meses < 12: 
                      print(f"con tus ahorros y ganando ${ganancia_mensual} al mes, ganaras ${meta} en {meses} meses")
                  elif meses > 12: 
                      años = meses / 12
                      print(f"con tus ahorros y ganando ${ganancia_mensual} al mes, ganaras ${meta} en {años} años")
           elif opcion_cuentas == 2:
              salir_cuentas = True    
   elif opcion == 6: 
       print("CERRANDO PROGRAMA....")
       salir = True            
              
               
            
             
             
        
           
           
             
        
           
           
        
            
        
        
       
        
       
                                  
           
       
           
       
       