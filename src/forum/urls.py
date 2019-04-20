from django.conf.urls import url, include
from .views import QuestionListView, QuestionCreateView, QuestionUpdateView, post_detail, AnswerUpdateView

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='list'),
    url(r'^post/$', QuestionCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', post_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', QuestionUpdateView, name='update'),
    url(r'^(?P<pk>[0-9]+)/edit/comment/$', AnswerUpdateView, name='updateAnswer'),
]
