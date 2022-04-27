import datetime
import pytz

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}

print("Please choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print(f"\t{place}. {available_zones[place]}")

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print(f"The time in {available_zones[choice]} is {world_time.strftime('%A %x %X %z')} {world_time.tzname()}")
        print(f"Local time is {datetime.datetime.now().strftime('%A %x %X')}")
        print(f"UTC time is {datetime.datetime.utcnow().strftime('%A %x %X')}")
        print()
