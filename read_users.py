from database import SessionLocal
from models import User

db = SessionLocal()

users = db.query(User).order_by(User.id).all()

for user in users:
    print(user.id, user.name, user.email)

db.close()