from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm

def home(request):
	if request.method == "POST":
		data = StudentForm(request.POST)
		if data.is_valid():
			data.save()
			msg = "record created "
			fm = StudentForm()
			return render(request,"home.html",{"msg":msg,"fm":fm})
		else:
			msg = "check errors"
			return render(request,"home.html",{"msg":msg,"fm":data})
	else:
		fm = StudentForm()
		return render(request,"home.html",{"fm":fm})