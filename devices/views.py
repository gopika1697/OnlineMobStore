from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Company,Oneplus,Xiaomi,Samsung,Apple

# Create your views here.
def index(request):
    all_companies= Company.objects.all()#get all albums
    #template=loader.get_template('music/index.html')#get html from templates folder in app
    #context={'all_albums':all_albums}
    return render(request,'devices/index.html',{'all_companies':all_companies})

def home(request):
    return render(request,'devices/home.html')


def liop(request):
    all_ops=Oneplus.objects.all()
    return render(request,'devices/oneplus.html',{'all_ops':all_ops})
def opde(request,op_id):
    oneplus=get_object_or_404(Oneplus,pk=op_id)
    return render(request,'devices/opde.html',{'oneplus':oneplus})

def limi(request):
    all_mis=Xiaomi.objects.all()
    return render(request,'devices/xiaomi.html',{'all_mis':all_mis})
def mide(request,mi_id):
    xiaomi=get_object_or_404(Xiaomi,pk=mi_id)
    return render(request,'devices/mide.html',{'xiaomi':xiaomi})

def liss(request):
    all_sss=Samsung.objects.all()
    return render(request,'devices/samsung.html',{'all_sss':all_sss})
def ssde(request,ss_id):
    samsung=get_object_or_404(Samsung,pk=ss_id)
    return render(request,'devices/ssde.html',{'samsung':samsung})

def liap(request):
    all_aps=Apple.objects.all()
    return render(request,'devices/apple.html',{'all_aps':all_aps})
def apde(request,ap_id):
    apple=get_object_or_404(Apple,pk=ap_id)
    return render(request,'devices/apde.html',{'apple':apple})


def detail(request,company_id):
    #return HttpResponse("<h2>detail of album id : "+str(album_id)+"</h2>")
    """try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")"""
    company=get_object_or_404(Company,pk=company_id)
    return render(request,'devices/detail.html',{'company':company})
