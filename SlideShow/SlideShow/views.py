from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):
	return render(request, 'SlideShow/home.html')


def logout_view(request):
	logout(request)
	return redirect(request.GET.get('next'))