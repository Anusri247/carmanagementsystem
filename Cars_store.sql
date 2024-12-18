CREATE DATABASE CarSalesDB;
USE CarSalesDB;
CREATE TABLE cars (
    CarID INT AUTO_INCREMENT PRIMARY KEY,
    CarName VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    Price DECIMAL(10, 2)
);
INSERT INTO cars (CarName, Model, Year, Price)
VALUES ('Mercedes-Benz', 'S-Class', 2023, 12000000.00);

INSERT INTO cars (CarName, Model, Year, Price)
VALUES ('BMW', '7 Series', 2022, 9000000.50);

SELECT * FROM cars;
SELECT * FROM cars WHERE CarName = 'BMW';


