# # import psycopg2

# # class DataManager:
# #     def __init__(self, db_name, user, password, host="localhost", port="5432"):
# #         self.connection = psycopg2.connect(
# #         dbname=db_name,
# #         user=user,
# #         password=password,
# #         host=host,
# #         port=port
# #         )
# #         self.cursor =self.connection.cursor()

# #     def insert_data(self, table_name, columns, values):
# #         query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
# #         self.cursor.execute(query, values)
# #         self.connection.commit()


# #     def close_conn(self):
# #         self.cursor.close()
# #         self.connection.close()

# # if __name__ == "__main__":
# #     db = DataManager("team4", "postgres", "3698")
# #     # db.insert_data("card", ["maxsulot_soni", "user_id", "book_id"], [20, 1, 1])
# #     # db.insert_data("books", ["name", "price", "author_id"], ["sariq devni minib", 25000, 1])
# #     # db.insert_data("likes", ["user_id", "book_id"], [1, 1])

# #     db.insert_data("coment", ["user_id", "book_id"], [1, 2])
# #     # db.insert_data("author", ["name", "age"], ["o'tkir hoshimov", 25])
# #     # db.insert_data("users", ["user_name", "user_age"], ["Asilbek", 25])





# import psycopg2

# class Database:
#     def __init__(self, dbname, user, password, host='localhost', port=5432):
#         self.conn = psycopg2.connect(
#             dbname = dbname,
#             password = password,
#             user = user,
#             host = host,
#             port = port
#         )
#         self.cursor = self.conn.cursor()
#         self.conn.autocommit = True

#     def add_to_table(self, table_name):
#         self.cursor.execute(f"select * from {table_name} limit 0")
#         if len(self.cursor.description) > 2:
#             columns = [i[0] for i in self.cursor.description]
#             new_data = []
#             added_columns = []
#             print(columns)
#             if len(columns) > 2:
#                 for i in columns[1:]:
#                     data = input(f"Enter {i} here:\t")
#                     if data:
#                         added_columns.append(i)
#                         new_data.append(data)


#                 columns = ", ".join(added_columns)
#                 placeholders = ", ".join(["%s"] * len(new_data))
#                 self.cursor.execute(f"insert into {table_name}({columns}) values ({placeholders})", new_data)
#                 self.conn.commit()

#         else: 
#             i = self.cursor.description[1][0]
#             data = input(f"Enter {i} here:\t")
#             self.cursor.execute(f"insert into {table_name}({i}) values ('{data}')")


# database = Database('team5', 'postgres', 3698)

# database.add_to_table('comment')



    
    


def add_table(table_name):
    d = True
    f = []
    while d:
        column = input("Column kiriting:")
        if column == 'exit':
            d = False
            continue
        type_ = input('data kiriting:')
        f.append(f"{column} {type_}")
        
    g = ','.join(f)
    f"create table {table_name} values ({g})"
    print(f)


add_table('wefqwer')