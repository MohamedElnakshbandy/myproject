from database import SessionLocal
from models import User

db = SessionLocal()

try:
    new_user = User(
        name="Ahmed",
        email="ahmed@gmail.com"
    )

    db.add(new_user)
    db.commit()

    print("User added successfully!")

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()