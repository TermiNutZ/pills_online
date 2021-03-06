from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from main.util import query_document_similarity


class Medication(models.Model):
    """
    stores all info about medication
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False, unique=True)
    pharm_action = models.TextField(null=True)
    pharm_kinetic = models.TextField(null=True)
    indication = models.TextField(null=True)
    contra = models.TextField(null=True)
    dosage = models.TextField(null=True)
    side_effect = models.TextField(null=True)
    med_interact = models.TextField(null=True)
    spec_instruct = models.TextField(null=True)
    pregnancy = models.TextField(null=True)
    kidney = models.TextField(null=True)
    liver = models.TextField(null=True)
    clinic_pharm_group = models.TextField(null=True)
    form_composition = models.TextField(null=True)
    overdosage = models.TextField(null=True)
    child_policy = models.TextField(null=True)
    old_policy = models.TextField(null=True)
    distr_policy = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    img_path = models.CharField(max_length=200, null=True)
    analogues = models.ManyToManyField('self')
    warn_pregnancy = models.IntegerField(null=True)
    warn_kidney = models.IntegerField(null=True)
    warn_liver = models.IntegerField(null=True)


    def check_contradiction(self, profile_disease):
        """
        Check contraindication between user and drug
        :param profile_disease: diseases of user
        :return: True if there could be contraindication
        """
        if profile_disease == "" or self.contra == "" \
                or profile_disease is None or self.contra is None:
            return False

        return query_document_similarity(profile_disease, self.contra)


class Profile(models.Model):
    """
    additional info about user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True)
    weight = models.FloatField(null=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    pregnancy = models.NullBooleanField()
    allergy = models.TextField(null=True)
    liver_malfunction = models.NullBooleanField()
    kidney_malfunction = models.NullBooleanField()
    medications = models.ManyToManyField(Medication)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
