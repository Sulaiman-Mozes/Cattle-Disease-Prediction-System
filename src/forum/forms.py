from django import forms
from django.forms import ModelForm
from .models import Question, Answer


class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = [
		'title',
		'question',
		'image',
	]


class AnswerForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = [
		'answer'
	]
