#ingresamos el mensaje a codificar 
mensaje = input("Ingresa mensaje a codificar: ")

#craemos una lista para el mensaje que se decea codificar
#ejemplo se desea codificar google en la lista quedaria asi
# g, o, o, g, l, e
# 0, 1, 2, 3, 4, 5
list_mensaje = list(mensaje)

#caracteres en desorden, la lista de caracteres no supere las 99 caracteres 
#debe tener un espacio en la lista de caracteres 
codigos = "sopqbaxyzABOPQR&*()-_|:;,.<>?ckl mnMNÑ0123456dfghiej+=[]{/XYZW7'}`~º°¡¿CDEFGLJKTrtuvwS89!@#$%^ñHIUV"

#se enlistan los caracteres en una lista dandoles una pocion numerica a cada caracter
list_caracteres = list(codigos)

#se crea un array para guardar el mensaje codificado 
array_mensajecodificado = []

contador = 0

#funcion para codificar el mesaje que se quiere codificar 
for i in range(len(list_mensaje)): #recorre la list_mensaje 
    for a in range(len(list_caracteres)):#recorre la list_caracteres
        
        #se compara el caracter de la list_mensaje con la lista list_caracteres
        if  list_mensaje[i] ==  list_caracteres[a]: 
            
            #si el numero de la pociion de la list_caracteres esta en el rango de 0 a 9 se le agrega un 0 a la izquierda  
            if 0 <= a <= 9:
                n = str(a).zfill(2)#sele agrega un 0 ala izquierda 
                contador = contador + 1 
                array_mensajecodificado.append(n)        
            else:
                contador = contador + 1
                array_mensajecodificado.append(a)    

#se compara si el contador es el misma cantidad que la cantidad de los caracteres de el mensaje a codificar 
#se hace esta comparacion para verificar que el mensaje que a codificar no tenga caractes que no esten en el listado de caracteres 
if contador == len(list_mensaje):
    
    print("mensaje valido ")

    #se concatenan o se une un array en una sola cadena 
    user_codificado = ''.join(map(str, array_mensajecodificado))   

    print("su mensaje codificado es: ")
    print(user_codificado)#user_codificado en esta variable se guarda el mensaje codificado  

else:
    #el mensaje no es valido cuando tiene un caracter que no se encuentra en el listado de caracteres
    print("usuario no valido") 
    
    
    

    
