-- create_analytics_rev0.1 database setup snippet

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email)
VALUES ('alice', 'alice@example.com'),
       ('bob', 'bob@example.com');

SELECT * FROM users WHERE username = 'create_analytics_rev0.1';

# Additional Implementation 1760748680

# Additional Implementation 1760748680

# Additional Implementation 1760748681

# Code Update 1760748681-32729

# Additional Implementation 1760748681

# Code Update 1760748681-8066
