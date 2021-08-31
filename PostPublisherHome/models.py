from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

def directoy_path(instace, filename):
    return filename

class ProductPublisherModels(models.Model):
	Name = models.CharField(max_length=50)
	Description = models.TextField()
	Price = models.IntegerField()
	Rating = models.IntegerField()
	Image = models.FileField(upload_to = directoy_path, validators=[FileExtensionValidator(allowed_extensions=['jpg'])], null=True)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.Name