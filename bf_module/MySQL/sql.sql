CREATE DATABASE bf_db;

CREATE TABLE city (
  city_id INT PRIMARY KEY,
  address VARCHAR(255),
  phone VARCHAR(20),
  info VARCHAR(255)
);

CREATE TABLE sensor (
  sensor_id INT PRIMARY KEY,
  type VARCHAR(50),
  topic VARCHAR(100),
  location VARCHAR(100),
  description VARCHAR(255)
);

CREATE TABLE humidity_reads (
  hr_id INT PRIMARY KEY,
  sensor_id INT,
  time_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  value DECIMAL(10,2),
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);
ALTER TABLE `humidity_reads` CHANGE `hr_id` `hr_id` INT(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `humidity_reads` ADD `payload` JSON NOT NULL AFTER `value`;

CREATE TABLE sensor_location (
  sensor_id INT,
  location_id INT,
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id),
  FOREIGN KEY (location_id) REFERENCES city(city_id)
);
