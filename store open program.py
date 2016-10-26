from datetime import datetime, time
from pytz import timezone
import pytz


def start():
    now_ny = datetime.now(timezone('US/Eastern'))
    ny_Time = time(hour= now_ny.hour)
    now_london = datetime.now(timezone('Europe/London'))
    lon_Time = time(hour=now_london.hour)
    store_open= time(hour=9, minute=0, second=0, microsecond=0)
    store_close= time(hour=21, minute=0, second=0, microsecond=0)
    get_ny_status(ny_Time, store_open, store_close)
    get_london_status(lon_Time, store_open, store_close)

def get_ny_status(ny_Time, store_open, store_close):
    if ny_Time > store_open and ny_Time < store_close:
        print ("New York OPEN")
    else:
        print ("New York CLOSED")
    

def get_london_status(lon_Time, store_open, store_close):
    if lon_Time > store_open and lon_Time < store_close:
        print ("London OPEN")
    else:
        print ("London CLOSED")
    






if __name__ == "__main__":
    start()
