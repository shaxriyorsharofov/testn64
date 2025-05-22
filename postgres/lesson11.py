import psycopg2
from prettytable import PrettyTable
table = PrettyTable()
import csv

db_info = {
    'dbname':'lesson11', 
    "user":'postgres', 
    "port":5432, 
    "password":'3698'
}
conn = psycopg2.connect(**db_info)

cursor = conn.cursor()
conn.autocommit = True 



# cursor.execute("""
#     select  t.name, t.age, count(distinct c.name), count(s.id)
#     from course as c
#     inner join teacher as t
#     ON t.id =  c.teacher_id
#     left join students as s
#     on s.course_id = c.id
#     group by t.id
#                """)

# print(cursor.fetchall())

# table.field_names = ["Teacher name", "Teacher age", "students"]
# # # table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_rows([list(i) for i in cursor.fetchall()])

# print(table)


# def select_table(table_name):
#     cursor.execute(f"select *from {table_name}")
#     column = [i[0] for i in cursor.description]
#     table.field_names = column
#     table.add_rows([list(i) for i in cursor.fetchall()])
#     return table

# print(select_table('students'))

# def write_csv(table_name):
#     cursor.execute(f"select *from {table_name}")

#     with open('result.csv', 'a', newline='') as file:
#         write = csv.writer(file)
#         write.writerow([i[0] for i in cursor.description])
#         write.writerows([list(i) for i in cursor.fetchall()])

# write_csv('students')
    



print('sdfqwe')