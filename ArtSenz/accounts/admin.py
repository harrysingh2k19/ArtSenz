from django.contrib import admin
from .models import model_like_article, model_user_article
# Register your models here.
admin.site.register(model_like_article)
admin.site.register(model_user_article)
