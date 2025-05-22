import psycopg2
from psycopg2.errors import UndefinedColumn, UndefinedTable

# db_info = {
#     'dbname':'n64bd', 
#     "user":'postgres', 
#     "port":5432, 
#     "password":'3698'
# }
# conn = psycopg2.connect(**db_info)

# cursor = conn.cursor()
# conn.autocommit = True  # Muhim!

# def delete_data(table_name, column_name, data):
#     cursor.execute(f"SELECT *FROM {table_name} WHERE {column_name}={data}")
#     if cursor.fetchone():
#         cursor.execute(f"DELETE FROM {table_name} WHERE {column_name}={data}")
#         conn.commit()
#         conn.close()
#         print(f"O'chirildi")
#     else:
#         print("Bunaqa malumot topilmadi")
    
# delete_data('cars', 'year', 1999)


# def drop_database(databse_name):
#     cursor.execute(f"DROP DATABASE {databse_name}")
#     conn.close()
    
    
# drop_database('n62')



# def update_data(table_name, column_name, data, update_column_name, new_data):
#     try:
#         cursor.execute(f"UPDATE {table_name} SET {update_column_name}={new_data} WHERE {column_name}={data}")
#     except UndefinedColumn:
#         print("Ozgartirmoqchi bolgan column mavzud emas")
#     except UndefinedTable:
#         print("Ozgartirmoqchi bolgan table mavjud emas")
#     else:
#         print("ozgartirildi") 
#     finally:
#         conn.close()    
# update_data(table_name='cars', column_name='model', data="'Impala'", update_column_name='year', new_data=2025)






class Database:
    def __init__(self, dbname, password, user, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            password=password,
            user=user,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True
        
    def delete_data(self, table_name, column_name, data):
        self.cursor.execute(f"SELECT *FROM {table_name} WHERE {column_name}={data}")
        if self.cursor.fetchone():
            self.cursor.execute(f"DELETE FROM {table_name} WHERE {column_name}={data}")
            self.conn.close()
            print(f"O'chirildi")
        else:
            print("Bunaqa malumot topilmadi")
            
            
            
    def insert_func(self, table_name):
        self.cursor.execute(f"SELECT *FROM {table_name}")
        columns = [i[0] for i in self.cursor.description]
        values = []
        columns_new = []
        for i in columns[1:]:
            data = input(f"{i} ni kiriting:")
            if data:
                values.append(data)
                columns_new.append(i)
            
        columns_str = ', '.join(columns_new)  
        self.cursor.execute(f"INSERT INTO {table_name}({columns_str}) VALUES{tuple(values)}")
                    
database1 = Database(dbname='n64bd', user='postgres', password='3698')
database1.insert_func('cars')














