from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/orders',methods = ["POST"])
def get_orders():
  return jsonify