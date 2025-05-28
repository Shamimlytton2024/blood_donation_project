from lib.database import Session
from lib.models import Donor, Staff, Donation, Test

session = Session()

def list_donors() -> None:
    """List all donors in the database."""
    donors = session.query(Donor).all()
    print("Donors:")
    for d in donors:
        print(f"  ID: {d.id}, Name: {d.name}")

def add_donor() -> None:
    """Add a new donor to the database."""
    name = input("Enter donor name: ").strip()
    if not name:
        print("Donor name cannot be empty.")
        return
    donor = Donor(name=name)
    session.add(donor)
    session.commit()
    print(f"Donor '{name}' added with ID {donor.id}")

def main() -> None:
    """Main CLI loop for donor management."""
    while True:
        print("\nChoose an option:")
        print("1. List donors")
        print("2. Add donor")
        print("3. Exit")

        choice = input("> ").strip()

        if choice == "1":
            list_donors()
        elif choice == "2":
            add_donor()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
