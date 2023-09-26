from smartninja_sql.sqlite import SQLiteDatabase

import querys

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

# # (a) What order (Invoice) was the most expensive? Which one was the cheapest?
# db.pretty_print("""
# SELECT MIN(Invoice.Total) AS min_price,
# MAX(Invoice.Total) AS max_price
# FROM Invoice
# """)
# # SOLUTION
# db.pretty_print("""
# SELECT MIN(Invoice.Total), *
# FROM Invoice
# """)
# db.pretty_print("""
# SELECT MAX(Invoice.Total), *
# FROM Invoice
# """)
#
# # (b) Which city (BillingCity) has the most orders?
# db.pretty_print("""
# SELECT Invoice.BillingCity AS City, count(*) AS Orders
# FROM Invoice
# GROUP BY Invoice.BillingCity
# ORDER BY Orders DESC
# LIMIT 9
# """)
# # SOLUTION - THE SAME
# db.pretty_print("""
# SELECT Invoice.BillingCity, COUNT(*) AS Invoice_num
# FROM Invoice
# GROUP BY Invoice.BillingCity
# ORDER BY Invoice_num DESC
# """)
#
# # (c) Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.
# db.pretty_print("""
# SELECT COUNT (*) as Tracks
# FROM Track WHERE Track.MediaTypeId = 2
# """)
# # SOLUTION
# db.pretty_print("""
# SELECT COUNT(*)
# FROM Track
# JOIN MediaType ON Track.MediaTypeId=MediaType.MediaTypeId
# WHERE MediaType.Name='Protected AAC audio file'
# """)
#
# # (d) Find out what Artist has the most albums? (hint: check ORDER BY)
# db.pretty_print("""
# SELECT Album.ArtistId, COUNT(*) AS Albums, Artist.Name
# FROM Album
# JOIN Artist ON Album.ArtistId=Artist.ArtistId
# GROUP BY Album.ArtistId
# ORDER BY COUNT(*) DESC
# LIMIT 3
# """)
# # SOLUTION 1
# db.pretty_print("""
# SELECT Artist.Name, COUNT(*) as Album_num
# FROM Artist
# JOIN Album ON Album.ArtistId=Artist.ArtistId
# GROUP BY Album.ArtistId
# ORDER BY Album_num DESC
# """)
# # SOLUTION 2
# db.pretty_print("""
# SELECT COUNT(Artist.Name) AS Alb_count, Artist.Name AS Art_name
# FROM Artist
# INNER JOIN Album ON Album.ArtistId=Artist.ArtistId
# GROUP BY Artist.ArtistId
# ORDER BY -COUNT(Artist.Name)
# """)
#
#
# # (e) What genre has the most tracks?
# db.pretty_print("""
# SELECT Genre.Name, COUNT(*) AS Tracks
# FROM Track
# JOIN Genre ON Track.GenreId=Genre.GenreId
# GROUP BY Track.GenreId
# ORDER BY COUNT(*)DESC
# LIMIT 3
# """)
# # SOLUTION
# db.pretty_print("""
# SELECT Genre.Name, COUNT(*) as Track_num
# FROM Genre
# JOIN Track ON Track.GenreId = Genre.GenreId
# GROUP BY Track.GenreId
# ORDER BY Track_num DESC
# """)
#
# # (f) Which customer spent the most money so far?
# db.pretty_print("""
# SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Total
# FROM Invoice
# JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
# GROUP BY Invoice.CustomerId
# ORDER BY Total DESC
# LIMIT 3
# """)
# # SOLUTION
# db.pretty_print("""
# SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Invoice_sum
# FROM Customer
# JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
# GROUP BY Invoice.CustomerId
# ORDER BY Invoice_sum DESC
# """)
#
# # (g) What songs were bought with each order? (hint: here you have to do a
# # many-to-many SQL query with three tables: Track, Invoice and InvoiceLine. You have to do two JOINS here)
# # SOLUTION
# db.pretty_print("""
# SELECT Invoice.InvoiceId, Track.Name
# FROM Invoice
# JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
# JOIN Track ON InvoiceLine.TrackId = Track.TrackId;
# """)


# # TRACK, INVOICE, INVOICE LINE
# db.pretty_print("""
# SELECT Invoice.InvoiceId, Invoice.InvoiceDate, Track.TrackId, Track.Name Track_name
# FROM Track
# JOIN InvoiceLine ON InvoiceLine.TrackId = Track.TrackId
# JOIN Invoice ON Invoice.InvoiceId = InvoiceLine.InvoiceId
# LIMIT 3
# """)
#
# db.pretty_print("""
# SELECT Invoice.InvoiceId, Invoice.InvoiceDate, Track.TrackId, Track.Name as Track_name, InvoiceLine.InvoiceId IID,
# InvoiceLine.TrackId TID
# FROM Invoice
# JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
# JOIN Track ON Track.TrackId = InvoiceLine.TrackId
#
# """)
# ______________________________________________________________________________________________________________________

# DAY_5_Session
# from sqla_wrapper import SQLAlchemy


# from sqlalchemy import Column, Integer, String
# from .base import db
#
#
# # db = SQLAlchemy("sqlite:///localhost.sqlite")
#
#
# # db = SQLAlchemy(dialect='sqlite', name='localhost.sqlite')
#
#
# class Messages(db.Model):
#     __tablename__ = "Messages"
#
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String)
#     user_name = db.Column(db.String)
#
#
# class User(db.Model):
#     __tablename__ = "Users"
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String)
#
#
# class DataHead(db.Model):
#     __tablename__ = "DataHead"
#
#     id = db.Column(db.Integer, primary_key=True)
#     Serial_number = db.Column(db.Integer)
#
#
# class ParameterList(db.Model):
#     __tablename__ = "ParameterList"
#
#     id = db.Column(db.Integer, primary_key=True)
#     id_DataHead = db.Column(db.Integer)
#     ActualValue = db.Column(db.Integer)
#     Name = db.Column(db.String)
#
#
# db.create_all()
#
#
#
# # messages = Messages(test="This is a third message")
# # db.add(messages)
# #
# # db.commit()
#
# # messages = db.query(Messages).filter(Messages.id == 1).all()
# # print(messages[0])
# # print(messages[0].test)
# #
# # first_message = db.query(Messages).filter(Messages.id == 1).first()
# #
# # print(first_message.id, first_message.test)
#
# data = db.query(DataHead, ParameterList).filter(DataHead.id == ParameterList.id_DataHead).all()
# # print(data[0].id, data[0].Serial_number)
# # print(data[0][0].id, data[0][0].Serial_number)
# # print(data[0][1].id, data[0][1].id_DataHead, data[0][1].ActualValue, data[0][1].Name)


import tables

if __name__ == '__main__':

    # Create tables if not exist
    # tables.create_tables()

    # add new message data
    # querys.insert_message('Hello from over there!', 'Tutam')

    # get all messages
    data = querys.get_all_data_message()
    print('Messages')
    for message in data:
        print(f"row {message.id} message: {message.text} User: {message.user_name}")

    # get all messages from user X
    data = querys.get_data_message_filter_user("Tutam")
    print('Messages')
    for message in data:
        print(f"row {message.id} message: {message.text} User: {message.user_name}")


    print('PARAMATERS')
    db1 = SQLiteDatabase("localhost.sqlite")



    # Insert part into Data Head
    db1.execute("INSERT INTO DataHead (Serial_number) VALUES (0001)")
    # Find row sorted by serial number
    data = db1.execute("SELECT DataHead.id FROM DataHead WHERE DataHead.Serial_number = 0001")
    print(f'DataHead.id: {data[0][0]}')
    # Insert parameter data
    db1.execute(f"INSERT INTO ParameterList (id_DataHead, ActualValue, Name) VALUES ({data[0][0]}, 100, 'Parameter 1')")
    data = db1.execute("SELECT * FROM ParameterList")
    print(f'ParameterList.id: {data[0][0]}, ParameterList.id_DataHead: {data[0][1]}, ParameterList.ActualValue: {data[0][2]}, ParameterList.Name: {data[0][3]} ')

