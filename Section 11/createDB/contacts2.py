import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "another.update@update.com"
phone = input("Please enter the phone number: ")

# update_sql = f"UPDATE contacts SET email = {new_email} WHERE contacts.phone = {phone}"
update_sql = f"UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
# update_cursor.executescript(update_sql)
# print(f"{update_cursor.rowcount} rows updated")

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("---")

db.close()
