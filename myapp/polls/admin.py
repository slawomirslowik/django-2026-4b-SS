from django.contrib import admin

from .models import Question, Choice

registered_models = [Question, Choice]

admin.site.register(registered_models)
