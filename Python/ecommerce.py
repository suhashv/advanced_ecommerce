from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database of products
products_db = {
    1: {"name": "Virtual T-Shirt", "price": 19.99, "size": "M"},
    2: {"name": "Virtual Jacket", "price": 49.99, "size": "L"}
}

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products_db)

@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    product_id = data.get('product_id')
    if product_id not in products_db:
        return jsonify({"error": "Product not found"}), 404
    
    # Simulate order creation
    return jsonify({"message": f"Order placed for product ID {product_id}"}), 201

if __name__ == '__main__':
    app.run(debug=True)
