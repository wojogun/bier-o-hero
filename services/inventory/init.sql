DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'inventory') THEN
        CREATE DATABASE inventory;
    END IF;
END
$$;

\c inventory

CREATE TABLE IF NOT EXISTS inventory (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    stock INTEGER NOT NULL,
    purchase_price FLOAT NOT NULL,
    sale_price FLOAT NOT NULL
);

INSERT INTO inventory (product_name, stock, purchase_price, sale_price)
VALUES
    ('Hirter Kellermeister', 50, 2.5, 4.0),
    ('Weitra Hell', 100, 0.9, 1.3),
    ('Mohrenbraeu Spezial', 25, 0.8, 1.2),
    ('Schremser Pils', 125, 0.5, 1.0)
ON CONFLICT DO NOTHING;
