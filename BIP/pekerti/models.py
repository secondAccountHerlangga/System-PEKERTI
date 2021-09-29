from djongo import models

# reference https://www.djongomapper.com/using-django-with-mongodb-data-fields/#nesting-embedded-fields
class Permission(models.Model):
    validate_data = models.BooleanField()
    update_data_peserta = models.BooleanField()
    add_other_user =models.BooleanField()
class Admin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    permission = models.EmbeddedField(model_container=Permission)