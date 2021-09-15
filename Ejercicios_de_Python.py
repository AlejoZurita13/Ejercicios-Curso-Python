#Ejercicio de calculadora v 1.0.0
primero = input('Ingrese el primer numero: ')

try: 
    primero = int(primero)
except:
    primero = 'Incorrecto'

if primero == 'Incorrecto': 
    print('Ingresaste mal un dato, prueba de nuevo solo con numeros')
    exit()

segundo = input('Ingrese el segundo numero: ')

try: 
    segundo = int(segundo)
except:
    segundo = 'Incorrecto'

if segundo == 'Incorrecto':
    print('Ingresaste mal un dato, prueba de nuevo solo con numeros')
    exit()

simbolo = input('Ingrese operacion: ')
if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicacion: ', primero * segundo)
elif simbolo == '/':
    print('Divison: ', primero / segundo)
else:
    print('El simbolo ingresado no es valido')
#Prueba de commit 