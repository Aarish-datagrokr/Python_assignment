import MySQLdb

def data_generator():
    db = MySQLdb.connect(user='root',db='sakila',password='messi@10')
    cursor = db.cursor()
    cursor.execute('Select * from actor')
    for row in cursor.fetchall():
        yield row


def main():
    for row in data_generator():
        print(row)


if '__main__' == __name__:
    main()