from datetime import datetime
from datetime import date

datetime.today()

today = datetime.today()
christmas = date(2021, 12, 25)
# christmas - todaydate
(christmas - todaydate).date

if christmas is not todaydate:
    print("sorry there are still" + str((christmas - todaydate).days) + "until Christmas!")
else:
    print("Yay it's Christmas!")



from datetime import datetime
from datetime import  timedelta

t = timedelta(days=4, hours=10)
# type(t)
# t.days
# t.seconds

# t.seconds / 60 / 60
# t.seconds / 3600

eta = timedelta(hours=6)
today= datetime.today()

# today
# eta
# today + eta

# str(today + eta)




