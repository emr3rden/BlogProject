from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



class Post(models.Model):

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar", related_name="posts")
    title = models.CharField(verbose_name="Başlık", max_length=120)
    content = RichTextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Tarih", auto_now_add=True)
    slug = models.SlugField(verbose_name="Link", unique=True, editable=True, max_length=150)
    image = models.ImageField(verbose_name="Resim", null=True, blank=True)



    def __str__(self):

        return self.title



    def get_unique_slug(self):

        slug = slugify(self.title.replace("ı", "i"))
        unique_slug = slug
        counter = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug



    def slugsave(self, *args, **kwargs):

        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)



    def get_absolute_url(self):

        return reverse("post:detail", kwargs={"slug": self.slug})



    def get_create_url(self):

        return reverse("post:create")



    def get_update_url(self):

        return reverse("post:update", kwargs={"slug": self.slug})



    def get_delete_url(self):

        return reverse("post:delete", kwargs={"slug": self.slug})



    class Meta():

        ordering = ["-publishing_date", "id"]



class Comment(models.Model):

    post = models.ForeignKey("post.Post", related_name="comments", on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name="İsim")
    content = models.TextField(verbose_name="Yorum")

    created_date = models.DateTimeField(auto_now_add=True)