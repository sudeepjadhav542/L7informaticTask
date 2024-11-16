"""
Customer Suggestions Management Module

This module provides functionality to manage customer suggestions
in the Chocolate House Management System.
"""

from datetime import datetime
from sqlalchemy.orm import Session,declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

Base = declarative_base()

class CustomerSuggestion(Base):
    __tablename__ = 'customer_suggestions'
    
    id = Column(Integer, primary_key=True)
    flavor_name = Column(String, nullable=False)
    description = Column(Text)
    allergy_concerns = Column(Text)
    submission_date = Column(DateTime,default=datetime.utcnow)

def manage_customer_suggestions(session: Session):
    """
    Main function to manage customer suggestions.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    while True:
        print("\nManage Customer Suggestions")
        print("1. Add new suggestion")
        print("2. View all suggestions")
        print("3. Delete suggestion")
        print("4. Return to main menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_suggestion(session)
        elif choice == '2':
            view_suggestions(session)
        elif choice == '3':
            delete_suggestion(session)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_suggestion(session: Session):
    """
    Add a new customer suggestion to the database.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    flavor_name = input("Enter suggested flavor name: ")
    description = input("Enter flavor description: ")
    allergy_concerns = input("Enter any allergy concerns (comma-separated): ")
    submission_date = datetime.now()

    new_suggestion = CustomerSuggestion(
        flavor_name=flavor_name,
        description=description,
        allergy_concerns=allergy_concerns,
        submission_date=submission_date
    )

    session.add(new_suggestion)
    session.commit()
    print("Suggestion added successfully!")

def view_suggestions(session: Session):
    """
    View all customer suggestions in the database.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    suggestions = session.query(CustomerSuggestion).all()
    
    if not suggestions:
        print("No suggestions found.")
    else:
        for suggestion in suggestions:
            print(f"ID: {suggestion.id}, Flavor: {suggestion.flavor_name}, Description: {suggestion.description}")
            print(f"Allergy Concerns: {suggestion.allergy_concerns}, Submitted: {suggestion.submission_date}")
            print("-" * 50)

def delete_suggestion(session: Session):
    """
    Delete a customer suggestion from the database.

    Args:
        session (Session): The SQLAlchemy session object.
    """
    suggestion_id = input("Enter the ID of the suggestion to delete: ")

    suggestion = session.query(CustomerSuggestion).get(suggestion_id)
    if suggestion:
        session.delete(suggestion)
        session.commit()
        print("Suggestion deleted successfully!")
    else:
        print("Suggestion with the given ID does not exist.")
