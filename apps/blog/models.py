"""Import Django inbuilt user."""
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class UserProfile(models.Model):
    """model for storing user info while registering."""

    user = models.OneToOneField(User)

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Name')

    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name='Email')

    def __unicode__(self):
        """Method displays the Name field in admin view."""
        return self.name


class Questions(models.Model):
    """Model to save questions posted in Blog."""

    user_profile = models.ForeignKey(
        UserProfile,
        related_name='questions_for_user_profile')

    question = models.TextField(
        verbose_name='Question')

    votes = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name='Votes')

    def __unicode__(self):
        """Method displays the question field in admin view."""
        return self.question


class QuestionComments(models.Model):
    """Model to save the comments on questions posted in blog."""

    user_profile = models.ForeignKey(
        UserProfile,
        related_name='question_comments_for_user_profile')

    questions = models.ForeignKey(
        Questions,
        related_name='question_comments_for_Questions_table')

    comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Question Comments')

    def __unicode__(self):
        """Method displays the comments field in admin view."""
        return self.comments


class Answers(models.Model):
    """Model to save the Answers to the questions posted in Blog."""

    user_profile = models.ForeignKey(
        UserProfile,
        related_name='answers_for_user_profile')

    questions = models.ForeignKey(
        Questions,
        related_name='answers_for_Questions_table')

    answer = models.TextField(
        blank=True,
        null=True,
        verbose_name='Answer')

    votes = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name='Votes')

    def __unicode__(self):
        """Method displays the answer field in admin view."""
        return self.answer


class AnswerComments(models.Model):
    """Model to save comments on Answers to a question in Blog."""

    user_profile = models.ForeignKey(
        UserProfile,
        related_name='answers_comments_for_user_profile')

    answers = models.ForeignKey(
        Answers,
        related_name='answers_comments_for_Answers_table')

    comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Answer Comments')

    def __unicode__(self):
        """Method displays the comments field in admin view."""
        return self.comments
