from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'News'

	def __str__(self):
		return self.text

class Feedback(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	class Meta:
		verbose_name_plural = 'Feedbacks'

	def __str__(self):
		return self.title

class Tools(models.Model):
	name = models.CharField(max_length=200)
	link = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Tools'

	def __str__(self):
		return self.name

class Software(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Softwares'

	def __str__(self):
		return self.name

class Version(models.Model):
	software = models.ForeignKey(Software,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	link = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Versions'

	def __str__(self):
		return self.name

class Message(models.Model):
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	touser = models.CharField(max_length=200)
	owner = models.ForeignKey(User)

	class Meta:
		verbose_name_plural = 'Messages'

	def __str__(self):
		return self.text