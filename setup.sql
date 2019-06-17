CREATE DATABASE locator;

CREATE TABLE IF NOT EXISTS location(
    store_name VARCHAR(255),
    store_location VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(255),
    start_zip BIGINT,
    end_zip BIGINT,
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    county VARCHAR(255)
);
