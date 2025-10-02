from django.db import models
from django.utils.text import slugify
from Accounts.models import User
from django.urls import reverse

class CategoryModel(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='عنوان')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد')

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'

    def __str__(self):
        return self.title

class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')
    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name='تصویر')
    content = models.TextField(verbose_name='بدنه')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='دسته بندی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        db_table = 'post'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        if len(self.content) <= 30: return self.content
        return self.content[:30]

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.id, self.slug])

