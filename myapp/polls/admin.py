from django.contrib import admin

from .models import Question, Choice, Category, Comment

registered_models = [Question, Choice, Category, Comment]

admin.site.register(registered_models)
