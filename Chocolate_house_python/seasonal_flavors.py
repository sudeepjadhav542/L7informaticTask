"""
Seasonal Flavors Management Module

This module provides functionality to manage seasonal chocolate flavors
in the Chocolate House Management System.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

Base = declarative_base()

class SeasonalFlavor(Base):
    __tablename__ = 'seasonal_flavors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    description = Column(String, nullable=True)

def manage_seasonal_flavors(session: Session):
    """
    Main function to manage seasonal flavors.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    while True:
        print("\nManage Seasonal Flavors")
        print("1. Add new flavor")
        print("2. View all flavors")
        print("3. Update flavor")
        print("4. Delete flavor")
        print("5. Return to main menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_flavor(session)
        elif choice == '2':
            view_flavors(session)
        elif choice == '3':
            update_flavor(session)
        elif choice == '4':
            delete_flavor(session)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_flavor(session: Session):
    """
    Add a new seasonal flavor to the database.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    name = input("Enter flavor name: ")
    season = input("Enter season (Spring/Summer/Fall/Winter): ")
    description = input("Enter flavor description: ")
    
    new_flavor = SeasonalFlavor(name=name, season=season, description=description)
    session.add(new_flavor)
    session.commit()
    print("Flavor added successfully!")

def view_flavors(session: Session):
    """
    View all seasonal flavors in the database.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    flavors = session.query(SeasonalFlavor).all()
    
    if not flavors:
        print("No flavors found.")
    else:
        for flavor in flavors:
            print(f"ID: {flavor.id}, Name: {flavor.name}, Season: {flavor.season}, Description: {flavor.description}")

def update_flavor(session: Session):
    """
    Update an existing seasonal flavor in the database.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    flavor_id = input("Enter the ID of the flavor to update: ")
    flavor = session.query(SeasonalFlavor).get(flavor_id)

    if flavor:
        name = input("Enter new name (press enter to skip): ")
        season = input("Enter new season (press enter to skip): ")
        description = input("Enter new description (press enter to skip): ")

        if name:
            flavor.name = name
        if season:
            flavor.season = season
        if description:
            flavor.description = description

        session.commit()
        print("Flavor updated successfully!")
    else:
        print("Flavor with the given ID does not exist.")

def delete_flavor(session: Session):
    """
    Delete a seasonal flavor from the database.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    flavor_id = input("Enter the ID of the flavor to delete: ")
    flavor = session.query(SeasonalFlavor).get(flavor_id)

    if flavor:
        session.delete(flavor)
        session.commit()
        print("Flavor deleted successfully!")
    else:
        print("Flavor with the given ID does not exist.")
