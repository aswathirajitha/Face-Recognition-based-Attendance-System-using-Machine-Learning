from django.urls import path
from webapp import views

urlpatterns=[
    path('',views.about,name='about'),
    path('login.html',views.login,name='login'),
    path('stlogin.html',views.stlogin,name='stlogin'),
    path('register.html',views.register,name='register'),
    path('home.html',views.home,name='home'),
    path('sthome.html',views.sthome,name='sthome'),
    path('details.html',views.addstudents,name='detail'),
    path('simple_function',views.simple_function,name='simple_function'),
    path('leave.html',views.leaves,name='leave'),
    path('att.html',views.readfile,name='readfile'),
    path('attendance.html',views.attendview,name='attendview'),
    path('delete_item/<int:myid>/',views.delete_item, name='delete_item'),
    path('leave_view.html',views.leave_view,name='leave_view'),
    path('edit_item/<int:myid>/',views.edit_item, name='edit_item'),
    path('update_item/<int:myid>/',views.update_item, name='update_item'),
    path('verify.html',views.verify,name='verify'),
    path('display.html',views.display_att,name='disp'),
    path('att_view.html/',views.single_view,name='att_view'),
]

