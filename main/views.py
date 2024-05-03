from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import News, Software, Tools, Version, Feedback, Message
from .forms import FeedbackForm, MessageForm
from django.contrib.auth.decorators import login_required

def index(request):
	news = News.objects.order_by('date_added')
	context = {'news': news}
	return render(request, 'main/index.html', context)

def products(request):
	softwares = Software.objects.order_by('date_added')
	context = {'softwares': softwares}
	return render(request, 'main/products.html', context)

@login_required
def versions(request, product_id):
	software = Software.objects.get(id=product_id)
	versions = software.version_set.order_by('-date_added')
	context = {'software': software, 'versions': versions}
	return render(request, 'main/versions.html', context)

def functions(request):
	tools = Tools.objects.order_by('date_added')
	context = {'tools': tools}
	return render(request, 'main/functions.html', context)

@login_required
def feedback(request):
	feedback = Feedback.objects.order_by('date_added')
	if request.method != 'POST':
		form = FeedbackForm()
	else:
		form = FeedbackForm(request.POST)
		if form.is_valid():
			newform = form.save(commit=False)
			newform.owner = request.user
			newform.save()
			return HttpResponseRedirect(reverse('main:feedback'))
	context = {'feedback': feedback, 'form': form}
	return render(request, 'main/feedback.html', context)

@login_required
def message(request):
	message = Message.objects.order_by('date_added')
	if request.method != 'POST':
		form = MessageForm()
	else:
		form = MessageForm(request.POST)
		if form.is_valid():
			newform1 = form.save(commit=False)
			newform1.owner = request.user
			newform1.save()
			return HttpResponseRedirect(reverse('main:message'))
	context = {'message': message, 'form': form}
	return render(request, 'main/message.html', context)

def about(request):
	return render(request,'main/about.html')