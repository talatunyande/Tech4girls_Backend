from config import session, engine  # Assuming session and engine are properly configured
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Backend(Base):
    __tablename__ = 'backend_class'  # Corrected to use double underscores
    
    student_id = Column(Integer, primary_key=True)  # Corrected: Removed the dot and fixed primary_key declaration
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(256), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    
    laptops = relationship("Laptops", back_populates="student")
    
    def __str__(self):
        return f"Student's ID: {self.student_id}, Name: {self.firstname} {self.lastname}, Age: {self.age}, Email: {self.email}"

class Laptops(Base):
    __tablename__ = 'laptops'
    
    laptop_name = Column(String(50), unique=True)
    laptop_number = Column(Integer, primary_key=True)  # Fixed: primary_key=True (not primary_Key)
    student_id = Column(Integer, ForeignKey('backend_class.student_id'), nullable=False)

    student = relationship("Backend", back_populates="laptops")
    
    def __str__(self):
        return f"Laptop Name: {self.laptop_name} (Laptop ID: {self.laptop_number}), Assigned to Student ID: {self.student_id}"

if __name__ == '__main__':
    try:
        # Corrected: use engine for table creation, not session.bind
        Base.metadata.create_all(engine)  # Create the tables
        print('Tables created.')
    except Exception as e:
        print(f'An error occurred: {e}')
