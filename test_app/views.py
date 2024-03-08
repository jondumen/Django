from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	my_context = {'username': 'Hana dice Hola desde Views.py', 
			   'ifav1': 'Hatsune Miku 💙', 
			   'ifav2': 'Hardware y Software', 
			   'ifav3': 'Videojuegos'}
	return render(request, 'test_app/index.html', context=my_context)
	#return HttpResponse("Miku Miku, You Can Call Me Miku, Blue Hair Blue Tie, Hiden in Your Wi-Fi")