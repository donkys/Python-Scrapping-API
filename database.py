import sqlite3
conn = sqlite3.connect('hora.db')
print("เปิดฐานข้อมูลสำเร็จ")

conn.execute("INSERT INTO SAVEONE (ID,NAME,MESSENGE ) \
      VALUES (1, 'ต้นตาล','ทดสอบระบบ :D ')")
conn.execute("INSERT INTO SAVEONE (ID,NAME,MESSENGE ) \
      VALUES (2, 'วรรณพงษ์','ทดสอบระบบ ครับ  :D ')")
conn.commit()
print("เพิ่มระเบียงข้อมูลสำเร็จ")
conn.close() 