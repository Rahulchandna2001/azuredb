-- Create department table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255)
);

-- Insert sample data into departments table
INSERT INTO departments (department_name, location)
VALUES ('HR', 'New York'), ('Engineering', 'San Francisco');

-- Create employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Update location column in departments table
ALTER TABLE departments MODIFY COLUMN location VARCHAR(100);

-- Delete a department by department_id
DELETE FROM departments WHERE department_id = 1;
