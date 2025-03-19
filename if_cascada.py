'''if en cascada:
    estructura selectiva 
    compuesta por multiples
    condicionales, seguidos 
    unos de otros
    Sintaxis:
    if condicional1:
    iinstruccion1
    instruccion2
    if condicional2:
        instruccion1
        instruccion2
    elif condicional2:
        instruccion3
        instruccion4
    elif condicional3:
    instruccion5
    instruccion6
    '''
    
#ejemplo:
#vamos a hacer un pequeño
#traductor
#el programa debe permitir
#leer fruta en español
#y debe mostrar esa fruta
#en ingles

fruta_es = input("ingrese fruta")
if fruta_es == "manzana" or fruta_es=="manzana":
    print ("apple")
elif fruta_es == "naranja" or fruta_es=="naranja":
    print ("orange")
elif fruta_es == "uva" or fruta_es=="uva":
    print ("grape")
elif fruta_es == "piña" or fruta_es=="piña":
    print ("pineapple")

#caso por defecto