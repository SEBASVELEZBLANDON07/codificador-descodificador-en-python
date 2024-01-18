#remplazar con el mensaje codificado 
mensaje_codificado = "0050040500" 

#se separa el mensaje a descodificarpor medio de una lista 
list_decodificacion = list(mensaje_codificado) 

#lista de caracteres, debe ser la misma con la que se codifico el mensaje 
codigos = "sopqbaxyzABOPQR&*()-_|:;,.<>?ckl mnMNÑ0123456dfghiej+=[]{/\XYZW7'}`~º°¡¿CDEFGLJKTrtuvwS89!@#$%^ñHIUV"

#separamos los caracteres por medio de una lista 
list_caracteres = list(codigos)



#creamos un array donde se almacenara el mensaje descodificado 
array_descodificado = []

#se inicia un bucle for con el rango de el total de elementos en la lista, pasando de 2 en 2 
for i in range(0, len(list_decodificacion), 2):
   
    #unimos por parejas de 2 en 2 
    #es decir unimos el primer elemento con el segunto, el tercero con el cuarto y asi sucesivamente 
    n = list_decodificacion[i] + list_decodificacion[i + 1]
    
    #se pretende pasar la lista del mensaje codificado que se encuentra de la siguiente manerta
    #['0', '0', '5', '0', '0', '4', '0', '5', '0', '0']
    #[ 0    1    2    3    4    5    6    7    8    9]
    
    #a la siguente manera 
    #[00, 50, 04, 05, 00]
    #estas serian las posiciones de la lista list_caracteres 
    
    xn = int(n)
    #vamos agregando al array cada caracter segun en la posicion donde este en la lista de caracteres 
    array_descodificado.append(list_caracteres[xn])

#concatenamos el array, es decir unir los elementos del array en uno solo 
mensaje_descodificado = ''.join(map(str, array_descodificado))  
 
print(mensaje_descodificado)#mensaje_descodificado seria la variable donde se guarde el mensaje descodificado 

