from django import forms
from .models import Feedback, Message

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ['title','text']
		labels = {'title': '反馈标题', 'text': '反馈内容'}

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['touser','text']
		labels = {'touser': '发给（用户名）','text': '短信息内容'}