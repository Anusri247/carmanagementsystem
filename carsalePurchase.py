import mysql.connector

def connect_db():
    """Establish a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="DESKTOP-2UKK8VK",
            user="root",  # Replace with your MySQL username
            password="12345678",  # Replace with your MySQL password
            database="carsalesdb"  # Replace with your database name
        )
        print("Database connection established.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table():
    """Create the cars table if it doesn't exist."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cars (
                CarID INT AUTO_INCREMENT PRIMARY KEY,
                CarName VARCHAR(50),
                Model VARCHAR(50),
                Year INT,
                Price DECIMAL(10, 2)
            );
            """
        )
        conn.commit()
        print("Table 'cars' created successfully (if it didn't exist).")
        conn.close()

def insert_car(car_name, model, year, price):
    """Insert a new car into the cars table."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO cars (CarName, Model, Year, Price) VALUES (%s, %s, %s, %s);"
        values = (car_name, model, year, price)
        cursor.execute(query, values)
        conn.commit()
        print(f"Car '{car_name}' inserted successfully.")
        conn.close()

def fetch_cars():
    """Fetch and display all cars from the cars table."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars;")
        rows = cursor.fetchall()
        print("\nCars in the Database:")
        for row in rows:
            print(row)
        conn.close()

def update_car(car_id, price):
    """Update the price of a car by its ID."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE cars SET Price = %s WHERE CarID = %s;"
        values = (price, car_id)
        cursor.execute(query, values)
        conn.commit()
        print(f"Car ID {car_id} updated successfully.")
        conn.close()

def delete_car(car_id):
    """Delete a car from the cars table by its ID."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM cars WHERE CarID = %s;"
        values = (car_id,)
        cursor.execute(query, values)
        conn.commit()
        print(f"Car ID {car_id} deleted successfully.")
        conn.close()

def main():
    """Main program to perform database operations."""
    create_table()

    while True:
        print("\n--- Car Sales Management ---")
        print("1. Add a new car")
        print("2. View all cars")
        print("3. Update car price")
        print("4. Delete a car")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            car_name = input("Enter car name: ")
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            price = float(input("Enter price: "))
            insert_car(car_name, model, year, price)
        elif choice == "2":
            fetch_cars()
        elif choice == "3":
            car_id = int(input("Enter car ID to update: "))
            price = float(input("Enter new price: "))
            update_car(car_id, price)
        elif choice == "4":
            car_id = int(input("Enter car ID to delete: "))
            delete_car(car_id)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()