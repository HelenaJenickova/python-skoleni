#datum a čas
from datetime import datetime, timedelta
print(datetime.now())

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%d. %m. %Y"))
date_time_format = "%d. %m. %Y, %H:%M"
apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")
apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", date_time_format)
delka_mise = apollo_pristani - apollo_start
print(delka_mise)

from datetime import datetime, timedelta
planovany_prijezd = datetime(2024, 3, 13, 19, 59)
zpozdeni = timedelta(minutes=10)
skutecny_prijezd = planovany_prijezd + zpozdeni
print(skutecny_prijezd)

#cviceni 
apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%m/%d/%Y"))

#cviceni 2
satelit_solar_orbiter = datetime(2020, 2, 10, 5, 3)
satelit_solar_orbiter.weekday()
print(satelit_solar_orbiter.weekday())
print(satelit_solar_orbiter.isoweekday())
od_startu_uplynulo = datetime.now() - satelit_solar_orbiter
print(od_startu_uplynulo)
print((datetime.now() - satelit_solar_orbiter).days / 365)

#doprava večeře
objednavka = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)
celkem = objednavka + prevzeti + doprava
print(celkem)

#bonus
prvni_udalost = datetime(2021, 7, 1)
druha_udalost = datetime(2021, 7, 3)


#falesna_jmena
from faker import Faker
fake = Faker()

print(fake.name())
print(fake.address())

for _ in range(10):
    print(fake.name())


#cviceni
from faker import Faker
fake = Faker("cs_CZ")

for _ in range(10):
  print(fake.name_female())
  print(fake.address())

  #cviceni
import humanize
humanize.activate("it_IT")

print(humanize.intword(1200000000))
print(humanize.apnumber(9))




