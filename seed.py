from app import app
from models import db, Pet

# Drop all tables and create them again
db.drop_all()
db.create_all()

# Create sample pets
pets = [
    Pet(name="Bella", species="Dog", photo_url="https://cdn-prod.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg", age=3, notes="Friendly and loves to play."),
    Pet(name="Whiskers", species="Cat", photo_url="https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", age=2, notes="Calm and independent."),
    Pet(name="Nemo", species="Fish", photo_url="https://cdn.mos.cms.futurecdn.net/RY2EpSo74hvYXyAVpTN2Gg-1200-80.jpg", age=1, notes="Colorful and active."),
    Pet(name="Chirpy", species="Bird", photo_url='https://ars.els-cdn.com/content/image/3-s2.0-B9780323851251000934-f00093-04-9780323851251.jpg', age=4, notes="Loves to sing in the mornings."),
    Pet(name="Rex", species="Dog", photo_url="https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg", age=5, notes="Protective but friendly.", available=False),
]

# Add pets to the session and commit
db.session.add_all(pets)
db.session.commit()

