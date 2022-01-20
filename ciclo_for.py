nume = int(input('Ingrese numero: ')) 
for i in range(nume, -1, -2):  # Este rango garantiza la cuenta hacia atras de 2 en 2
    print(i, end=', ')  # end permite que en vez de imprimir vertical lo haga horizontal separado por comas
    print()
