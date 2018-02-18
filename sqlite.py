import csv
import sqlite3

con = sqlite3.connect('examples/db.sqlite')

# 유니코드 인코딩 문제 발생시 실행
# con.text_factory = str

# 파일 대신에 메모리에서 직접 데이터 베이스를 이용하는 코드
# con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS hanbit_books(
  title varchar(100),
  author varchar(100),
  translator varchar(100),
  pub_date date,
  isbn varchar(100) PRIMARY KEY 
)
""")
con.commit()

csv_file = open("examples/book_list.csv")
csv_reader = csv.reader(csv_file)
book_list = list(csv_reader)
book_list = book_list[1:]
for item in book_list:
    item[1] = item[1].strip()
    item[2] = item[2].strip()
print("book_list : ", book_list)

cur.executemany("INSERT OR REPLACE into hanbit_books values(?,?,?,?,?)", book_list)
con.commit()

cur.execute("SELECT * FROM hanbit_books WHERE author = ?", ["틱낫한"])
print("SELECT 윤웅식 :",cur.fetchall())

cur.execute("DELETE FROM hanbit_books WHERE author = ?", ["틱낫한"])


if cur :
    cur.close()
if con :
    con.close()

