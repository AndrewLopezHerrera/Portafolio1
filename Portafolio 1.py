"""
Entradas: Un número entero mayor a uno (numero).
Salidas: Los números divisores de "numero".
Restricciones: numero debe de ser mayor a uno.
"""
def imprimedivisores (numero) :
    if isinstance(numero, int) :
        if numero > 0 :
            resultado = numero // 2
            print (numero)
            return imprimedivisoresaux (numero, resultado)
        else :
            print ('Error: el numero es menor o igual que cero')
    else :
        print ('Error: digite un numero entero positivo')

def imprimedivisoresaux (numero, resultado) :
    if resultado == 1 :
        return 1
    elif numero % resultado == 0 :
        print (resultado)
        return imprimedivisoresaux (numero, resultado - 1)
    else :
        return imprimedivisoresaux (numero, resultado - 1)

#=====================================================================================

"""
Entradas: Un número 'n' multiplicado por un numero 'm'.
Salidas: El producto de la multiplicación.
Restricciones: Solo se permiten numeros positivos.
"""
def multiplicacion (n, m) :
    if isinstance(n, int) and isinstance(m, int) :
        if n >= 0 :
            if m > -1 :
                if m == 0 :
                    return 0
                else:
                    return n + multiplicacion (n, m - 1)
            else:
                print('Error: m es menor que cero')
        else:
            print('Error: n es menor que cero')
    else:
        print('Error: digite numeros enteros positivos')

#=====================================================================================

"""
Entradas: Un número 'n' dividido por un numero 'm'.
Salidas: El cociente de la división.
Restricciones: Solo se permiten numeros positivos.
"""
def division (n, m) :
    if isinstance(n, int) and isinstance(m, int) :
        if n >= 0 :
            if m > 0 :
                if n >= m :
                    return divisionaux (n, m)
                else :
                    print('Error: n debe ser mayor o igual que m')
            else :
                print('Error: m debe ser mayor o igual a 1')
        else :
            print('Error: n debe ser mayor o igual a cero')
    else :
        print('Error: digite números enteros positivos')
def divisionaux (n, m) :
    if n == 0:
        return 0
    elif n < 0 :
        return -1
    else :
        return 1 + divisionaux (n - m, m)

#=====================================================================================

"""
Entradas: Un número positivo.
Salidas: Un número convertido a entero.
Restricciones: Debe ser un número mayor a cero, entero o flotante.
"""
def corrimientoAEntero(numero) :
    if numero > 0 :
        if numero % 2 == 1 :
            return numero
        elif numero % 2 == 0 :
            return numero
        else :
            return corrimientoAEntero(numero * 10)
    else :
        print('Error: El número es menor que 1')

#=====================================================================================

"""
Entradas: Un número positivo o negativo.
Salidas: La cuenta de dígitos de cualquier número.
Restricciones: Debe ser un número entero o flotante.
"""
def contarDigitosFlotantes(numero) :
    entero = corrimientoAEnteroAux(numero)
    return cuentadigitosaux(entero)

def corrimientoAEnteroAux(numero) :
    if numero % 2 == 1 :
        return numero
    elif numero % 2 == 0 :
        return numero
    else :
        return corrimientoAEntero(numero * 10)

def cuentadigitosaux(entero) :
    if entero == 0 :
        return 0
    else :
        return 1 + cuentadigitosaux(entero // 10)

#=====================================================================================

"""
Entradas: Un número entero mayor que 0 y un índice mayor o igual que 0.
Salidas: El número que seleccionó el indice.
Restricciones: Debe ser un número entero, el índice debe ser entero y debe ser igual o mayor que cero.
"""
def indiceNumero(numero, indice) :
    if isinstance(numero, int) :
        if isinstance(indice, int) :
            if numero > 0 :
                if indice >= 0 :
                    evaluando = numeroInversoAux(numero)
                    return indiceDelNumeroAux(evaluando, indice)
                else :
                    print('Error: Introduzca un índice mayor o igual que cero')
            else :
                print('Error: Introduzca un numero mayor o igual que cero')
        else :
            print('Error: Introduzca un índice como un número entero')
    else :
        print('Error: Introduzca un índice como un número entero')

def indiceDelNumeroAux(evaluando, indice):
    if indice == 0 :
        return evaluando % 10
    else:
        resultado = evaluando // 10 ** indice
        return resultado % 10
        
        

def numeroInversoAux(numero) :
    if isinstance (numero, int):
        if (numero == 0):
            return 0
        else :
            potencia = cuentadigito (numero) - 1
            return (numero % 10) * (10 ** potencia) + numeroInversoAux (numero // 10)
        
def cuentadigito (numero) :
    if numero == 0 :
        return 0
    else:
        return 1 + cuentadigito(numero // 10)

#=====================================================================================

"""
Entradas: Un número entero mayor que 0, un indice1 mayor o igual que cero y un indice2 mayor o igual que cero.
Salidas: Dos número, el primero selccionado por indice1 y el segundo seleccionado por indice2.
Restricciones: Los tres numeros deben ser enteros positivos, los indices iguales o mayores que cero y numero mayor que 0.
"""
def cortarNumero(numero, indice1, indice2) :
    if isinstance(numero, int) and isinstance(indice1, int) and isinstance(indice2, int):
        if numero > 0 :
            if indice1 >= 0 and indice2 >= 0 :
                evaluando = numeroInversoAux(numero)
                return print(indiceDelNumeroAux(evaluando, indice1) * 10 + indiceDelNumeroAux(evaluando, indice2))
            else :
                print('Error: Introduzca un índice mayor o igual que cero')
        else :
            print('Error: Introduzca un numero mayor o igual que cero')
    else :
        print('Error: Introduzca un numeros enteros')

def indiceDelNumeroAux(evaluando, indice):
    if indice == 0 :
        return evaluando % 10
    else:
        resultado = evaluando // 10 ** indice
        return resultado % 10

def numeroInversoAux(numero) :
    if isinstance (numero, int):
        if (numero == 0):
            return 0
        else :
            potencia = cuentadigito (numero) - 1
            return (numero % 10) * (10 ** potencia) + numeroInversoAux (numero // 10)
        
def cuentadigito (numero) :
    if numero == 0 :
        return 0
    else:
        return 1 + cuentadigito(numero // 10)
