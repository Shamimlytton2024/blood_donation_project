# Blood Donation Management System

A robust backend system built with Python and SQLAlchemy ORM for managing blood donation operations, donor records, and medical testing workflows. This system demonstrates complex data modeling for healthcare logistics and donor management.

## 🚀 Features

- **Donor Management**: Complete CRUD operations for donor profiles and history tracking
- **Donation Tracking**: Record and monitor blood donations with timestamps and quantities
- **Staff Management**: Assign healthcare staff to process donations and manage operations
- **Medical Testing Integration**: Link eligibility tests and medical screenings to specific donations
- **Data Integrity**: Robust relational database design ensuring data consistency and accuracy

## 🛠️ Technology Stack

- **Backend Framework**: Python
- **ORM**: SQLAlchemy
- **Database**: SQLite (with potential for PostgreSQL migration)
- **Database Management**: SQLAlchemy ORM for object-relational mapping

## 📁 Project Structure



blood-donation-project/
├──main.py          # Application entry point
├──models.py        # SQLAlchemy data models
├──seed.py          # Database population script
├──config.py        # Configuration settings
├──requirements.txt # Project dependencies
└──README.md        # Project documentation



## 🗄️ Database Schema

The system implements a relational database with the following core entities:

- **Donors**: Personal information, contact details, and donation history
- **Donations**: Blood type, donation date, quantity, and donor association
- **Staff**: Healthcare personnel managing donation processes
- **Tests**: Medical tests and eligibility screenings linked to donations

## 🔧 Installation & Setup

1. **Clone the repository**
   bash
   git clone https://github.com/yourusername/blood-donation-project.git
   cd blood-donation-project


1. Create virtual environment
   bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
2. Install dependencies
   bash
   pip install -r requirements.txt
   
3. Initialize the database
   bash
   python main.py
   

💻 Usage

Basic Operations

python
# Example: Adding a new donor
from models import Donor, session

new_donor = Donor(
    name="John Doe",
    blood_type="A+",
    contact_info="john.doe@email.com"
)
session.add(new_donor)
session.commit()


Key Functionalities

· Register new donors with complete medical profiles
· Track donation history and frequency
· Assign staff to process donations
· Link medical tests to specific donations
· Generate reports on donation activities

🎯 Technical Highlights

· Object-Relational Mapping: Clean data access layer using SQLAlchemy ORM
· Data Validation: Built-in validation for medical data and donor information
· Relationship Management: Complex one-to-many and many-to-one relationships
· Session Management: Efficient database session handling and transaction control

🔮 Future Enhancements

· REST API implementation with Flask/FastAPI
· Frontend dashboard for real-time monitoring
· Analytics and reporting module
· Integration with hospital management systems
· Mobile application for donor engagement

🤝 Contributing

This project is open for improvements and extensions. Feel free to fork the repository and submit pull requests for additional features.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Developed by Shamim Kalande| Linkedin :https://www.linkedin.com/in/shamim-lytton-757b23227/
