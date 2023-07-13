from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse


User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,  verbose_name="Auteur")
    content = models.TextField(verbose_name="Contenu")
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    thumbnail = models.ImageField(
        upload_to='blog/thumbnails/', blank=True, null=True, verbose_name="Miniature")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(BlogPost, self).save(*args, **kwargs)

    @property
    def author_name(self):
        return self.author.username if self.author else "L'auteur inconnu"

    def get_absolute_url(self):
        return reverse("posts:home")
