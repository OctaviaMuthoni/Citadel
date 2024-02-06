-- Creating queries that define all data tables and their relationsips

CREATE TABLE members(
    member_id VARCHAR(20) NOT NULL PRIMARY KEY,
    id_type ENUM("Employee Card", "Student ID", "National ID", "Passport") NOT NULL,
    id_number VARCHAR(20) NOT NULL UNIQUE,
    firstname CHAR(20) NOT NULL,
    middlename CHAR(20) NOT NULL,
    lastname CHAR(20) NOT NULL,
    profile_image VARCHAR(255),
    dob DATE NOT NULL,
    gender ENUM("Female", "Male", "Other") NOT NULL,
    phone VARCHAR(14),
    email VARCHAR(255),
    current_resident VARCHAR(50),
    permanent_residence VARCHAR(50)
);

CREATE TABLE users(
    -- All system users are members
    user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    member_id VARCHAR(20) NOT NULL,
    password VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES (member_id) ON (members.member_id)
);

CREATE TABLE cards (
    card_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    serial_number VARCHAR(25) UNIQUE,
    expiry_date DATE
);

CREATE TABLE member_cards (
    issue_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    member_id VARCHAR(20) NOT NULL,
    card_number INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE,
    status ENUM("Active", "Returned", "Lost")
);

CREATE TABLE subscriptions (
    subscription_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    subscription_type ENUM("Premium", "Freemium Limited", "Freemium Unlimited"),
    period INT -- Period is given in months
    subscription_fee DECIMAL(8, 2)
);

CREATE TABLE member_subscription (
    member_id VARCHAR(20),
    subscription_id INT,
    subscription_date DATE,
    expiry_date DATE
);

CREATE TABLE member_suspension(
    sus_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    member_id VARCHAR(20) NOT NULL,
    reason CHAR(50),
    explanation VARCHAR(255),
    sus_date DATE,
    sus_end_date DATE,
    FOREIGN KEY (member_id) REFERENCES (member_id) ON (members)
);

-- Queries that create user views for all defined tables
-- Members VIEW
--CREATE OR REPLACE VIEW members_view (
--    member_id,
--    fullname,
--    subscription,
--    status
--);

-- Data Manipulation queries


-- Stored procedures
-- backup
-- unsubscriptions
