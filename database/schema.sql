-- CREATE IF NOT EXISTS DATABASE 'citadel';

-- USE citadel;

CREATE TABLE members (
    member_id VARCHAR(20) NOT NULL PRIMARY KEY,
    profile_image VARCHAR(255),
    name CHAR(50) NOT NULL,
    dob DATE,
    gender CHAR(10),
    grade_year VARCHAR(15),
    id_number VARCHAR(20),
    phone VARCHAR(20),
    email VARCHAR(255),
    residence VARCHAR(50),
    status CHAR(20)
);

CREATE TABLE users (
    user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    member_id VARCHAR(20),
    password VARCHAR(255),
    role CHAR(50)
);

CREATE TABLE material (

);

CREATE TABLE loan (

);

CREATE TABLE fines (
    fine_id INT(4) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(),
    amount DECIMAL(6, 2),
    suspension INT(2),
    termination INT(2)
);

CREATE TABLE loss_damages (
    loss_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    material_id INT,
    inventory_id INT,
    description VARCHAR(255),
    fined CHAR(10),
);

CREATE TABLE inventory(
    inventory_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category CHAR(50), -- include furniture, electronics, cleaning equipments.
    sub_category CHAR(50), -- printers, computers, tables, chairs, tablets, shelves
    serial_number VARCHAR(50),
    description VARCHAR(255),
    condition CHAR(20),
    quantity INT(4),
    last_update DATE
);

CREATE TABLE payments (
    payment_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(8, 2),
    payment_date DATE,
    paid_by VARCHAR(20)
);

CREATE TABLE periods (
    period_id VARCHAR(10) NOT NULL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE,
    status CHAR(10) NOT NULL
);

CREATE TABLE time_schedule (
    slot_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    slot_date DATE,
    slot_time TIME,
    reserved_for VARCHAR(50),
    description VARCHAR(255),
    reserved_by CHAR(50),
    reserved_on DATE
);






