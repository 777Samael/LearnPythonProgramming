import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.phone = 1234"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f"{update_cursor.rowcount} rows updated")

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("---")

db.close()
