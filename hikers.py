from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking_trip.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS user 
            (id integer primary key autoincrement, name text, age integer)""")

# db.execute("INSERT INTO user (name, age) VALUES ('Rika', '28')")

users = db.execute("SELECT name, age FROM user")

for record in users:
    print(record)

db.pretty_print("SELECT name, age FROM user")

# db.print_tables(verbose=False)

# db.execute("UPDATE user SET age = 34 WHERE id = 1")

# db.execute("DELETE FROM user WHERE id = 1")


# db.execute("ALTER TABLE user ADD email text")

db.pretty_print("SELECT name, age FROM user")
