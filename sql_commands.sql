CREATE DATABASE contingency_db
GRANT ALL PRIVILEGES ON contingency_db.* TO 'contingency_user'@'%';

CREATE TABLE contingency (
    id INTEGER NOT NULL AUTO_INCREMENT,
    zip_code_start INTEGER NOT NULL DEFAULT 0,
    zip_code_end INTEGER NOT NULL DEFAULT 0,
    weight_start FLOAT(10.2),
    weight_end FLOAT(10,2),
    absolute_cost FLOAT(6,2),
    delivery_time INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
)
