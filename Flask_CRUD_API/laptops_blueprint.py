from flask import Blueprint, request, jsonify
from laptop_crud import Laptop_crud
from config import session  

# Create the Blueprint
laptops_blueprint = Blueprint('laptops', __name__)

# Initialize the CRUD class to handle laptop operations
laptop_crud = Laptop_crud(session)

# Add a Laptop
@laptops_blueprint.route('/add', methods=['POST'])
def add_laptop():
    # Get JSON data from the request
    data = request.get_json()
    
    # Validate the presence of required fields
    if not data or not all(field in data for field in ['laptop_name', 'laptop_number', 'student_id']):
        return jsonify({"error": "Missing required fields: laptop_name, laptop_number, student_id"}), 400
    
    # Extract data fields
    laptop_name = data['laptop_name']
    laptop_number = data['laptop_number']
    student_id = data['student_id']
    
    # You can add the code to save the laptop data here using the laptop_crud object
    # Example: laptop_crud.add_laptop(laptop_name, laptop_number, student_id)
    
    return jsonify({"message": "Laptop added successfully!"}), 201
