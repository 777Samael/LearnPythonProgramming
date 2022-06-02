import sqlite3
import pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()
    print(f"{utc_time},\t {local_time}")

db.close()
