CREATE DATABASE sarawak_tourism;

USE sarawak_tourism;

CREATE TABLE Visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    visit_date DATE,
    visited_spots TEXT
);