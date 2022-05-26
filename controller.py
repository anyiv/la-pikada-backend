from config import sales
from datetime import datetime, timedelta

products = []
zones = []
waiters = []
cashiers = []
payments = []
l_sales = []

def list_sales():
    for sale in sales:
        l_sales.append(sale)
    return l_sales


def list_products():
    for sale in sales:
        for product in sale['products']:
            products.append(product)

    return products


def total_ingress():
    l_sales = list_sales()
    amount = 0
    initial_date = l_sales[0]['date_closed']
    final_date = l_sales[len(l_sales)-1]['date_closed']
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
    names = list(set(zones))
    return names


def list_payments():
    for sale in sales:
        payments.append(sale['payments'])
    return payments


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

#cantidad de ventas por método de pago
def cant_by_payment_type():
    paym = list_payments()
    list_general = []
    type_names = []
    data = []
    for p in paym:
        for i in p:
            list_general.append(i)
            
    for t in list_general:
        type_names.append(t['type'])

    types = list(set(type_names))

    for type in types:
        data.append({'type': type, 'quantity':type_names.count(type)})

    result = sorted(data, key=lambda d: -d['quantity'])
    return result

#Lista de meseros por cantidad de ventas
def waiter_more_sales():
    list_sales()
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
    list_sales()
    l_cashiers = list_cashiers()
    names_general = []
    data = []

    for sale in sales:
        names_general.append(sale['cashier'])

    for cashier in l_cashiers:
        data.append({ 'name': cashier, 'quantity':names_general.count(cashier) })
    result = sorted(data, key=lambda d: -d['quantity'])
    return result

#Lista de productos por cantidad venta
def most_selled_products():
    l_products = list_products()
    names_general = []
    data = []
    for product in l_products:
        names_general.append(product['name'])

    products_name = list(set(names_general))

    for name in products_name:
        data.append({'name': name, 'quantity': names_general.count(name)})
    
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


  