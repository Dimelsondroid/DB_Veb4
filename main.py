import sqlalchemy
from pprint import pprint

class DataBase:
    db = 'postgresql:// '
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

my_db = DataBase()

#Домашнее задание к лекции «Select-запросы, выборки из одной таблицы»
#1
pprint(my_db.connection.execute(
    """
    SELECT album_name, album_release_year FROM Albums
    WHERE album_release_year = 2018;
    """
).fetchall())

#2
pprint(my_db.connection.execute(
    """
    SELECT track_name, duration FROM Tracks
    WHERE duration = (SELECT MAX(duration) FROM Tracks);
    """
).fetchall())

#3
pprint(my_db.connection.execute(
    """
    SELECT track_name FROM Tracks
    WHERE duration >= 210;
    """
).fetchall())

#4
pprint(my_db.connection.execute(
    """
    SELECT collection_name FROM Collections
    WHERE collection_release_year >= 2018 AND collection_release_year <= 2020;
    """
).fetchall())

#5
pprint(my_db.connection.execute(
    """
    SELECT performer_name FROM Artists
    WHERE performer_name NOT LIKE '%% %%';
    """
).fetchall())

#6
pprint(my_db.connection.execute(
    """
    SELECT track_name FROM Tracks
    WHERE track_name iLIKE '%%my%%' OR track_name iLIKE '%%мой%%';
    """
).fetchall())
