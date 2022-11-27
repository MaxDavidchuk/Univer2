from django.db import models


class Faculty(models.Model):
    # Properties:
    title = models.CharField(max_length=150, null=False)
    about = models.TextField(max_length=300, null=False)
    content = models.TextField(max_length=1024, null=False)
    photo = models.FileField(upload_to='photo/', null=True)
    logo = models.FileField(upload_to='logo/', null=True)
    url = models.URLField(null=True)
    # Repr:
    def __str__(self) -> str:
        return str(self.title)
