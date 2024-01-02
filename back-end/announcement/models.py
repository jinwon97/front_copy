# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Announcements(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    creationdate = models.DateTimeField(db_column='creationDate', auto_now_add=True)  # Field name made lowercase.
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=45)
    admin = models.ForeignKey('Admin', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'announcements'


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=75)
    password = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'admin'
