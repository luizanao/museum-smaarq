from django.shortcuts import render, get_object_or_404
from models import * 

def home(request, id):
	item = get_object_or_404(Collection, pk=id)

	return render(request,'index.html', context={'item':item})