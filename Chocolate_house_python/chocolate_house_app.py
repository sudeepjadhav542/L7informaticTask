"""
Chocolate House Management System

This module serves as the main entry point for the Chocolate House Management System.
It provides a command-line interface for managing seasonal flavors, ingredient inventory,
and customer suggestions for a chocolate house business.
"""

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import os

from seasonal_flavors import manage_seasonal_flavors
from ingredient_inventory import manage_ingredient_inventory
from customer_suggestions import manage_customer_suggestions

DB_NAME = 'sqlite:///chocolate_house.db'
engine = create_engine(DB_NAME, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class SeasonalFlavor(Base):
    __tablename__ = 'seasonal_flavors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    description = Column(Text)

class IngredientInventory(Base):
    __tablename__ = 'ingredient_inventory'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)

class CustomerSuggestion(Base):
    __tablename__ = 'customer_suggestions'
    
    id = Column(Integer, primary_key=True)
    flavor_name = Column(String, nullable=False)
    description = Column(Text)
    allergy_concerns = Column(Text)
    submission_date = Column(DateTime, default=datetime.utcnow)

def initialize_database():
    """
    Set up the necessary tables in the database if they don't already exist.
    """
    Base.metadata.create_all(engine)

def display_main_menu():
    """Display the main menu options to the user."""
    print("\nChocolate House Management System")
    print("1. Manage Seasonal Flavors")
    print("2. Manage Ingredient Inventory")
    print("3. Manage Customer Suggestions")
    print("4. Exit")

def process_user_choice(choice, session):
    """
    Process the user's menu choice and call the appropriate function.

    Args:
        choice (str): The user's input choice.
        session (Session): The SQLAlchemy session object.

    Returns:
        bool: False if the user chooses to exit, True otherwise.
    """
    if choice == '1':
        manage_seasonal_flavors(session)
    elif choice == '2':
        manage_ingredient_inventory(session)
    elif choice == '3':
        manage_customer_suggestions(session)
    elif choice == '4':
        print("Thank you for using the Chocolate House Management System. Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def run_application():
    """
    Main application loop.
    
    This function establishes a database connection, initializes the database,
    and runs the main menu loop until the user chooses to exit.
    """
    initialize_database()
    
    with Session() as session:
        application_running = True
        while application_running:
            display_main_menu()
            user_choice = input("Enter your choice (1-4): ")
            application_running = process_user_choice(user_choice, session)

if __name__ == "__main__":
    run_application()
