from django.db import models
from django.utils.text import slugify
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
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        if len(self.content) <= 30: return self.content
        return self.content[:30]

