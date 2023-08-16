-- Replace 'your_database_name' with the actual name of your database
USE your_database_name;

-- Check if table exists
SELECT 1 FROM information_schema.tables WHERE table_schema = 'your_database_name' AND table_name = 'id_not_null' LIMIT 1;

-- If table does not exist, create it
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
