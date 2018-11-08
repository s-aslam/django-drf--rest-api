from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    discription = models.CharField(max_length=255, blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_by = models.IntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
    	db_table = 'products'

