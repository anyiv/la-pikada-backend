from flask import Flask, jsonify, request
from flask_cors import CORS
from controller import *


app = Flask(__name__)
CORS(app)

@app.route('/api/cant-by-zones')
def cant_zones():
    return jsonify(cant_by_zones())


@app.route('/api/cant-by-payment-type')
def cant_type_payment():
    return jsonify(cant_by_payment_type())


@app.route('/api/waiter-more-sales')
def waiters_sales():
    return jsonify(waiter_more_sales())


@app.route('/api/cashier-more-sales')
def cashier_sales():
    return jsonify(cashier_more_sales())


@app.route('/api/income-by-date-range', methods=['POST'])
def income_by_range():
    initial_date = request.args.get('initial_date')
    final_date = request.args.get('final_date')
    return jsonify(income_by_date(initial_date,final_date))


@app.route('/api/poducts_most_selled')
def most_selled():
    return jsonify(most_selled_products())

@app.route('/api/total-amount')
def total_amount_income():
    return jsonify(total_income())

@app.route('/api/cant-reports')
def cantss_reports():
    return jsonify(cants_reports())

@app.route('/api/list-sales')
def l_sales_report():
    return jsonify(sales_report_list())


if __name__ == "__main__":
    app.run(debug = True)
