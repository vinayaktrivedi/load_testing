import pymysql as mysql 
import pandas as pd
import numpy as np 
from dateutil import parser
conn = mysql.connect(host='127.0.0.1', port=10002, user='root', passwd='root', db='pe')
cursor=conn.cursor()
sql="SHOW TABLES"
cursor.execute(sql)
table=cursor.fetchall()
for i in table:
	if i[0] == 'order' or i[0] =='auth_item':
		continue
	else:
		sql="SELECT * FROM "+i[0] 
	df = pd.read_sql(sql, con=conn)
	if set(['updated_at','created_at']).issubset(df.columns):
		minima=2000000
		created_at=df['created_at']
		updated_at=df['updated_at']
		for k in range(len(created_at)):
			if created_at[k] is None or updated_at[k] is None or created_at[k]=='0000-00-00 00:00:00' or updated_at[k]=='0000-00-00 00:00:00':
				continue
			else:
				if minima > (updated_at[k]-created_at[k]).seconds :
					minima= (updated_at[k]-created_at[k]).seconds 
		if minima > 1000  :
			print(i[0])
		
	else:
		print(i[0]+"not created/updated col")		


				

		
		
