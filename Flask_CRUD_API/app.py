from Laptop_crud import Laptop_Crud  # Assuming correct class name is LaptopCrud
from config import session

"""Simple Flask Application"""
from flask import Flask, jsonify, request

app = Flask("__name__")
laptop_crud = Laptop_Crud()  # Use lowercase for the instance name

# Create an endpoint in Flask to get started

@app.route('/')
def home():
    return "Welcome to Flask"

# Endpoint to get all laptops
@app.route('/laptops', methods=['GET'])  # Changed the route from /students to /laptops for clarity
def get_all_laptops():
    try:
        laptops = laptop_crud.get_all_laptops()  # Fetch the laptops using your CRUD class
        laptops_list = []
        
        for laptop in laptops:
            laptops_list.append({
                "laptop_name": laptop.laptop_name,
                "laptop_number": laptop.laptop_number,
                "student_id": laptop.student_id
            })
        
        return jsonify(laptops_list), 200  # Return 200 OK with the laptops list
    
    except Exception as e:
        return jsonify({"error": (e)}), 400  # In case of an error, return a 500 error with the error message


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application
