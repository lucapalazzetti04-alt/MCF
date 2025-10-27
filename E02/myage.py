
from datetime import datetime, timedelta
d= int(input(' Inserisci il giorno di nascita : '))
m= int(input(' Inserisci il mese di nascita : '))
y= int(input(" Inserisci l'anno di nascita : "))
mydate = datetime(year=y,month=m,day=d)
print('date:',       mydate       )
print('year:',  mydate.year  )
print('second:',mydate.second)
now=datetime.now()
timediff = now - mydate
years_diff = now.year - mydate.year
if (now.month, now.day) < (mydate.month, mydate.day):
    years_diff -= 1
days_diff= timediff.days
seconds_diff= int(timediff.total_seconds())
print("\nEtà calcolata:")
print(f"{'Anni:':10} {years_diff}")
print(f"{'Giorni:':10} {days_diff}")
print(f"{'Secondi:':10} {seconds_diff}")
