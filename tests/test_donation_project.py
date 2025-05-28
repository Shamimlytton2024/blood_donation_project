import unittest
from io import StringIO
import sys
from lib.database import engine, Base, Session
from lib.models import Donor, Staff, Donation, Test
import cli
from sqlalchemy import inspect

class TestDonationProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create tables
        Base.metadata.create_all(engine)
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        Base.metadata.drop_all(engine)

    def setUp(self):
        # Start a new session for each test
        self.session = Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_database_tables_created(self):
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        self.assertIn('donors', tables)
        self.assertIn('staff', tables)
        self.assertIn('donations', tables)
        self.assertIn('tests', tables)

    def test_add_and_list_donor(self):
        # Add donor
        donor = Donor(name="Test Donor")
        self.session.add(donor)
        self.session.commit()

        # Capture output of list_donors
        captured_output = StringIO()
        sys.stdout = captured_output
        cli.list_donors()
        sys.stdout = sys.__stdout__

        self.assertIn("Test Donor", captured_output.getvalue())

    def test_add_donor_cli_empty_name(self):
        # Test add_donor with empty input
        input_values = ['']
        def mock_input(s):
            return input_values.pop(0)
        import builtins
        original_input = builtins.input
        builtins.input = mock_input

        captured_output = StringIO()
        sys.stdout = captured_output
        cli.add_donor()
        sys.stdout = sys.__stdout__

        builtins.input = original_input

        self.assertIn("Donor name cannot be empty.", captured_output.getvalue())

    def test_model_relationships(self):
        donor = Donor(name="Donor1")
        staff = Staff(name="Staff1")
        self.session.add_all([donor, staff])
        self.session.commit()

        donation = Donation(donor_id=donor.id, staff_id=staff.id)
        self.session.add(donation)
        self.session.commit()

        test = Test(donation_id=donation.id)
        self.session.add(test)
        self.session.commit()

        self.assertEqual(donation.donor.name, "Donor1")
        self.assertEqual(donation.staff.name, "Staff1")
        self.assertEqual(test.donation.id, donation.id)

if __name__ == '__main__':
    unittest.main()
