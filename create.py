from app import db
with app.app_context():
    db.create_all()
