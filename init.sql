CREATE USER 'deniz'@'%' IDENTIFIED WITH mysql_native_password BY 'dnzpss';
GRANT ALL PRIVILEGES ON *.* TO 'deniz'@'%';
FLUSH PRIVILEGES;


CREATE DATABASE delivery_db;

USE delivery_db;

CREATE TABLE delivery (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tcgb_customs_administration_code INT,
    tcgb_customs_administration_name VARCHAR(100),
    tcgb_registration_number VARCHAR(50),
    tcgb_registration_date DATE,
    tcgb_closing_date DATE,
    sender_receiver_tax_number BIGINT,
    receiver_name TEXT,
    destination_country_17_code VARCHAR(10),
    destination_country_17_name VARCHAR(100),
    country_of_origin_code VARCHAR(10),
    country_of_origin_name VARCHAR(100),
    delivery_terms_code VARCHAR(10),
    item_serial_number INT,
    item_regime_code INT,
    item_regime_description TEXT,
    gtip_code BIGINT,
    gtip_description TEXT,
    commercial_description TEXT,
    tcgb_status_description VARCHAR(255),
    invoice_amount FLOAT,
    invoice_amount_currency_code VARCHAR(10),
    measurement_goods_quantity FLOAT,
    measurement_unit_description VARCHAR(50),
    net_weight_kg FLOAT,
    calculated_item_value_usd FLOAT,
    statistical_value_usd FLOAT,
    customs_administration_code VARCHAR(50),
    customs_administration_name VARCHAR(100),
    sender_receiver_name TEXT,
    sender_name VARCHAR(100),
    country_of_exit_code VARCHAR(10),
    country_of_exit_name VARCHAR(100),
    invoice_currency_code VARCHAR(10),
    tcgb_regional_directorate_code VARCHAR(10),
    tcgb_regional_directorate_name VARCHAR(100),
    customs_statistics_date DATE,
    insurance_amount FLOAT,
    receiver_identity_number VARCHAR(50),
    transportation_mode_description_of_border_vehicle VARCHAR(255),
    transportation_mode_code_of_border_vehicle VARCHAR(10),
    country_of_trade_name VARCHAR(100),
    country_of_trade_code VARCHAR(10),
    country_of_registration_of_exit_vehicle_name VARCHAR(100),
    country_of_registration_of_exit_vehicle_code VARCHAR(10),
    user_unit_value_usd FLOAT,
    freight_amount_tl FLOAT,
    gross_weight FLOAT,
    measurement_unit VARCHAR(50),
    measurement_unit_code VARCHAR(10),
    statistical_unit_code VARCHAR(10),
    statistical_unit_description VARCHAR(100)
);