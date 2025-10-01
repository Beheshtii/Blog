from django.db import models
from Accounts.models import User

class CategoryModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.title

class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'

    def __str__(self):
        if len(self.content) <= 30: return self.content
        return self.content[:30]

