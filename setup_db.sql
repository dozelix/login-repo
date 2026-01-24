-- Script SQL para XAMPP - Ejecutar en phpMyAdmin o MySQL
-- URL: http://localhost/phpmyadmin

CREATE DATABASE IF NOT EXISTS login_db;
USE login_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verificar la tabla
SELECT * FROM usuarios;


