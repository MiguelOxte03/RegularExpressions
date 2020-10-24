import re

opcion = 0
while opcion != 11:

    print("\nSelecion un Opcion")
    print("1.-Todas las que tengan una longitud de 7 o mas")
    print("2.-Expresiones que NO finalicen con una vocal")
    print("3.-Las palabras que inicien con 'M'donde la segunda letra no sea vocal")
    print("4.-Expresiones encerradas entre comillas")
    print("5.-Ip's")
    print("6.-Horas")
    print("7.-Telefonos")
    print("8.-Correos electrinicos")
    print("9.-Url's")
    print("10.-Codigos postales")
    print("11.-PARA SALIR")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]{7,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 2:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = "[A-Za-z]+[^aeiou]$"
            for elemento in lista:
                if re.search(regex, elemento):
                    print(elemento)
        textfile.close()
    elif opcion == 3:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "[M][^aeiou]\w{0,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 4:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = '(?:".*?")'
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 5:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 6:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "\d{1,2}\:\d{1,2}[aA|pP][m]"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 7:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "\d{3}\-\d{3}\-\d{4}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 8:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "[a-z0-9\.-_]+@[\w\d]+\.\w*"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 9:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 10:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "[cp|CP]?(\:\s?\d{5,5})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    else:
        print("GRACIAS POR HABER USADO EL PROGRAMA")