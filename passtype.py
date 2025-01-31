class PassType:
    def __init__(self, name, validity_period_days):
        self.name = name
        self.validity_period_days = validity_period_days  # Pass validity period in days

    def __str__(self):
        return f"{self.name} (Valid for {self.validity_period_days} days)"