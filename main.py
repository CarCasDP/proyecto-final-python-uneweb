from decimal import Decimal, InvalidOperation
import datetime

def is_decimal(s):
    try:
        Decimal(s)
        return True
    except InvalidOperation:
        return False

def format_check(date, fmt):
    try: datetime.datetime.strptime(date, fmt)
    except: return False
    else: return True

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

def verify_date(x):
  employees[x]['entry-date'] = input()
  if not(format_check(employees[x]['entry-date'], '%Y-%m-%d')):
    print('El dato ingresado no posee el formato de fecha deseado "yyyy-mm-dd", por favor intentelo nuevamente:')
    verify_date(x)
  if (datetime.datetime.now().strftime("%Y-%m-%d") < employees[x]['entry-date']):
    print('La fecha ingresada supera a la fecha actual:')
    verify_date(x)

def verify_int(x):
  employees[x]['number-of-children'] = input()
  if not(employees[x]['number-of-children'].isnumeric()):
    print('El dato ingresado no es un numero, por favor intentelo nuevamente:')
    verify_int(x)

def verify_company(x):
  employees[x]['company'] = input()
  if employees[x]['company'] != '1' and employees[x]['company'] != '2':
    print('El dato ingresado no es ni 1 ni 2, por favor intentelo nuevamente:')
    verify_company(x)

def diff_month(x):
  start = employees[x]['entry-date']
  end = datetime.datetime.now().strftime("%Y-%m-%d")

  s_date = datetime.datetime.strptime(start, "%Y-%m-%d")
  e_date = datetime.datetime.strptime(end, "%Y-%m-%d")

  return (e_date.year - s_date.year) * 12 + e_date.month - s_date.month

def calculate_tax_base(x):
  return "{:.2f}".format(float(employees[x]['base-salary']) + (float(employees[x]['base-salary']) * (diff_month(x) / 100)) + (float(employees[x]['base-salary']) * ((float(employees[x]['number-of-children']) * 5) / 100)))

def calculate_tax_health(x):
  return "{:.2f}".format(float(calculate_tax_base(x)) * 0.07)

def calculate_tax_SSO(x):
  tax = 0.12 if employees[x]['company'] == '1' else 0.114
  return "{:.2f}".format(float(calculate_tax_base(x)) * tax)

def average_pay(x):
  return float(calculate_tax_base(x)) - float(calculate_tax_health(x)) - float(calculate_tax_SSO(x))

for x in range(0, 1):
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

  #print('Por favor ingrese el nombre del empleado ' + str(x + 1) + ':')
  #verify_str(x)

  #print('Por favor ingrese el apellido del empleado ' + str(x + 1) + ':')
  #verify_str(x)

  print('Por favor ingrese el sueldo base del empleado ' + str(x + 1) + ', colocandolo como un numero decimal de 2 cifras, especificando los números decimales con punto y no con coma:')
  verify_float(x)

  print('Por favor ingrese la fecha de ingreso del empleado ' + str(x + 1) + ', en el siguiente formato "yyyy-mm-dd":')
  verify_date(x)

  print('Por favor ingrese la cantidad de hijos del empleado ' + str(x + 1) + ':')
  verify_int(x)

  print('Por favor ingrese a qué empresa pertenece, ingrese 1 si pertenece a la primera empresa que cobra un 12% de base imponible o 2 si pertenece a la segunda empresa que cobra un 11.4% de base imponible de empleado ' + str(x + 1) + ':')
  verify_company(x)

  print('La base imponible del empleado ' + str(x + 1) + ' es: ' + str(calculate_tax_base(x)) + '. Además debe pagar ' + str(calculate_tax_health(x)) + ' en salud y ' + str(calculate_tax_SSO(x)) + ' en gastos a su afiliacion con la empresa ' + str(employees[x]['company']) + ' de SSO. En promedio, el empleado cobrara: ' + str(average_pay(x)))

# print(employees)
