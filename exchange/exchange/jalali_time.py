from datetime import datetime
from khayyam import JalaliDatetime

# Converting now date time to jalali and format it
now = datetime.now()
jalali = JalaliDatetime(now).strftime('%y-%B-%d  %A  %H:%M')
