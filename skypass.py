from datetime import datetime, timedelta

class SkyPass:
    def __init__(self, pass_type, user, issue_date=None):
        self.pass_type = pass_type
        self.user = user
        self.issue_date = issue_date or datetime.now()   # Defaults to current time
        self.expiry_date = self.issue_date + timedelta(days=self.pass_type.validity_period_days)

    def is_valid(self):
        """Check if the pass is still valid based on expiration date"""
        return datetime.now() <= self.expiry_date

    def __str__(self):
        status = "Valid" if self.is_valid() else "Expired"
        return f"Pass for {self.user.name}: {self.pass_type} - {status}"
