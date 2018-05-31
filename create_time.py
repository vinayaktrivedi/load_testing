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
	if set(['update_time','create_time']).issubset(df.columns):
		minima=2000000
		create_time=df['create_time']
		update_time=df['update_time']
		for k in range(len(create_time)):
			if create_time[k] is None or update_time[k] is None or create_time[k]=='0000-00-00 00:00:00' or update_time[k]=='0000-00-00 00:00:00':
				continue
			else:
				if minima > (update_time[k]-create_time[k]).seconds :
					minima= (update_time[k]-create_time[k]).seconds 
		if minima > 1000  :
			print(i[0])
				


				

		
		
