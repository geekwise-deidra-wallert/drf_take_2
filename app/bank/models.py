from django.db import models
import uuid

class Branch (models.Model):

    class Meta:
        verbose_name_plural = 'Branches'

    branch_name = models.CharField(max_length=25)
    location_city = models.CharField(max_length=50)
    location_id = str(uuid.uuid4)

    def __str__(self):
        return (
            f"Bank Name : {self.branch_name} | Bank City : {self.location_city}"
            )

class Client (models.Model):

    client_name = models.CharField(
        max_length=50,
        default=''
        )
    client_email = models.CharField(
        max_length=50,
        default=''
        )
    
    connect_to_branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )
    
    # connect_to_account = models.OneToOneField(
    #     Account,
    #     on_delete = models.CASCADE
    # )

    def __str__(self):
        return(
            f"{self.client_name} | {self.connect_to_branch}"
        )

class Account (models.Model):
    account_types = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('none', 'NONE'),
    )
    account_params = models.CharField(
        max_length = 8,
        choices = account_types,
        default = account_types[0]
    )
    account_balance = models.FloatField(max_length=500, default='0.00')

    connect_to_client = models.OneToOneField(
    Client, 
    on_delete = models.CASCADE
    )

    def __str__ (self):
        return(
            f"{self.connect_to_client.client_name} | Balance : {self.account_balance}"
        )



