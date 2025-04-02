from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/orders',methods = ["POST"])
def get_orders():
  data = request.get_json()
  if data is None:
    return jsonify({"error":"Invalid JSON"}),400
  
  if "orderNumber" not in data:
    return jsonify({"error":"Missing orderNumber"}),400
  order_number = data["orderNumber"]
  print(order_number)
  return jsonify({
    "order_number":order_number,
    "customer_name":"John Doe",
    "order_date":"2020-01-01",
    "total_amount":100,
    "status":"pending",
    "shipping_address":"123 Main St, New York, NY 10030"
  })