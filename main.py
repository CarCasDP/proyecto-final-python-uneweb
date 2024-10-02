from scripts import *

for x in range(0, 10):
  employees.append(
    {
      'first-name': '',
      'last-name': '',
      'base-salary': 0,
      'entry-date': '',
      'number-of-children': 0,
      'company': 0
    }
  )

  print('Por favor ingrese el nombre del empleado ' + str(x + 1) + ':')
  verify_str(x)

  print('Por favor ingrese el apellido del empleado ' + str(x + 1) + ':')
  verify_str(x)

  print('Por favor ingrese el sueldo base del empleado ' + str(x + 1) + ', colocandolo como un numero decimal de 2 cifras, especificando los números decimales con punto y no con coma:')
  verify_float(x)

  print('Por favor ingrese la fecha de ingreso del empleado ' + str(x + 1) + ', en el siguiente formato "yyyy-mm-dd":')
  verify_date(x)

  print('Por favor ingrese la cantidad de hijos del empleado ' + str(x + 1) + ':')
  verify_int(x)

  print('Por favor ingrese a qué empresa pertenece, ingrese 1 si pertenece a la primera empresa que cobra un 12% de base imponible o 2 si pertenece a la segunda empresa que cobra un 11.4% de base imponible de empleado ' + str(x + 1) + ':')
  verify_company(x)

  print('La base imponible del empleado ' + str(x + 1) + ' es: ' + str(calculate_tax_base(x)) + '. Además debe pagar ' + str(calculate_tax_health(x)) + ' en salud y ' + str(calculate_tax_SSO(x)) + ' en gastos a su afiliacion con la empresa ' + str(employees[x]['company']) + ' de SSO. En promedio, el empleado cobrara: ' + str(average_pay(x)))
