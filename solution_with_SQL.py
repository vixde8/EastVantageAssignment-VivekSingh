'''
Solution with SQL - 

Approach used is straight forward, establishing connection to the sqlite db and executing the query that gives desired output.
And csv_writer is used to write to write the contents of result query in csv file delimited by ;.

'''

import sqlite3, csv

connection = sqlite3.connect("Data Engineer_ETL Assignment.db")
cursor = connection.cursor()

# SQL Solution for the problem statement
my_sql_query = "select c.customer_id, c.age , i.item_id, sum(o.quantity) \
                FROM customers c \
                INNER JOIN sales s ON c.customer_id = s.customer_id \
                INNER JOIN orders o ON s.sales_id = o.sales_id \
                INNER JOIN items i ON o.item_id = i.item_id \
                WHERE c.age BETWEEN 18 AND 35 and o.quantity  > 0 \
                GROUP BY c.customer_id , c.age , i.item_id ;"

cursor.execute(my_sql_query)
results = cursor.fetchall()

'''
for row in results:             # Uncomment this to see output in Console
    print(row)
'''

csv_file_path = 'sql_solution_output.csv'
delimiter = ';'
header = ['Customer', 'Age', 'Item', 'Quantity']

with open(csv_file_path, 'w', newline='') as csv_file:              # Writing the result to a ';' delimited csv file
    csv_writer = csv.writer(csv_file, delimiter=delimiter)
    csv_writer.writerow(header)
    csv_writer.writerows(results)

print("Write Successful...")

cursor.close()
connection.close()