from django.db import models
from django.utils import timezone

# Create your models here.
class PersonData(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    division=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    present_address=models.CharField(max_length=1000)
    about=models.CharField(max_length=1000)

    GENDER_CHOICHES = [
        ('M', 'Male'), 
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICHES)

    personal_number=models.IntegerField()
    relative_number=models.IntegerField()
    emergency_number=models.IntegerField()
    nid_number=models.IntegerField()
    person_face_image=models.ImageField(upload_to="person_face_image")
    person_nid_image=models.ImageField(upload_to="person_nid_image")
    person_fingerprint_image=models.ImageField(upload_to="person_fingerprint_image")
    timestamp=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"id:{self.id} name:{self.first_name} {self.last_name}"