contador=0
miemail=input("Introduce tu direccion de email: ")

for i in miemail:
    if (i=="@"or i=="."):
        contador=contador+1

if contador >= 2:
    print("Correcto")
else:
    print("incorrecto")


for j in range(5):
    print(j)
