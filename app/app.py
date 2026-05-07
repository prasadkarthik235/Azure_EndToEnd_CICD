from flask import Flask, jsonify, request
import os
import socket

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Phone", "price": 30000},
    {"id": 3, "name": "Headphones", "price": 5000}
]

orders = []

@app.route("/")
def home():
    return jsonify({
        "message": "Azure DevOps CI/CD Demo Application",
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json

    order = {
        "order_id": len(orders) + 1,
        "product_id": data.get("product_id"),
        "quantity": data.get("quantity")
    }

    orders.append(order)

    return jsonify({
        "message": "Order created successfully",
        "order": order
    }), 201

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
