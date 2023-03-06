#1.mysql 응용을 위해 라이브러리 가져오기
import pymysql
#2.db에 접속
db = pymysql.connect(host='127.0.0.1',
                    port=3306,
                    user='mydata',
                    password='mamawoaini1992!',
                    database='new_data',
                    charset='utf8'
                    )
#3. 커서를 가져오기
cur = db.cursor()

#4. 원하는 sql문 적기
sql = "select * from users where userid = 'aaa';" 
sql1 = "select * from users where userid = '%s';" %'aaa'
sql2 = "select * from users where userid = '{}';" .format('aaa')
sql3 = "select * from users where userid = %s;" 

# 5. 커서가 전달 받은 sql를 실행
# res = cur.execute(sql)

data = []
data.append('사용자의 id 를 입력하세요')

res = cur.execute(sql3,data)

#6. 결과를 확인하기
print(res)
users = cur.fetchall()
print(users)
for user in users:
    print(user)

#7.db 접속 끊기
db.close()
