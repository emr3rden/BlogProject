from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home.views import home
from aboutme.views import aboutme
from contactme.views import contactme



urlpatterns = [
    path('admin/', admin.site.urls, name="yönetim"),

    path("account/", include("accounts.urls"), name="hesaplar"),

    path("", home, name="anasayfa"),

    path("aboutme/", aboutme, name="hakkimda"),

    path("contactme/", contactme, name="iletisim"),

    path("posts/", include("post.urls"), name="gonderiler"),
]



urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)