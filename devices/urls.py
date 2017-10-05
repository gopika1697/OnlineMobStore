from django.conf.urls import url
from . import views

app_name='devices'

urlpatterns = [
    #/devices/ ---homepage
    url(r'^$', views.index,name='index'),
    #/devices/home/
   url(r'^home/$',views.home,name='home'),

    #/devices/oneplus/
    url(r'^oneplus/$',views.liop,name='liop'),
    #/devices/oneplus/1/
    url(r'^oneplus/(?P<op_id>[0-9]+)/$',views.opde,name='opde'),

   #/devices/xiaomi/
   url(r'^xiaomi/$',views.limi,name='limi'),
   #/devices/xiaomi/1/
   url(r'^xiaomi/(?P<mi_id>[0-9]+)/$',views.mide,name='mide'),

   #/devices/samsung/
   url(r'^samsung/$',views.liss,name='liss'),
   #/devices/samsung/1/
   url(r'^samsung/(?P<ss_id>[0-9]+)/$',views.ssde,name='ssde'),

 #/devices/apple/
 url(r'^apple/$',views.liap,name='liap'),
 #/devices/apple/1/
 url(r'^apple/(?P<ap_id>[0-9]+)/$',views.apde,name='apde'),


    #/music/712/----712-(album_id)
    url(r'^(?P<company_id>[0-9]+)/$',views.detail,name='detail'),

    #/music/<album_id/favorite/-----go to fav

]
