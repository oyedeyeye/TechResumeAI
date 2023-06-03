-- prepares a MySQL server for TechResumeAI project

CREATE DATABASE IF NOT EXISTS TechResumeAI;
-- CREATE USER IF NOT EXISTS 'TRAi_test'@'localhost' IDENTIFIED BY 'TRAi_test_pwd';
-- GRANT ALL PRIVILEGES ON `TechResumeAI`.* TO 'TRAi_test'@'localhost';
-- GRANT SELECT ON `performance_schema`.* TO 'TRAi_test'@'localhost';
-- FLUSH PRIVILEGES;

USE TechResumeAI;

CREATE TABLE IF NOT EXISTS User (
  id INT NOT NULL,
  github_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  avatar_url VARCHAR(60) NOT NULL,
  access_token VARCHAR(100) NOT NULL,
  created_at DATETIME NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Template (
  id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(255) NOT NULL,
  layout VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Resume_info (
  id INT NOT NULL,
  content JSON,
  created_at DATETIME NOT NULL,
  user_id INT NOT NULL,
  template_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES User(id),
  FOREIGN KEY (template_id) REFERENCES Template(id)
);