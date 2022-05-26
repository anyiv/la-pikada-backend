from config import sales
from datetime import datetime, timedelta

products = []
zones = []
waiters = []
cashiers = []
payments = []

def products_list():
    result = []
    for sale in sales:
        for product in sale['products']:
            products.append(product)

    for product in products:
        result.append(product['name'])
    return result


def total_income():
    amount = 0
    data = sorted(sales, key=lambda d: d['date_closed'])
    initial_date = data[0]['date_closed']
    final_date = data[len(sales)-1]['date_closed']
    for sale in sales:
        amount += sale['total'] 

    result = dict({
        'inicial_date': initial_date,
        'final_date': final_date,
        'amount': amount
    })
    return result 


def zones_list():
    for sale in sales:
        zones.append(sale['zone'])
    result = list(set(zones))
    return result


def payments_list():
    general_list = []
    result = []
    for sale in sales:
        payments.append(sale['payments'])

    for p in payments:
        for i in p:
            general_list.append(i)
            
    for t in general_list:
        result.append(t['type'])
    return result


def waiters_listers():
    for sale in sales:
        waiters.append(sale['waiter'])

    names_waiters = list(set(waiters))
    return names_waiters

def cashiers_list():
    for sale in sales:
        cashiers.append(sale['cashier'])

    names_cashiers = list(set(cashiers))
    return names_cashiers


#Cantidad de ventas por zona/zona más concurrida
def cant_by_zones():
    names = zones_list()
    data = []
    for name in names:
        data.append({'name': name, 'quantity': zones.count(name)})
    result = sorted(data, key=lambda d: -d['quantity'])
    return result

def filtered_payment_names():
    l_payments = payments_list()

    result = list(set(l_payments))
    return result


#cantidad de ventas por método de pago
def cant_by_payment_type():
    payments = payments_list()
    types = filtered_payment_names()
    data = []

    for type in types:
        data.append({'name': type, 'quantity':payments.count(type)})

    result = sorted(data, key=lambda d: -d['quantity'])
    return result

#Lista de meseros por cantidad de ventas
def waiter_more_sales():
    l_waiters = waiters_listers()
    names_general = []
    data = []

    for sale in sales:
        names_general.append(sale['waiter'])

    for waiter in l_waiters:
        data.append({ 'name': waiter, 'quantity':names_general.count(waiter) })
    result = sorted(data, key=lambda d: -d['quantity'])
    return result

#Lista de cajeros por cantidad de ventas
def cashier_more_sales():
    l_cashiers = cashiers_list()
    names_general = []
    data = []

    for sale in sales:
        names_general.append(sale['cashier'])

    for cashier in l_cashiers:
        data.append({ 'name': cashier, 'quantity':names_general.count(cashier) })
    result = sorted(data, key=lambda d: -d['quantity'])
    return result

def filtered_products_names():
    l_products = products_list() 

    result = list(set(l_products))
    return result

#Lista de productos por cantidad venta
def most_selled_products():
    l_products = products_list()
    products_name = filtered_products_names()
    data = []

    for name in products_name:
        data.append({'name': name, 'quantity': l_products.count(name)})
    
    result = sorted(data, key=lambda d: -d['quantity'])

    return result

#Ingreso por dia en rango de rechas
def income_by_date(initial_date, final_date):
    initial_d = datetime.strptime(initial_date, '%Y-%m-%d')
    final_d = datetime.strptime(final_date, '%Y-%m-%d')
    final_d_h = final_d + timedelta(days=1)
    amount = 0

    sales_l = [sale for sale in sales if datetime.strptime(sale['date_closed'], '%Y-%m-%d %X')  <= final_d_h and  datetime.strptime(sale['date_closed'], '%Y-%m-%d %X') >= initial_d]

    if len(sales_l) > 0:
        for sale in sales_l:
            amount += sale['total']
        result = dict({ 'initial_date': initial_d, 'final_date':final_d, 'amount': amount, 'status': True })

        return result
    else:
        result = dict({
            'msg': 'No hay registros dentro de ese rango de fechas',
            'status': False
        })
        return result

#Reportes por cantidad
def cants_reports():
    l_cashiers = cashiers_list()
    l_waiters = waiters_listers()
    l_products = filtered_products_names()
    l_zones = zones_list()
    result = []
    result.append({ 'name': 'Nro de productos', 'cant' : len(l_products)})
    result.append({ 'name': 'Nro de cajeros', 'cant' : len(l_cashiers)})
    result.append({ 'name': 'Nro de meseros', 'cant' : len(l_waiters)})
    result.append({ 'name': 'Nro de zonas', 'cant' : len(l_zones)})

    return result

#Lista de ventas 
def sales_report_list():
    data = []
    for index, sale in enumerate(sales):
        data.append({ 'id': index, 'zone': sale['zone'], 'table': sale['table'],
         'diners': sale['diners'], 'nro_products': len(sale['products']), 'total': sale['total'], 'date': sale['date_closed'] })
    result = sorted(data, key=lambda d: d['date'], reverse=True)
    return result