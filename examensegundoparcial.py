print("Vamos a ayudarte a gestionar tus tareas :)")
print("Por favor contesta lo que se te pide a continuacion: ")
print("Dia de la semana en la que te encuentras...")
dia=input()
print("Que hora del dia es?")
hora= int(input())
print("Tipo de tarea: Estudio, descanso, deportes o trabajo")
tarea=input()
if hora >1<=5:
  print("Debes estar dormido")
elif hora >5<14:
  print("Debes estar en clase")
elif hora >14<22:
  print("Puedes hacer tarea")
if hora >18<22 and tarea=="descanso":
  print("Ademas de tomar una siesta puedes realizar tus tareas")
if hora >18<22 and dia=="Sabado""Domingo":
  print("Puedes Ver una pelicula")
elif hora >14<20 and dia=="Lunes""Miercoles""Jueves":
  print("Puedes ir al gimnasio")
elif hora>13<15 and dia=="Martes""Jueves":
  print("Espero estes comiendo algo muy nutritivo")
