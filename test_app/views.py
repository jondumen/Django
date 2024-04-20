from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import uwu

# Create your views here.
def index(request):
	uwu_team = uwu.objects.order_by('f_name')
	my_context = {'username': 'Hana dice Hola desde Views.py', 
			   'ifav1': 'Hatsune Miku 💙', 
			   'ifav2': 'Hardware y Software', 
			   'ifav3': 'Videojuegos',
			   'uwu': uwu_team}
	return render(request, 'test_app/index.html', context=my_context)
	#return HttpResponse("Miku Miku, You Can Call Me Miku, Blue Hair Blue Tie, Hiden in Your Wi-Fi")
 
