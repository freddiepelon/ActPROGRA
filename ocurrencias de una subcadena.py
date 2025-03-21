#contador de ocurrencias de una subcadena
# count cuenta el número de ocurrencias donde una subcadena aparece en la cadena principal
a = input(f"ingresa un texto largo, muy largo, porfavor :(  : ")
c = a.lower() 
b = c.split()
for i in range(0, len(b), 1):
    d = b[i]
    ocurrencias = a.count(d)
    print(f"el número de ocurrencias de la subcadena {d} es:  {ocurrencias}")
# el número de ocurrencias de la subcadena hola es:  1
#el número de ocurrencias de la subcadena soooooooy es:  1
#el número de ocurrencias de la subcadena soooooy es:  1
#el número de ocurrencias de la subcadena soy es:  1
#el número de ocurrencias de la subcadena un es:  1
#el número de ocurrencias de la subcadena cacahuate es:  1
    
    



