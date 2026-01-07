from django.contrib import admin

from .models import Question, Choice, Category

registered_models = [Question, Choice, Category]

admin.site.register(registered_models)
