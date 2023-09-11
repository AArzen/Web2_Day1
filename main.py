from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

artist_list = db.execute("SELECT DISTINCT Name FROM Artist")
db.pretty_print("SELECT DISTINCT Name FROM Artist")
# for artist in artist_list:
#    print(artist[0])

german_ppl = db.execute("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")
db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")

cnt_albums = db.execute("SELECT COUNT (*) FROM Album")
print(f"Germany = {cnt_albums[0][0]}")

cnt_france_ppl = db.execute("SELECT COUNT (*) FROM Customer WHERE Country = 'France'")
print(f"France = {cnt_france_ppl[0][0]}")
