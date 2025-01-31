import unittest
from datetime import datetime, timedelta
from passsystem import *
from skypass import *
from user import *
from passtype import *

# Unit Test Class
class TestPassSystem(unittest.TestCase):

    def setUp(self):
        """This method will run before each test."""
        # Set up the system and sample data
        self.system = PassSystem()
        self.daily_pass = self.system.add_pass_type("Daily Pass", 1)
        self.monthly_pass = self.system.add_pass_type("Monthly Pass", 30)
        self.user = self.system.add_user("John Doe", "johndoe@example.com")

    def test_add_user(self):
        """Test that users are being added to the system correctly"""
        self.assertEqual(len(self.system.users), 1)
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "johndoe@example.com")

    def test_add_pass_type(self):
        """Test that pass types are being added to the system correctly"""
        self.assertEqual(len(self.system.pass_types), 2)
        self.assertEqual(self.daily_pass.name, "Daily Pass")
        self.assertEqual(self.monthly_pass.validity_period_days, 30)

    def test_issue_pass(self):
        """Test that passes are being issued correctly to the user"""
        daily_pass_issued = self.user.issue_pass(self.daily_pass)
        self.assertEqual(len(self.user.passes), 1)
        self.assertEqual(daily_pass_issued.pass_type.name, "Daily Pass")
        self.assertTrue(daily_pass_issued.is_valid())

    def test_pass_expiry(self):
        """Test that passes expire correctly after the validity period"""
        # Issue a pass and fast-forward time by 2 days to expire the pass
        expired_pass = self.user.issue_pass(self.daily_pass)
        expired_pass.expiry_date = datetime.now() - timedelta(days=3)  # Manually set the pass issue date
        self.assertFalse(expired_pass.is_valid())

    def test_pass_validity_check(self):
        """Test that validity checks work correctly"""
        daily_pass_issued = self.user.issue_pass(self.daily_pass)
        # Pass should be valid at creation time
        self.assertTrue(daily_pass_issued.is_valid())

        # Manually simulate expiry by changing the date
        expired_pass = self.user.issue_pass(self.daily_pass)
        expired_pass.expiry_date = datetime.now() - timedelta(days=2)  # Set issue date to 2 days ago
        self.assertFalse(expired_pass.is_valid())

    def test_multiple_passes_for_user(self):
        """Test that a user can have multiple passes"""
        self.user.issue_pass(self.daily_pass)
        self.user.issue_pass(self.monthly_pass)
        self.assertEqual(len(self.user.passes), 2)
        self.assertEqual(self.user.passes[0].pass_type.name, "Daily Pass")
        self.assertEqual(self.user.passes[1].pass_type.name, "Monthly Pass")

    def tearDown(self):
        """This method will run after each test."""
        pass  # No teardown needed for this example

# Running the tests
if __name__ == "__main__":
    unittest.main()
