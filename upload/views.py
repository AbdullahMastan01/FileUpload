from django.shortcuts import render
from .forms import uploadForm 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .readFile import process

def uploadedFile(request):
	if request.method == 'POST':
		file = request.FILES['uploaded_file']
		print(file.name, file.size)
		fss = FileSystemStorage()
		fss.save(file.name, file)
		process(file.name)
		return HttpResponse("File uploaded successfuly") 
	return	render(request, 'upload/home.html', {})	
