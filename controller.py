from config import sales
from datetime import datetime, timedelta

products = []
zones = []
waiters = []
cashiers = []
payments = []

def list_products():
    result = []
    for sale in sales:
        for product in sale['products']:
            products.append(product)

    for product in products:
        result.append(product['name'])
    return result


def total_ingress():
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


def list_zones():
    for sale in sales:
        zones.append(sale['zone'])
    result = list(set(zones))
    return result


def list_payments():
    list_general = []
    result = []
    for sale in sales:
        payments.append(sale['payments'])

    for p in payments:
        for i in p:
            list_general.append(i)
            
    for t in list_general:
        result.append(t['type'])
    return result


def list_waiters():
    for sale in sales:
        waiters.append(sale['waiter'])

    names_waiters = list(set(waiters))
    return names_waiters

def list_cashiers():
    for sale in sales:
        cashiers.append(sale['cashier'])

    names_cashiers = list(set(cashiers))
    return names_cashiers


#Cantidad de ventas por zona/zona más concurrida
def cant_by_zones():
    names = list_zones()
    data = []
    for name in names:
        data.append({'name': name, 'quantity': zones.count(name)})
    result = sorted(data, key=lambda d: -d['quantity'])
    return result

def filtered_payment_names():
    l_payments = list_payments()

    result = list(set(l_payments))
    return result


#cantidad de ventas por método de pago
def cant_by_payment_type():
    payments = list_payments()
    types = filtered_payment_names()
    data = []

    for type in types:
        data.append({'type': type, 'quantity':payments.count(type)})

    result = sorted(data, key=lambda d: -d['quantity'])
    return result

#Lista de meseros por cantidad de ventas
def waiter_more_sales():
    l_waiters = list_waiters()
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
    l_cashiers = list_cashiers()
    names_general = []
    data = []

    for sale in sales:
        names_general.append(sale['cashier'])

    for cashier in l_cashiers:
        data.append({ 'name': cashier, 'quantity':names_general.count(cashier) })
    result = sorted(data, key=lambda d: -d['quantity'])
    return result

def filtered_products_names():
    l_products = list_products() 

    result = list(set(l_products))
    return result

#Lista de productos por cantidad venta
def most_selled_products():
    l_products = list_products()
    products_name = filtered_products_names()
    data = []

    for name in products_name:
        data.append({'name': name, 'quantity': l_products.count(name)})
    
    result = sorted(data, key=lambda d: -d['quantity'])

    return result

#Ingreso por dia en rango de rechas
def ingress_by_date(initial_date, final_date):
    initial_d = datetime.strptime(initial_date, '%Y-%m-%d')
    final_d = datetime.strptime(final_date, '%Y-%m-%d')
    final_d_h = final_d + timedelta(days=1)
    amount = 0
    l_sales = [sale for sale in sales if datetime.strptime(sale['date_closed'], '%Y-%m-%d %X')  <= final_d_h and  datetime.strptime(sale['date_closed'], '%Y-%m-%d %X') >= initial_d]
    
    for sale in l_sales:
        amount += sale['total']
    result = dict({ 'initial_date': initial_d, 'final_date':final_d, 'amount': amount })
    return result

#Reportes por cantidad
def cants_reports():
    l_cashiers = list_cashiers()
    l_waiters = list_waiters()
    l_products = filtered_products_names()
    l_zones = list_zones()
    result = []
    result.append({ 'name': 'Nro de productos', 'cant' : len(l_products)})
    result.append({ 'name': 'Nro de cajeros', 'cant' : len(l_cashiers)})
    result.append({ 'name': 'Nro de meseros', 'cant' : len(l_waiters)})
    result.append({ 'name': 'Nro de zonas', 'cant' : len(l_zones)})

    return result

#Lista de ventas 
def sales_list_report():
    data = []
    for index, sale in enumerate(sales):
        data.append({ 'id': index, 'zone': sale['zone'], 'table': sale['table'],
         'diners': sale['diners'], 'nro_products': len(sale['products']), 'total': sale['total'], 'date': sale['date_closed'] })
    result = sorted(data, key=lambda d: d['date'], reverse=True)
    return result