from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, "age/Dob.html", )
	#else:
			#return redirect("/")

def age(request):
		if request.method=='POST' :
			year = int(request.POST['odun'])
			c_y = 2020
			age = c_y - year
		else:
			return redirect("/")
			if age == 20:
				messages.info(request, f"You are an adult")
		return render(request, 'age/result.html', {'result' : age} )
	

	    
#import datetime
#DOb = input('Enter Year:- ')
#Currentyear #=datetime.datetime.now#().year
#Age = Currentyear - int(DOb)
#print('Your Age is #{}'.format(Age))

