# Database name provided as the first argument
db_name=$1

# MySQL command to retrieve table information
mysql_cmd="SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
           FROM INFORMATION_SCHEMA.COLUMNS
           WHERE TABLE_SCHEMA = '$db_name'
           AND TABLE_NAME = 'first_table';"

# Execute the MySQL command
mysql -u <username> -p<password> -e "$mysql_cmd" $db_name