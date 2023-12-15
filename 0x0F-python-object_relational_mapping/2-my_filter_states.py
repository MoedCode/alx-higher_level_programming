#!/usr/bin/python3
"""Write a script that lists
all states from the database
 hbtn_0e_0_usa
 """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    dp = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], dp=argv[3])
    cur = dp.cursor()
    qrr = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC;".format(argv[4])
    cur.execute(qrr)
    rows = cur.fetchall()
    for _ in rows:
        print(_)
