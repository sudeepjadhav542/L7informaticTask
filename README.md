
## Problem statement
Create a Simple Python Application for a fictional chocolate house that uses
SQLite to manage,
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns
use an ORM and dockerize this application.

## Features

- Manage seasonal chocolate flavors
- Keep track of ingredient inventory
- Record and manage customer suggestions
- SQLite database for data persistence
- Use of SQLAlchemy as an ORM to avoid writing sql queries
- Dockerized Application(i.e you can run your application without py installed in your local system)

## Prerequisites

- Python 3.6 or higher
- SQLite3

## Installation

1. Clone this repository or download the source code.
   ```
   git clone https://github.com/sudeepjadhav542/L7informaticTask.git
   ```
2. Navigate to the project directory in your terminal.

## File Structure

- `chocolate_house_app.py`: Main application file
- `seasonal_flavors.py`: Manages seasonal flavors
- `ingredient_inventory.py`: Manages ingredient inventory
- `customer_suggestions.py`: Manages customer suggestions
- `chocolate_house.db`: SQLite database file (will be created when you run the application)

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing the project files.
3. Run the following command to install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Run the following command:
   ```
   python chocolate_house_app.py
   ```

5. If you're using Python 3 and the above command doesn't work, try:
   ```
   python3 chocolate_house_app.py
   ```

6. The application will start, and you'll see the main menu in the console.

## Using the Application

1. From the main menu, choose an option by entering the corresponding number:
   - 1: Manage Seasonal Flavors
   - 2: Manage Ingredient Inventory
   - 3: Manage Customer Suggestions
   - 4: Exit

2. Follow the prompts to perform various operations within each module.

3. To exit the application, choose option 4 from the main menu.

## Testing

To validate the application, follow these test steps:

1. **Main Menu Navigation**
   - Start the application and verify that the main menu is displayed.
   - Test each menu option (1-4) to ensure it leads to the correct module or exits the application.

2. **Seasonal Flavors Module**
   - Add a new seasonal flavor (option 1).
   - View all flavors (option 2) and confirm the added flavor is listed.
   - Update an existing flavor (option 3) and verify the changes.
   - Delete a flavor (option 4) and confirm it's removed from the list.

3. **Ingredient Inventory Module**
   - Add a new ingredient (option 1).
   - View all ingredients (option 2) and confirm the added ingredient is listed.
   - Update the quantity of an existing ingredient (option 3) and verify the changes.
   - Delete an ingredient (option 4) and confirm it's removed from the list.

4. **Customer Suggestions Module**
   - Add a new customer suggestion (option 1).
   - View all suggestions (option 2) and confirm the added suggestion is listed.
   - Delete a suggestion (option 3) and confirm it's removed from the list.

5. **Data Persistence**
   - Exit the application and restart it.
   - Check that all previously added data (flavors, ingredients, suggestions) is still present.

6. **Error Handling**
   - Test invalid inputs in each module to ensure the application handles errors gracefully.
   - Try to update or delete non-existent items to verify proper error messages are displayed.

7. **Database Integrity**
   - Use a SQLite browser to open the `chocolate_house.db` file.
   - Verify that the tables (seasonal_flavors, ingredient_inventory, customer_suggestions) are created correctly.
   - Check that the data in the database matches what's displayed in the application.

By following these test steps, you can validate the functionality, data persistence, and error handling of the Chocolate House Management System.

## Run the Application through docker

You can also run this application using docker by following these commands

```bash
# Build the Docker image
docker build -t chocolate_house_app .

# Run the Docker container
docker run -it --rm chocolate_house_app
```
*Note* -it tag is a must as the application is a CLI interactive application you can replace the name to your custom image name.
