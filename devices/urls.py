from django.conf.urls import url
from . import views

app_name='devices'

urlpatterns = [
    #/devices/ ---homepage
    url(r'^$', views.index,name='index'),
    #/devices/home/
   url(r'^home/$',views.home,name='home'),
   #/devices/aboutus/
  url(r'^about_us/$',views.about_us,name='about_us'),
  #/devices/retpolicy/
 url(r'^retpolicy/$',views.returnpolicy,name='returnpolicy'),

 #/devices/support/
url(r'^support/$',views.support,name='support'),

   #/devices/homeres/
   url(r'^homeres/$',views.homeres,name='homeres'),
   #/devices/map/
  url(r'^map/$',views.mymap,name='mymap'),
   #/devices/mail/
  url(r'^mail/$',views.mailsend,name='mailsend'),

   #/devices/register/
   url(r'^register/$',views.register,name='register'),
    #/devices/update/
    url(r'^update/$',views.update,name='update'),

    #/devices/delitem/
    url(r'^delitem1/$',views.delete1,name='delete1'),
    #/devices/delitem/
    url(r'^delitem2/$',views.delete2,name='delete2'),
    #/devices/delitem/
    url(r'^delitem3/$',views.delete3,name='delete3'),

   #/devices/addressreg/
   url(r'^addressreg/$',views.addressreg,name='addressreg'),
    #/devices/login_user/
    url(r'^login_user/$',views.login_user,name='login_user'),
    #/devices/logout_user/
    url(r'^logout_user/$',views.logout_user,name='logout_user'),

    #/devices/oneplus/
    url(r'^oneplus/$',views.liop,name='liop'),
    #/devices/oneplus/1/
    url(r'^oneplus/(?P<op_id>[0-9]+)/$',views.opde,name='opde'),
    #/devices/oneplus/1/buy/
     url(r'^oneplus/(?P<op_id>[0-9]+)/buy/$',views.opbuy,name='opbuy'),
     #devices/outofstock/compname/modelname/
     url(r'^outofstock/(?P<comp_name>[A-Za-z0-9 ]+)/(?P<model_name>[A-Za-z0-9 ]+)/$',views.outofstock,name='outofstock'),
     #devices/placeorder/comp_name/model_name/
     url(r'^placeorder/(?P<comp_name>[A-Za-z0-9 ]+)/(?P<model_name>[A-Za-z0-9 ]+)/$',views.placeorder,name='placeorder'),
   #/devices/xiaomi/
   url(r'^xiaomi/$',views.limi,name='limi'),
   #/devices/xiaomi/1/
   url(r'^xiaomi/(?P<mi_id>[0-9]+)/$',views.mide,name='mide'),
   #/devices/xiaomi/1/buy/
    url(r'^xiaomi/(?P<mi_id>[0-9]+)/buy/$',views.mibuy,name='mibuy'),

   #/devices/samsung/
   url(r'^samsung/$',views.liss,name='liss'),
   #/devices/samsung/1/
   url(r'^samsung/(?P<ss_id>[0-9]+)/$',views.ssde,name='ssde'),
    #/devices/samsung/1/buy/
    url(r'^samsung/(?P<ss_id>[0-9]+)/buy/$',views.ssbuy,name='ssbuy'),

   #/devices/leonovo/
   url(r'^lenovo/$',views.lilen,name='lilen'),
   #/devices/lenovo/1/
   url(r'^lenovo/(?P<len_id>[0-9]+)/$',views.lende,name='lende'),
   #/devices/lenovo/1/buy/
    url(r'^lenovo/(?P<len_id>[0-9]+)/buy/$',views.lenbuy,name='lenbuy'),

 #/devices/google/
 url(r'^google/$',views.ligo,name='ligo'),
 #/devices/google/1/
 url(r'^google/(?P<go_id>[0-9]+)/$',views.gode,name='gode'),
 #/devices/google/1/buy/
  url(r'^google/(?P<go_id>[0-9]+)/buy/$',views.gobuy,name='gobuy'),

 #/devices/sony/
 url(r'^sony/$',views.lison,name='lison'),
 #/devices/sony/1/
 url(r'^sony/(?P<son_id>[0-9]+)/$',views.sonde,name='sonde'),
 #/devices/sony/1/buy/
  url(r'^sony/(?P<son_id>[0-9]+)/buy/$',views.sonbuy,name='sonbuy'),


 #/devices/apple/
 url(r'^apple/$',views.liap,name='liap'),
 #/devices/apple/1/
 url(r'^apple/(?P<ap_id>[0-9]+)/$',views.apde,name='apde'),
  #/devices/apple/1/buy/
  url(r'^apple/(?P<ap_id>[0-9]+)/buy/$',views.apbuy,name='apbuy'),

 #/devices/moto/
 url(r'^moto/$',views.limo,name='limo'),
 #/devices/moto/1/
 url(r'^moto/(?P<mo_id>[0-9]+)/$',views.mode,name='mode'),
  #/devices/moto/1/buy/
  url(r'^moto/(?P<mo_id>[0-9]+)/buy/$',views.mobuy,name='mobuy'),

  #/devices/lg/
  url(r'^lg/$',views.lilg,name='lilg'),
  #/devices/lg/1/
  url(r'^lg/(?P<lg_id>[0-9]+)/$',views.lgde,name='lgde'),
   #/devices/lg/1/buy/
   url(r'^lg/(?P<lg_id>[0-9]+)/buy/$',views.lgbuy,name='lgbuy'),


#/devices/asus/
url(r'^asus/$',views.lias,name='lias'),
#/devices/asus/1/
url(r'^asus/(?P<as_id>[0-9]+)/$',views.asde,name='asde'),
 #/devices/asus/1/buy/
 url(r'^asus/(?P<as_id>[0-9]+)/buy/$',views.asbuy,name='asbuy'),

    #/devices/cartdetails/
    url(r'^cartdetails/$',views.cartdetails,name='cartdetails'),
    #/music/712/----712-(album_id)
    url(r'^(?P<company_id>[0-9]+)/$',views.detail,name='detail'),

    #/music/<album_id/favorite/-----go to fav

]
