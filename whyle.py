i=1
contador=0

while i<=10:
    print("Ejecucion" + str(i))
    i=i+1


print("Termino la ejecucion")

edad=int(input("Introduce tu edad: "))

while edad<0:
    print("La edad es incorrecta")
    edad=int(input("Introduce tu edad: "))

print ("gracias, edad correcta :D ")
print ("La edad del usuario es " + str(edad))
