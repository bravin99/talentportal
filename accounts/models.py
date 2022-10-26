from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver


class AccountBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
EDU_CHOICES = (
    ("cert", "Certificate"),
    ("dip", "Diploma"),
    ("deg", "Degree"),
    ("mas", "Masters")
)

class Profile(AccountBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed_email = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100)
    alternative_email = models.EmailField()
    registered_id = models.CharField(max_length=15, verbose_name="ID/Alien Number")
    education = models.CharField(max_length=20, choices=EDU_CHOICES, default="cert")
    experience = models.CharField(max_length=10, help_text="put an acurate represantation of your experience")
    date_of_birth = models.DateTimeField(null=True, blank=True)
    town = models.CharField(max_length=65, null=True, blank=True)
    nationality = models.CharField(max_length=35, null=True, blank=True)
    current_location = models.CharField(max_length=155, null=True, blank=True)
    prefered_work_location = models.CharField(max_length=155, null=True, blank=True)
    languages = models.CharField(max_length=100, help_text="comma separated", null=True, blank=True)    
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
@receiver(post_save, sender=User)
def update_profile_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()