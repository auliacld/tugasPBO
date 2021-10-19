from django.shortcuts import render

def halamanbaru(request):
		return render(request,'login.php')

def halamanlainnya(request):
		return render(request,'halamanlainnya.html')