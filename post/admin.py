from django.contrib import admin
from .models import Post
from django.utils.text import slugify



class PostAdmin(admin.ModelAdmin):

    list_display = ["id", "title", "publishing_date", "slug", "user"]
    list_display_links = ["id", "title", "publishing_date", "slug"]
    list_filter = ["title", "publishing_date"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    # list_editable = ["title"]    ---list_display 'den title çıkarılması gerek (düzenleme işlemi)



    class Meta:

        model = Post



admin.site.register(Post, PostAdmin)