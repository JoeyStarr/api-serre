from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview),

    path('listpers/',views.getPers, name="list-person"),
    path('listcult/',views.getCult, name="list-culture"),
    path('listserre/',views.getSerre, name="list-serre"),

    path('setpers/',views.setPers, name="insert-person"),
    path('setcult/',views.setCult, name="insert-culture"),
    path('setserre/',views.setSerre, name="insert-serre"),

    path('uppers/<str:pk>',views.updPers, name="update-person"),
    path('upcult/<str:wrd>',views.updCult, name="update-culture"),
    path('upserre/<str:pk>',views.upSerre, name="update-serre-byId"),
    path('updserre/<str:wrd>',views.updSerre, name="update-serre-byHash"),

    path('dpers/<str:wrd>',views.ddayPers, name="detail-person"),
    path('dcult/<str:pk>',views.ddayCult, name="detail-culture"),
    path('dserre/<str:wrd>',views.ddaySerre, name="detail-serre"),

    path('delserre/<str:wrd>',views.delSerre, name="detail-serre"),
    

    path('seapers/<str:wrd>',views.seaPers, name="search-person"),
    path('seaserre/<str:wrd>',views.seaSerre, name="search-serre"),
]