CREATE DATABASE Friends;

CREATE TABLE Dogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    breed VARCHAR(255),
    command VARCHAR(255),
    birth_date DATE
);

CREATE TABLE Cats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    color VARCHAR(255),
    command VARCHAR(255),
    birth_date DATE
);

CREATE TABLE Hamsters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    fur_color VARCHAR(255),
    command VARCHAR(255),
    birth_date DATE
);

CREATE TABLE Horses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    color VARCHAR(255),
    command VARCHAR(255),
    birth_date DATE
);

CREATE TABLE Donkeys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    size VARCHAR(255),
    command VARCHAR(255),
    birth_date DATE
);


INSERT INTO Dogs (name, breed, command, birth_date) VALUES ('Buddy', 'Labrador Retriever', 'Sit', '2019-05-15');
INSERT INTO Cats (name, color, command, birth_date) VALUES ('Whiskers', 'Tabby', 'Meow', '2020-02-20');


DELETE FROM Camels;

ALTER TABLE Donkeys RENAME TO Horses;


CREATE TABLE YoungAnimals AS
SELECT *
FROM Dogs
WHERE birth_date BETWEEN DATE_SUB(NOW(), INTERVAL 3 YEAR) AND DATE_SUB(NOW(), INTERVAL 1 YEAR)
UNION
SELECT *
FROM Cats
WHERE birth_date BETWEEN DATE_SUB(NOW(), INTERVAL 3 YEAR) AND DATE_SUB(NOW(), INTERVAL 1 YEAR)
UNION
SELECT *
FROM Hamsters
WHERE birth_date BETWEEN DATE_SUB(NOW(), INTERVAL 3 YEAR) AND DATE_SUB(NOW(), INTERVAL 1 YEAR)
UNION
SELECT *
FROM Horses
WHERE birth_date BETWEEN DATE_SUB(NOW(), INTERVAL 3 YEAR) AND DATE_SUB(NOW(), INTERVAL 1 YEAR);



CREATE TABLE AllAnimals AS
SELECT 'Dog' AS animal_type, id, name, breed, command, birth_date FROM Dogs
UNION
SELECT 'Cat', id, name, color, command, birth_date FROM Cats
UNION
SELECT 'Hamster', id, name, fur_color, command, birth_date FROM Hamsters
UNION
SELECT 'Horse', id, name, color, command, birth_date FROM Horses;