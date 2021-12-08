import os

os.chdir("/home/teamkk/Downloads/")
print("Nuevo directorio de trabajo: ",os.getcwd()) #Nuevo directorio de trabajo:  /home/teamkk/Downloads

print("ID proceso: ", os.getpid()) #ID proceso:  23284
print("ID usuario: ", os.getuid()) #ID usuario:  1000

# os.mkdir("NuevoDirectorio") #in working directory!!!

# os.rename("ejemplo.txt","nuevonombre.txt")