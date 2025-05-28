from lib.database import engine, Base
import lib.models  # This is VERY important!

# Create all tables
Base.metadata.create_all(engine)

print("All tables created successfully in blood_donation.db")
