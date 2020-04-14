from django.urls import path
from . import views

urlpatterns = [

    path('hello/', views.hello), # Put a / after your input, this is a good habit
    # Also put a comma after each path to create a new path

    path('', views.home, name='home'), # This says that if nothing is entered after the main 
    #address, '', then the response should be the function views which we made to 
    #send a small message
     
    path('count/', views.count, name='count'), # This name = 'count' parameter that 
    #we created is what is going to link the input of pressing the button to the 
    #output of going to cound.html. Without this, the program would have to have 
    #exactly the input of 'count' in order to move on which in this case is not a 
    #problem, but could be in a different applicaiton. 

    path('what/', views.what),

    path('secret/', views.secret, name='secret'),

    path('about/', views.about, name='about'),
    
]

