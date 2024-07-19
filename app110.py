from datetime import datetime

fmt = '%Y/%m/%d %H:%M:%S'
data = datetime.strptime('2019/01/01 12:00:00', fmt)
print(data.strftime('%Y-%m-%d %H:%M:%S  %Y'))
