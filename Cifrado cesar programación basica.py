#cifrado cesar
def cifrado_cesar (c,d):
    a = c.lower() #c = "HOLA   soy jamoncito -- hola   soy jamoncito 
    u = ''.join(a) # holasoyjamoncito
    lista = []
    
    
    
    
     
    alfabeto = "abcdfefghijklmnñopqrstuvwxyz"
     
    for q in range(0, len(u), 1):
        m = u[q]
        if m in alfabeto:
            
            remplazo = alfabeto.find(m)
            p = (remplazo + d) % len(alfabeto) 
            s = alfabeto[p]
            lista.append(s) 
        else: #si no se cumple
            lista.append(m) 
        
        
        #devuelve la posición (el número)
        

    
        
        
        
        
            # ¿ese elemento "m" de la cadena "u" en que posición de "alfabeto" esta?
        






        
        
        

    ''.join(lista)
    return(''.join(lista))  
    


c = input(f"ingresa una frase/cadena: ")
d = int(input("ingresa un número: "))
o = cifrado_cesar(c,d)
print(o)
