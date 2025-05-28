from lib.database import Session
from lib.models import Donor, Staff, Donation, Test

def seed():
    session = Session()

    # Create Donors
    donor1 = Donor(name="Praise")
    donor2 = Donor(name="Shana")
    donor3 = Donor(name="Ivrine")
    donor4 = Donor(name="Shilom")

    # Create Staff
    staff1 = Staff(name="Dr. Smith")
    staff2 = Staff(name="Nurse Ivana")
    staff3 = Staff(name="Dr. Sirima")
    staff4 = Staff(name="Nurse Laviniah")

    # Add to session
    session.add_all([donor1, donor2, donor3, donor4, staff1, staff2, staff3, staff4])
    session.commit()

    # Create Donations
    donation1 = Donation(donor=donor1, staff=staff1)
    donation2 = Donation(donor=donor2, staff=staff2)
    donation3 = Donation(donor=donor3, staff=staff3)
    donation4 = Donation(donor=donor4, staff=staff4)

    session.add_all([donation1, donation2])
    session.commit()

    # Create Tests
    test1 = Test(donation=donation1)
    test2 = Test(donation=donation2)
    test3 = Test(donation=donation3)
    test4 = Test(donation=donation4)

    session.add_all([test1, test2, test3, test4])
    session.commit()

    print("Seed data inserted successfully.")

if __name__ == "__main__":
    seed()
