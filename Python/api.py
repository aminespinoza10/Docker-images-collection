from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory data store
items = [
    {"id": 1, "name": "Item 1", "description": "First item"},
    {"id": 2, "name": "Item 2", "description": "Second item"}
]

@app.route('/')
def home():
    """Root endpoint"""
    return jsonify({
        "message": "Welcome to the API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/api/items', methods=['GET'])
def get_items():
    """Get all items"""
    return jsonify(items), 200

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item by ID"""
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@app.route('/api/items', methods=['POST'])
def create_item():
    """Create a new item"""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    new_item = {
        "id": max([item["id"] for item in items]) + 1 if items else 1,
        "name": data["name"],
        "description": data.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item"""
    item = next((item for item in items if item["id"] == item_id), None)
    
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])
    
    return jsonify(item), 200

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item"""
    global items
    item = next((item for item in items if item["id"] == item_id), None)
    
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
