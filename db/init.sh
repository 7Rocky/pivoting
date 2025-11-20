#!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL
);

CREATE TABLE auth (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) NOT NULL,
    password VARCHAR(64) NOT NULL
);

INSERT INTO employees (name, department, position) VALUES
('Alice Johnson', 'Engineering', 'Backend Developer'),
('Bob Smith', 'Engineering', 'DevOps Engineer'),
('Clara Wright', 'HR', 'HR Manager'),
('Daniel Kline', 'Sales', 'Sales Lead'),
('Eva Martinez', 'Security', 'Security Analyst'),
('Frank Lee', 'Engineering', 'Full Stack Developer');

INSERT INTO auth (username, password) VALUES
('manager', '866485796cfa8d7c0cf7111640205b83076433547577511d81f8030ae99ecea5');
EOSQL
