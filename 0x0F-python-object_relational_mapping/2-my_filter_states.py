#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    dp = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], dp=argv[3], port="3306")
    cur = dp.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY  '{}' ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for _ in rows:
        print(_)
