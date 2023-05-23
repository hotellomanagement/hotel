from django.urls import path
from myapp import views
urlpatterns=[
path('home/',views.homeview.as_view()),
]
<html>
    <head>
        <title>
            firstpage
        </title>
    </head>
    <body>
        <h1> welcome about</h1>
        <l--anchor,hyperlink reference-->
        <a href="/home/">click here for about page</a>    
        </body>
        </html>''''