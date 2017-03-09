from django.shortcuts import render




def index(request):
	data = {'mydata': "Hello there, it's me again, the computer."}
	return render(request, 'blog/index.html',data)
