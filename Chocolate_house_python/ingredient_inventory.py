"""
Ingredient Inventory Management Module

This module provides functionality to manage the ingredient inventory
in the Chocolate House Management System.
"""

from sqlalchemy.orm import Session,declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class IngredientInventory(Base):
    __tablename__ = 'ingredient_inventory'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)

def manage_ingredient_inventory(session: Session):
    """
    Main function to manage ingredient inventory.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    while True:
        print("\nManage Ingredient Inventory")
        print("1. Add new ingredient")
        print("2. View all ingredients")
        print("3. Update ingredient quantity")
        print("4. Delete ingredient")
        print("5. Return to main menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_ingredient(session)
        elif choice == '2':
            view_ingredients(session)
        elif choice == '3':
            update_ingredient_quantity(session)
        elif choice == '4':
            delete_ingredient(session)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_ingredient(session: Session):
    """
    Add a new ingredient to the inventory.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    name = input("Enter ingredient name: ")
    quantity = float(input("Enter quantity: "))
    unit = input("Enter unit of measurement: ")

    new_ingredient = IngredientInventory(name=name, quantity=quantity, unit=unit)
    session.add(new_ingredient)
    session.commit()
    print("Ingredient added successfully!")

def view_ingredients(session: Session):
    """
    View all ingredients in the inventory.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    ingredients = session.query(IngredientInventory).all()
    
    if not ingredients:
        print("No ingredients found.")
    else:
        for ingredient in ingredients:
            print(f"ID: {ingredient.id}, Name: {ingredient.name}, Quantity: {ingredient.quantity} {ingredient.unit}")

def update_ingredient_quantity(session: Session):
    """
    Update the quantity of an existing ingredient.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    ingredient_id = input("Enter the ID of the ingredient to update: ")
    new_quantity = float(input("Enter new quantity: "))

    ingredient = session.query(IngredientInventory).get(ingredient_id)
    if ingredient:
        ingredient.quantity = new_quantity
        session.commit()
        print("Ingredient quantity updated successfully!")
    else:
        print("Ingredient with the given ID does not exist.")

def delete_ingredient(session: Session):
    """
    Delete an ingredient from the inventory.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    ingredient_id = input("Enter the ID of the ingredient to delete: ")

    ingredient = session.query(IngredientInventory).get(ingredient_id)
    if ingredient:
        session.delete(ingredient)
        session.commit()
        print("Ingredient deleted successfully!")
    else:
        print("Ingredient with the given ID does not exist.")
