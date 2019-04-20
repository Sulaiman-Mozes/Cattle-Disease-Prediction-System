from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


class QuestionCreateView(LoginRequiredMixin, CreateView):
	form_class = QuestionForm
	template_name = 'forms.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(QuestionCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(QuestionCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Create New Topic'
		context['button'] = 'Submit'
		return context


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
	form_class = QuestionForm
	template_name = 'forms.html'
	#success_url = '/forum/'

	def get_queryset(self):
		return Question.objects.filter(owner=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(QuestionUpdateView, self).get_context_data(*args, **kwargs)
		context['button'] = 'Update'
		return context


class QuestionListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Question.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(QuestionListView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		item_exists = Question.objects.all().exists()
		qs = Question.objects.all().search(query)
		if item_exists and qs.exists():
			context['search'] = qs
		return context
	

def post_detail(request, pk=None):
	template_name = "forum/question_detail.html"
	instance = get_object_or_404(Question, pk = pk)
	content_type = ContentType.objects.get_for_model(instance.__class__)
	obj_id = instance.id

	initial_data = {
			"content_type": content_type,
			"object_id": instance.id
	}
	form = AnswerForm(request.POST or None, initial = initial_data)
	if form.is_valid():
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		instance = Answer.objects.all()
		instance = form.save(commit=False)
		instance.owner = request.user
		instance.object_id = obj_id
		instance.content_type = content_type
		instance.answer = form.cleaned_data.get("answer")
		new_comment, created = Answer.objects.get_or_create(
							owner = instance.owner,
							content_type= instance.content_type,
							object_id = instance.object_id,
							answer = instance.answer
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments = Answer.objects.filter(content_type = content_type, object_id = obj_id)
	context = {
		"object": instance,
		"content_type": content_type,
		"comments": comments,
		"comment_form":form,
	}
	return render(request, template_name, context)


class AnswerUpdateView(LoginRequiredMixin, UpdateView):
	form_class = AnswerForm
	template_name = 'forms.html'
	#success_url = '/forum/'

	def get_queryset(self, ContentType):
		return Answer.objects.filter(owner=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(AnswerUpdateView, self).get_context_data(*args, **kwargs)
		context['button'] = 'Update'
		return context

