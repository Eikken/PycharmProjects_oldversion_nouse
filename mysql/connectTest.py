import MySQLdb

def connectDB():
    db = MySQLdb.Connect("localhost","root","123456","iamstudents",charset='utf8')
    cursor = db.cursor()
    cursor.execute('select * from studentinfo')
    data = cursor.fetchone()
    # print(bool(data))
    print(data)
    db.close()


if __name__ == '__main__':
    connectDB()

