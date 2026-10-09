nombre_mascotas=[""]*3
edad_mascotas=[""]*3

def insertar():
    for i in range((nombre_mascotas)):
        nombre_mascotas[i]=input(f"ingrese nombre de mascota:")
        edad_mascotas[i]=input(f"Ingrese edad mascota:")
def mostrar(): 
    for i in range(len(nombre_mascotas)):
        print(f"nombre: {nombre_mascotas[i]} , edad: {edad_mascotas}")          
def eliminar():

def main():
    global nombre_mascotas, edad_mascotas

    nombre_mascotas=[""]*3
    edad_mascotas=[""]*3

    opcion=0
    while opcion !=4:
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] mostrar mascota (nombre | edad)")
        print("[3] Eliminar mascotas (nombre | edad)")
        print("[4] Salir" )
        if opcion==1:
            print("Insertar")
        elif opcion==2:
            print("Mostrar")
        elif opcion==3:
            print("Eliminar")
        elif opcion==4:
            print("Saliendo.....")
        else: print ("opcion invalida")
        if opcion !=4: input("Presiona para continuar..")
main()