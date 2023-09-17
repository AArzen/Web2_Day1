from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")


# DAY_1_Homework

# artist_list = db.execute("SELECT DISTINCT Name FROM Artist")
# db.pretty_print("SELECT DISTINCT Name FROM Artist")
# # for artist in artist_list:
# #    print(artist[0])
#
# german_ppl = db.execute("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")
# db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")
#
# cnt_albums = db.execute("SELECT COUNT (*) FROM Album")
# print(f"Germany = {cnt_albums[0][0]}")
#
# cnt_france_ppl = db.execute("SELECT COUNT (*) FROM Customer WHERE Country = 'France'")
# print(f"France = {cnt_france_ppl[0][0]}")
# ______________________________________________________________________________________________________________________

# DAY_2_Homework

# (a) What order (Invoice) was the most expensive? Which one was the cheapest?
db.pretty_print("""
SELECT MIN(Invoice.Total) AS min_price,
MAX(Invoice.Total) AS max_price
FROM Invoice
""")
# SOLUTION
db.pretty_print("""
SELECT MIN(Invoice.Total), *
FROM Invoice
""")
db.pretty_print("""
SELECT MAX(Invoice.Total), *
FROM Invoice
""")

# (b) Which city (BillingCity) has the most orders?
db.pretty_print("""
SELECT Invoice.BillingCity AS City, count(*) AS Orders
FROM Invoice
GROUP BY Invoice.BillingCity
ORDER BY Orders DESC
LIMIT 9
""")
# SOLUTION - THE SAME
db.pretty_print("""
SELECT Invoice.BillingCity, COUNT(*) AS Invoice_num
FROM Invoice
GROUP BY Invoice.BillingCity
ORDER BY Invoice_num DESC
""")

# (c) Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.
db.pretty_print("""
SELECT COUNT (*) as Tracks
FROM Track WHERE Track.MediaTypeId = 2
""")
# SOLUTION
db.pretty_print("""
SELECT COUNT(*)
FROM Track
JOIN MediaType ON Track.MediaTypeId=MediaType.MediaTypeId
WHERE MediaType.Name='Protected AAC audio file'
""")

# (d) Find out what Artist has the most albums? (hint: check ORDER BY) - Vprašanje - DAL SEM JOIN Artist!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
db.pretty_print("""
SELECT Album.ArtistId, COUNT(*) AS Albums, Artist.Name
FROM Album
JOIN Artist ON Album.ArtistId=Artist.ArtistId
GROUP BY Album.ArtistId
ORDER BY COUNT(*) DESC
LIMIT 3
""")
# SOLUTION 1
db.pretty_print("""
SELECT Artist.Name, COUNT(*) as Album_num
FROM Artist
JOIN Album ON Album.ArtistId=Artist.ArtistId
GROUP BY Album.ArtistId
ORDER BY Album_num DESC
""")
# SOLUTION 2
db.pretty_print("""
SELECT COUNT(Artist.Name) AS Alb_count, Artist.Name AS Art_name
FROM Artist
INNER JOIN Album ON Album.ArtistId=Artist.ArtistId
GROUP BY Artist.ArtistId
ORDER BY -COUNT(Artist.Name)
""")


# (e) What genre has the most tracks? - Vprašanje - DAL SEM JOIN Genre!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
db.pretty_print("""
SELECT Genre.Name, COUNT(*) AS Tracks
FROM Track
JOIN Genre ON Track.GenreId=Genre.GenreId
GROUP BY Track.GenreId
ORDER BY COUNT(*)DESC
LIMIT 3
""")
# SOLUTION
db.pretty_print("""
SELECT Genre.Name, COUNT(*) as Track_num
FROM Genre
JOIN Track ON Track.GenreId = Genre.GenreId
GROUP BY Track.GenreId
ORDER BY Track_num DESC
""")

# (f) Which customer spent the most money so far? - Vprašanje - DAL SEM JOIN Customer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
db.pretty_print("""
SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Total
FROM Invoice
JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
GROUP BY Invoice.CustomerId
ORDER BY Total DESC
LIMIT 3
""")
# SOLUTION
db.pretty_print("""
SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Invoice_sum
FROM Customer
JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
GROUP BY Invoice.CustomerId
ORDER BY Invoice_sum DESC
""")

# (g) What songs were bought with each order? (hint: here you have to do a
# many-to-many SQL query with three tables: Track, Invoice and InvoiceLine. You have to do two JOINS here)
# SOLUTION
db.pretty_print("""
SELECT Invoice.InvoiceId, Track.Name
FROM Invoice
JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
JOIN Track ON InvoiceLine.TrackId = Track.TrackId;
""")
