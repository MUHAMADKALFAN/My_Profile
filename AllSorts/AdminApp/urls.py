from django.urls import path,include
from  . import views


urlpatterns = [
    path('Useradmin',views.Useradmin,name="Useradmin"),
    path('addmemento',views.addmemento,name="addmemento"),
    path('Viewachievements',views.Viewachievements,name="Viewachievements"),
    path('Momentofoms',views.Momentofoms,name="Momentofoms"),
    path('Momentoupdate/<int:id>',views.Momentoupdate,name="Momentoupdate"),
    path('Editmementos/<int:id>',views.Editmementos,name="Editmementos"),
    path('mementodelete/<int:id>',views.mementodelete,name="mementodelete"),
    path('viewcustomer',views.viewcustomer,name="viewcustomer"),
    path('customerdelete/<int:id>',views.customerdelete,name="customerdelete"),
    path('profile',views.profile,name="profile"),
    path('profileform',views.profileform,name="profileform"),
    path('Profilesettings',views.Profilesettings,name="Profilesettings"),
]
