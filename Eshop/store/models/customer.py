from django.db import models

class Customer(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    retype_password = models.CharField(max_length=500,default='')

    def register(self):
        self.save()
    # defining a function to confirm that the every user should have unique emails id

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return False
            