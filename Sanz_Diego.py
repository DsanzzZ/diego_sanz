from os import system
system("cls")
# import statisctic
# geometric_mean()
import random

sueldo0=random.randint(300000,2500000)
sueldo1=random.randint(300000,2500000)
sueldo2=random.randint(300000,2500000)
sueldo3=random.randint(300000,2500000)
sueldo4=random.randint(300000,2500000)
sueldo5=random.randint(300000,2500000)
sueldo6=random.randint(300000,2500000)
sueldo7=random.randint(300000,2500000)
sueldo8=random.randint(300000,2500000)
sueldo9=random.randint(300000,2500000)

sueldos=[sueldo0, sueldo1, sueldo2, sueldo3, sueldo4, sueldo5, sueldo6, sueldo7, sueldo8, sueldo9]

trabajadores=["juan perez","maria garcia","carlos lopez","ana martines","pedro rodriguez","laura hernandez","miguel sanchez","isabel gomez","francisco diaz","elena fernandez"]
menos800=[]
mas800=[]
dospalo=[]
#def´s
def asignar_sueldos():
    print(f"""
el trabajador {trabajadores[0]} tiene un sueldo de: ${sueldo0}
la trabajadora {trabajadores[1]} tiene un sueldo de: ${sueldo1}
el trabajador {trabajadores[2]} tiene un sueldo de: ${sueldo2}
la trabajadora {trabajadores[3]} tiene un sueldo de: ${sueldo3}
el trabajador {trabajadores[4]} tiene un sueldo de: ${sueldo4}
la trabajadora {trabajadores[5]} tiene un sueldo de: ${sueldo5}
el trabajador {trabajadores[6]} tiene un sueldo de: ${sueldo6}
la trabajadora {trabajadores[7]} tiene un sueldo de: ${sueldo7}
el trabajador {trabajadores[8]} tiene un sueldo de: ${sueldo8}
la trabajadora {trabajadores[9]} tiene un sueldo de: ${sueldo9}
""")
    input("precione enter para continuar...")
    from os import system
    system("cls")
def finalizar_programa():
    print("finalizando programa...")
    print("desarollado por Diego Sanz")
    print("RUT 21.515.937-k")

while True:
     print("""
 1.Asignar sueldos
 2.Clasificar sueldos
 3.Ver estadisticas
 4.Reporte de sueldos
 5.Salir
 """)
    
     op=input("seleccione una opcion: ")
     if op=="1":
          asignar_sueldos()

     



     elif op=="2":
            print("no logre hacer esto :/")
            # if sueldo0<800000:
            #     trabajadores[0] in menos800

            # elif sueldo1<800000:
            #     trabajadores[1] in menos800

            # elif sueldo2<800000:
            #     trabajadores[1] in menos800

            # elif sueldo3<800000:
            #     trabajadores[1] in menos800

            # elif sueldo4<800000:
            #     trabajadores[1] in menos800

            # elif sueldo5<800000:
            #     trabajadores[1] in menos800

            # elif sueldo6<800000:
            #     trabajadores[1] in menos800

            # elif sueldo7<800000:
            #     trabajadores[1] in menos800

            # elif sueldo8<800000:
            #     trabajadores[1] in menos800

            # elif sueldo9<800000:
            #     trabajadores[1] in menos800


            # elif sueldo0>=800000 and sueldo0<=2000000:
            #     mas800=[trabajadores[0]]

            # elif sueldo1>=800000 and sueldo1<=2000000:
            #     mas800=[trabajadores[1]]

            # elif sueldo2>=800000 and sueldo2<=2000000:
            #     mas800=[trabajadores[2]]

            # elif sueldo3>=800000 and sueldo3<=2000000:
            #     mas800=[trabajadores[3]]

            # elif sueldo4>=800000 and sueldo4<=2000000:
            #     mas800=[trabajadores[4]]

            # elif sueldo5>=800000 and sueldo5<=2000000:
            #     mas800=[trabajadores[5]]

            # elif sueldo6>=800000 and sueldo6<=2000000:
            #     mas800=[trabajadores[6]]

            # elif sueldo7>=800000 and sueldo7<=2000000:
            #     mas800=[trabajadores[7]]

            # elif sueldo8>=800000 and sueldo8<=2000000:
            #     mas800=[trabajadores[8]]

            # elif sueldo9>=800000 and sueldo9<=2000000:
            #     mas800=[trabajadores[9]]
                    
            # elif sueldo0>2000000:
            #     dospalo[trabajadores[0]]

            # elif sueldo1>2000000:
            #     dospalo[trabajadores[1]]

            # elif sueldo2>2000000:
            #     dospalo[trabajadores[2]]

            # elif sueldo3>2000000:
            #     dospalo[trabajadores[3]]

            # elif sueldo4>2000000:
            #     dospalo[trabajadores[4]]

            # elif sueldo5>2000000:
            #     trabajadores[5]=dospalo

            # elif sueldo6>2000000:
            #     dospalo[trabajadores[6]]

            # elif sueldo7>2000000:
            #     dospalo[trabajadores[7]]

            # elif sueldo8>2000000:
            #     dospalo[trabajadores[8]]

            # elif sueldo9>2000000:
            #     dospalo[trabajadores[9]]
            # print("SUELDOS MENORES A $800.000")
            # print(menos800)


            input("precione enter para continuar...")
            from os import system
            system("cls")
   
     elif op=="3":
         print(f"""
sueldo mas alto: """) 
         
          
     #elif op=="4":
         
          
     elif op=="5":
         finalizar_programa()
         break


