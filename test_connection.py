from database.mongodb import db

try:
    db.command("ping")
    print("✅ MongoDB Atlas Connected Successfully!")
except Exception as e:
    print("❌ Connection Failed")
    print(e)