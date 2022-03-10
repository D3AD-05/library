from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

def validate_rate(value):
    if value >= 5:
        raise ValidationError(
            _('%(value)s rating must be less than 5'),
            params={'value': value},
        )



class Books(models.Model):
    CATEGORY = (
        ('Fantasy','Fantasy'),
        ('Literary','Literary'),
        ('Mystery','Mystery'),
        ('Non-Fiction','Non-Fiction'),
        ('Science','Science'),
        ('Fiction','Fiction'),
        ('Thriller','Thriller'),
    )
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=200, choices=CATEGORY, null=True)
    author = models.CharField(max_length=100, null=True)
    review = models.IntegerField( null=True)
    rating = models.IntegerField(validators=[validate_rate])
    favourites = models.BooleanField(default=True)
    image = models.ImageField(upload_to='pic',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


def __str__(self):
    return self.title
