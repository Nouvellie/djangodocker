from django.contrib.auth.models import User
from django.db import models


class VerifiedAccount(models.Model):
    ver_acc_id = models.AutoField(db_column='VER_ACC_ID', primary_key=True, verbose_name='ID')
    ver_acc_verified = models.BooleanField(db_column='VER_ACC_VERIFIED', blank=True, null=True, verbose_name='VERIFIED')

    id = models.ForeignKey(User, db_column='USER_ID', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='ID')

    class Meta:
        db_table = 'verified_account'
        managed = True
        verbose_name = 'Verified account.'
        verbose_name_plural = 'Verified accounts.'