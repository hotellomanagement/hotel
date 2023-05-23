from django.urls import path
from myapp import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
path('home/',views.homeview.as_view()),
path('about/',views.aboutview.as_view()),

path('service/',views.serviceview.as_view()),
path('boot/',views.bootview.as_view()),
path('temp/',views.tempview.as_view()),
path('renovat/',views.renovatview.as_view()),
path('form/',views.formview.as_view()),
path('hotelmanagement/',views.hotelmanagementview.as_view()),
path('contact/',views.contactview.as_view()),
path('insertcontact/',views.insertcontact),
path('blog/',views.blogview),
path('blogdetail/<int:id>',views.blogdetail),
path('faq/',views.faqsview),
path('signup/',views.signupview),
path('login/',LoginView.as_view(),name="login"),
path('logout/',LogoutView.as_view(),name="logout"),
path('gallary/',views.gallaryview.as_view()),
path('Room/',views.Roomview),
path('Roomdetail/<int:id>',views.Roomdetail),
path('insertcustomer/',views.insertcustomer),
path('customer/',views.customerview),

path('insertbooking/',views.insertbooking),
path('booking/',views.bookingview),

path('insertsubscribe/',views.insertsubcribe),


path('viewbookings/',views.viewbookingsview),
path('paybooking/<int:id>',views.paybooking,name="pay_booking"),

 path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]



