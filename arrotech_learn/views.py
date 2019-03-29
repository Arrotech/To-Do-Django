from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	"""Render home page."""
	if request.method == 'POST':
		return render(request, 'index.html', {'new_to_do': request.POST['Input']})
	return render(request, 'index.html')
