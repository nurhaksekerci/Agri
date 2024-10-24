from django.db import models

class Contact(models.Model):
    SENDER_CHOICES = [
        ('Farmer', 'Farmer'),
        ('Business', 'Business'),
    ]

    full_name = models.CharField(verbose_name=("Name"), max_length=50)
    email = models.EmailField(verbose_name=("Email"), max_length=50)
    phone = models.CharField(verbose_name=("Phone"), max_length=50)
    message = models.TextField(verbose_name=("Message"))
    created_at = models.DateTimeField(verbose_name=("Created At"), auto_now_add=True)
    is_read = models.BooleanField(verbose_name=("Is Read?"), default=False)
    sender = models.CharField(verbose_name=("Sender"), max_length=10, choices=SENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone} - {self.created_at} - {self.get_sender_display()}"

class Subscribe(models.Model):
    email = models.CharField(verbose_name=("Name"), max_length=50)
    created_at = models.DateTimeField(verbose_name=("Created At"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.created_at}"