import sqlite3
import pandas as pd

# STEP 1A
# Import SQL Library and Pandas (Done above)

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# (Optional: Provided code to test employee data)
# employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
# print(employee_data)

# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# STEP 3
# Repeat Step 2, but reverse the column order
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)

# STEP 4
# Use an alias to rename employeeNumber as 'ID'
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)

# STEP 5
# Use CASE to bin job titles into Executive or Not Executive
# We use the IN operator to keep the query clean instead of multiple ORs
df_executive = pd.read_sql("""
    SELECT *,
    CASE 
        WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
    FROM employees
""", conn)

# STEP 6
# Find the length of the last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""", conn)

# STEP 7
# Return the first two letters of each job title
# SQLite uses SUBSTR(column, start_position, length). Note that SQL is 1-indexed!
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)

# STEP 8
# Find total amount (Sum of rounded (price * quantity))
# We round the product inside SQL, then use Pandas .sum() as suggested by the hint
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price 
    FROM orderDetails
""", conn).sum()

# STEP 9
# Extract day, month, and year from the orderDate
# SQLite uses strftime to format dates. %d = day, %m = month, %Y = year (4-digit)
# Note: In standard SQL sample databases, orderDate is often found in the `orders` table. 
# If `orderDetails` throws a "column not found" error, change the table name below to `orders`.
df_day_month_year = pd.read_sql("""
    SELECT orderDate, 
           strftime('%d', orderDate) AS day, 
           strftime('%m', orderDate) AS month, 
           strftime('%Y', orderDate) AS year 
    FROM orders
""", conn)

# Close the connection (ensure this is at the end of your script to free up resources)
conn.close()