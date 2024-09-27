from decimal import Decimal, InvalidOperation

def is_decimal(s):
    try:
        Decimal(s)
        return True
    except InvalidOperation:
        return False

employees = []

def verify_str(x):
  employees[x]['first-name'] = input()
  if not(employees[x]['first-name'].isalpha()):
    print('El dato ingresado no es una cadena de texto, por favor intentelo nuevamente:')
    verify_str(x)

def verify_float(x):
  employees[x]['base-salary'] = input()
  if not(is_decimal(employees[x]['base-salary'])):
    print('El dato ingresado no es un numero decimal, por favor intentelo nuevamente:')
    verify_float(x)
  employees[x]['base-salary'] = float(employees[x]['base-salary'])
  employees[x]['base-salary'] = "{:.2f}".format(employees[x]['base-salary'])

for x in range(0, 10):
  employees.append(
    {
      'first-name': '',
      'last-name': '',
      'base-salary': 0,
      'entry-date': '',
      'number-of-children': 0
    }
  )

  print('Por favor ingrese el nombre del empleado ' + str(x + 1) + ':')
  verify_str(x)

  print('Por favor ingrese el apellido del empleado ' + str(x + 1) + ':')
  verify_str(x)

  print('Por favor ingrese el sueldo base del empleado ' + str(x + 1) + ', colocandolo como un numero decimal de 2 cifras, especificando los números decimales con punto y no con coma:')
  verify_float(x)

  print('Por favor ingrese la fecha de ingreso del empleado ' + str(x + 1) + ':')
  employees[x]['entry-date'] = input()

  print('Por favor ingrese la cantidad de hijos del empleado ' + str(x + 1) + ':')
  employees[x]['number-of-children'] = input()

print(employees)
