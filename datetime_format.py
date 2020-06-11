from datetimescript import datetime

oldformat = '01/02/2020'
datetimeobject = datetime.strptime(oldformat,'%m/%d/%Y')
newformat = datetimeobject.strftime('%d-%m-%Y')
print(newformat)