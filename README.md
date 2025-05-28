# Donation Project
A backend application for tracking donations, donors, staff, and related testing processes. Built using Python and SQLAlchemy.

## Features

 * Donors: Register and manage donor information.

 * Donations: Track donation details including amount, date, and donor association.

 * Staff: Assign staff to process donations and manage operations.

 * Tests: Link medical or eligibility tests with specific donations.

###  Tech Stack

   ~ Backend: Python, SQLAlchemy

   ~ Database: SQLite (default, but easily configurable to Postgres/MySQL)    
   
 ####   Project Structure

donation_project/
├── models/
│   ├── donor.py
│   ├── donation.py
│   ├── staff.py
│   ├── test.py
│   └── __init__.py
├── database/
│   └── setup.py
├── app.py
├── requirements.txt
└── README.md

##### Setup Instructions

1.    Clone the repository

~ git clone https://github.com/yourusername/donation_project.git
~ cd donation_project

 2.   Create a virtual environment and activate it

~ python -m venv venv
~ source venv/bin/activate  # On Windows: venv\Scripts\activate

 3.   Install dependencies

~ pip install -r requirements.txt 

4.   Set up the database
 ~python database/setup.py

5.   Run the application
~ python app.py

 ######  Schema Overview

  *  Donor

        id, name, email, blood_type

  *  Donation

        id, amount, date, donor_id, staff_id

 *   Staff

        id, name, role

  *  Test

        id, type, result, donation_id

     

 ######  Testing
~tested using pytest / unittest integration recommended

##### Future Features

   * REST API with FastAPI or Flask

   * Authentication for staff roles

  *  Dashboard and reporting tools

   * Donation eligibility checks

 ### Contributing

PRs are welcome! Please open an issue first for major changes or feature requests.

## License

MIT License


     






   
