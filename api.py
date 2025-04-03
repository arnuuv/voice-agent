from flask import Flask, jsonify, request
from db import orders_db
from http import HTTPStatus
from typing import Dict, Any, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/orders', methods=["GET"])
def get_order() -> Tuple[Dict[str, Any], int]:
    """
    Retrieve order details by order number.
    
    Returns:
        Tuple containing response dictionary and HTTP status code
    """
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid JSON"}), HTTPStatus.BAD_REQUEST
        
        if "orderNumber" not in data:
            return jsonify({"error": "Missing orderNumber"}), HTTPStatus.BAD_REQUEST
        
        order_number = data["orderNumber"]
        order = orders_db.get(order_number)
        
        if not order:
            logger.info(f"Order not found: {order_number}")
            return jsonify({"error": "Order not found"}), HTTPStatus.NOT_FOUND
            
        response = {
            "order_number": order.order_number,
            "customer_name": order.customer_name,
            "order_date": order.order_date,
            "total_amount": order.total_amount,
            "status": order.status,
            "shipping_address": order.shipping_address
        }
        
        logger.info(f"Successfully retrieved order: {order_number}")
        return jsonify(response), HTTPStatus.OK
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)