import pandas as pd
import pymysql as mq
import sqlalchemy
mysql = mq.connect(host='localhost', user='root',
                   password='1234', port=3307, database='newminiproject')
mycursor = mysql.cursor()

# try:
#     db='create database dragon'
#     mycursor.execute(db)
#     print('database')
# except:
#     print("Error")


states = ["Andhra Pradesh", "Arunachal pradesh",
          "Assam", "Bihar", "chhatisgarh", "Madhya Pradesh"]

for i in states:
    # print(i)
    sql = 'SELECT *FROM weather_data WHERE State="%s";' % i
    # sql = 'select *from weather_data'
    mycursor.execute(sql)
    result = mycursor.fetchone()
    # print(end="\n\n\n")
    print(result)
    # for x in result:
    #     print(x)
