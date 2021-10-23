from django.db import models

# Create your models here.
class Person(models.Model):
    name            = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100, blank=True, null=True)
    phone_number    = models.CharField(max_length=10, blank=True, null=True)
    address         = models.JSONField()

    def __str__(self):
        return self.name + " - " + self.email

    class Meta:
        verbose_name_plural = "Persons"
        


class Clothes(models.Model):
    no_clothes      = models.IntegerField()
    cloth_type      = models.CharField(max_length=500)
    cloth_gender    = models.CharField(max_length=20)
    timestamp       = models.DateTimeField(auto_now_add=True) 
    person          = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.person.name + " - " + self.cloth_gender

    class Meta:
        verbose_name_plural = "Clothes"