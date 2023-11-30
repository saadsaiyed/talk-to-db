-- Create users table
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255)
);

-- Insert sample data into users table
INSERT INTO users (user_id, username, email)
VALUES
    (1, 'john_doe', 'john.doe@example.com'),
    (2, 'jane_smith', 'jane.smith@example.com'),
    (3, 'bob_jones', 'bob.jones@example.com');

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product_name VARCHAR(255),
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert sample data into orders table
INSERT INTO orders (order_id, user_id, product_name, order_date, amount)
VALUES
    (101, 1, 'Laptop', '2023-01-01', 1200.00),
    (102, 2, 'Smartphone', '2023-01-02', 800.00),
    (103, 3, 'Headphones', '2023-01-03', 100.00);