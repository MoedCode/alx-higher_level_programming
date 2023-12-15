#!/usr/bin/python3
"""
script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    namae = argv[4]
    db = MySQLdb.Connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], dp=argv[3])
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s \
                    ORDER BY id ASC", (argv[4], ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
