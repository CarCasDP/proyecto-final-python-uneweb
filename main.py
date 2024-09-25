employees = []

def verify_str(x):
  employees[x]['first-name'] = input()
  if isinstance(employees[x]['first-name'], str):
    # print('El dato ingresado no es una cadena de texto, por favor intentelo nuevamente:')
    # verify_str(x)
    print(type(employees[x]['first-name']))
  else:
    print('gracias')

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
  # employees[x]['first-name'] = input()
  verify_str(x)

  print('Por favor ingrese el apellido del empleado ' + str(x + 1) + ':')
  employees[x]['last-name'] = input()

  print('Por favor ingrese el sueldo base del empleado ' + str(x + 1) + ':')
  employees[x]['base-salary'] = input()

  print('Por favor ingrese la fecha de ingreso del empleado ' + str(x + 1) + ':')
  employees[x]['entry-date'] = input()

  print('Por favor ingrese la cantidad de hijos del empleado ' + str(x + 1) + ':')
  employees[x]['number-of-children'] = input()

print(employees)
