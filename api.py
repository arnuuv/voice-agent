from flask import Flask, jsonify, request
from db import orders_db
from http import HTTPStatus
from typing import Dict, Any, Tuple
import logging
from datetime import datetime

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

@app.route('/orders', methods=["POST"])
def create_order() -> Tuple[Dict[str, Any], int]:
    """
    Create a new order with the provided details.
    
    Expected JSON body:
    {
        "customer_name": str,
        "total_amount": float,
        "shipping_address": str
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), HTTPStatus.BAD_REQUEST
        
        required_fields = ["customer_name", "total_amount", "shipping_address"]
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                "error": "Missing required fields",
                "fields": missing_fields
            }), HTTPStatus.BAD_REQUEST
            
        # Generate unique order number (simple implementation)
        order_number = f"ORD-{len(orders_db) + 1:04d}"
        
        new_order = {
            "order_number": order_number,
            "customer_name": data["customer_name"],
            "order_date": datetime.now().isoformat(),
            "total_amount": float(data["total_amount"]),
            "status": "pending",
            "shipping_address": data["shipping_address"]
        }
        
        orders_db[order_number] = new_order
        logger.info(f"Created new order: {order_number}")
        
        return jsonify(new_order), HTTPStatus.CREATED
        
    except ValueError as ve:
        logger.error(f"Validation error: {str(ve)}")
        return jsonify({"error": "Invalid data format"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(f"Error creating order: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)