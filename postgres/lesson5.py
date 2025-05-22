import psycopg2

db_info = {
    'dbname':'n64bd', 
    "user":'postgres', 
    "port":5432, 
    "password":'3698'
}
conn = psycopg2.connect(**db_info)
# conn = psycopg2.connect(dbname='n64bd', user='postgres', port=5432, password='3698')

cursor = conn.cursor()

# cursor.execute("""select *from cars""")
# print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchmany(10))

def select_table(table_name, count=0):
    cursor.execute(f"select *from {table_name}")
    data = cursor.fetchall()
    if count==0:
        for i in data:
            print(i)
    else:
        if count > len(data):
            for i in data:
                print(i)
            print(f"Sizda {len(data)} ta malumot bor edi")
        else:
            for i in data[:count]:
                print(i)
# select_table('students', 2)



def delete_table(table_name):
    try:
        cursor.execute(f"DROP TABLE {table_name}")
        conn.commit()
    except psycopg2.errors.UndefinedTable:
        print (f"Sizda {table_name} jadvali mavjud emas")
    else:
        print (f"{table_name} jadvali ochirildi!")

delete_table("persons")



conn.close()