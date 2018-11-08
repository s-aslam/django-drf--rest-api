from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.html import mark_safe
#from base.models import BaseModel
from django.utils.safestring import mark_safe

class User(AbstractUser):
    phone_number = models.BigIntegerField(blank=True, null=True, db_column='phone_number')
    is_deleted = models.BooleanField(default=False, db_column='is_deleted')
    created_by = models.IntegerField(blank=True, null=True, db_column='created_by')
    created_date = models.DateTimeField(blank=True, null=True, db_column='created_date',auto_now_add=True)
    updated_by = models.IntegerField(blank=True, null=True, db_column='updated_by')
    updated_date = models.DateTimeField(blank=True, null=True, db_column='updated_date',auto_now=True)
    
    class Meta:
        db_table = 'user_master'

    def getFullName(self):    
        if self.first_name and self.last_name:
            return mark_safe(self.first_name+"  "+self.last_name)
        else:
            return mark_safe(self.username)
