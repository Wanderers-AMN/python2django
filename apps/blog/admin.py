"""Importing Admin."""
from apps.blog.models import AnswerComments, Answers, QuestionComments, Questions, UserProfile

from django.contrib import admin

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Questions)
admin.site.register(QuestionComments)
admin.site.register(Answers)
admin.site.register(AnswerComments)
