from flask import Flask, jsonify, request
from db import orders_db

app = Flask(__name__)

@app.route('/orders', methods=["GET"])
def get_order():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        
        if "orderNumber" not in data:
            return jsonify({"error": "Missing orderNumber"}), 400
        
        order_number = data["orderNumber"]
        order = orders_db.get(order_number)
        
        if not order:
            return jsonify({"error": "Order not found"}), 404
            
        return jsonify({
            "order_number": order.order_number,
            "customer_name": order.customer_name,
            "order_date": order.order_date,
            "total_amount": order.total_amount,
            "status": order.status,
            "shipping_address": order.shipping_address
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)