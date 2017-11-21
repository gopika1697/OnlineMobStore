from django.http import Http404
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,get_object_or_404,redirect
from .models import Company,Oneplus,Xiaomi,Samsung,Apple,Address
from .models import Cart,Lenovo,Asus,Motorola,Google,Sony,LG,Queryget,Orders
from .forms import UserForm,AddressForm,UpdateForm
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from  django.views.decorators.gzip import gzip_page
from django.db import IntegrityError
#from django.views.decorators.cache import cache_control
import re

flag=0
def index(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        query=request.GET.get('q',None)
        if query == None:
            all_companies= Company.objects.all()
            return render(request,'devices/index.html',{'all_companies':all_companies})
        else:
            opquery=re.match(r'one[a-z0-9 ]*|op[a-z0-9 ]*',query,re.I)
            miquery=re.match(r'mi[a-z0-9 ]*|xi[a-z0-9 ]*|redmi[a-z0-9 ]*',query,re.I)
            ssquery=re.match(r'sam[a-z0-9 ]*|gala[a-z0-9 ]*|note[a-z0-9 ]*',query,re.I)
            apquery=re.match(r'app[a-z0-9 ]*|ip[a-z0-9 ]*|iw[a-z0-9 ]*',query,re.I)
            lenquery=re.match(r'len[a-z0-9 ]*|yoga[a-z0-9 ]*',query,re.I)
            motoquery=re.match(r'moto[a-z0-9 ]*|nexus[ ]*6',query,re.I)
            asquery=re.match(r'as[a-z0-9 ]*|zen[a-z0-9 ]*|nexus[ ]*7',query,re.I)
            pixquery=re.match(r'pix[a-z0-9 ]*|goo[a-z0-9 ]*',query,re.I)
            sonyquery=re.match(r'son[a-z0-9 ]*|xpe[a-z0-9 ]*',query,re.I)
            lgquery=re.match(r'lg[a-z0-9 ]*|nexus[ ]*[45][x]?[ a-z0-9]*|v[0-9 ]*',query,re.I)
            if opquery:
                print(opquery.group())
                return redirect('devices:liop')
            elif miquery:
                print(miquery.group())
                all_mis=Xiaomi.objects.all()
                return render(request,'devices/xiaomi.html',{'all_mis':all_mis})
            elif ssquery:
                print(ssquery.group())
                all_sss=Samsung.objects.all()
                return render(request,'devices/samsung.html',{'all_sss':all_sss})
            elif apquery:
                print(apquery.group())
                all_aps=Apple.objects.all()
                return render(request,'devices/apple.html',{'all_aps':all_aps})
            elif lenquery:
                print(lenquery.group())
                all_lens=Lenovo.objects.all()
                return render(request,'devices/lenovo.html',{'all_lens':all_lens})
            elif motoquery:
                print(motoquery.group())
                all_mos=Motorola.objects.all()
                return render(request,'devices/moto.html',{'all_mos':all_mos})
            elif asquery:
                print(asquery.group())
                all_ass=Asus.objects.all()
                return render(request,'devices/asus.html',{'all_ass':all_ass})
            elif pixquery:
                print(pixquery.group())
                all_gos=Google.objects.all()
                return render(request,'devices/google.html',{'all_gos':all_gos})
            elif sonyquery:
                print(sonyquery.group())
                all_sons=Sony.objects.all()
                return render(request,'devices/sony.html',{'all_sons':all_sons})
            elif lgquery:
                print(lgquery.group())
                all_lgs=LG.objects.all()
                return render(request,'devices/lg.html',{'all_lgs':all_lgs})
            else:
                return render(request,'devices/invalid.html', {'query':query})

def homeres(request):
    return render(request,'devices/homeres.html')
def about_us(request):
    return render(request,'devices/aboutus.html',{'flag':flag})


@gzip_page
def home(request):
    global flag
    print('flag=',flag)
    if flag :
        return redirect('devices:homeres')
    queryn=request.GET.get('Name',None)
    querye=request.GET.get('Email',None)
    querys=request.GET.get('Subject',None)
    querym=request.GET.get('Message',None)
    if querym==None or queryn==None or querye==None or querys==None :
        return render(request,'devices/home.html')
    else :
        flag=1
        print(querym)
        query1=Queryget()
        query1.name=queryn
        query1.email=querye
        query1.message=querym
        query1.subj=querys
        query1.save()
        emails=EmailMessage(
        'Superstore query',
        'Query sent by : '+queryn+'\nSender\'s mail-id : '+querye+'\nSubject : '+querys+'\nMessage : '+querym,
        to=['rageapocalypse9@gmail.com']
        )
        print('query sent')
        emails.send()

        return redirect('devices:homeres')

def outofstock(request,comp_name,model_name):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        if request.user.is_superuser and request.user.is_staff:
                return render(request,'devices/outofstock1.html',{'comp_name':comp_name,'model_name':model_name})

        return render(request,'devices/outofstock.html',{'comp_name':comp_name,'model_name':model_name})

def placeorder(request,comp_name,model_name):
    print('order placed')
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        try:
            order=Orders()
            order.model_name=model_name
            company=Company.objects.get(name=comp_name)
            order.company_id=company.id
            order.save()
        except IntegrityError as e:
            return render(request,'devices/orderexists.html')
        return redirect('devices:index')

def liop(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        print('yes')
        all_ops=Oneplus.objects.all()
        return render(request,'devices/oneplus.html',{'all_ops':all_ops})

def opde(request,op_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        oneplus=get_object_or_404(Oneplus,pk=op_id)
        return render(request,'devices/opde.html',{'oneplus':oneplus})
def opbuy(request,op_id):
    addindex=1
    cart=Cart.objects.get(user_name=request.user.username)
    oneplus=get_object_or_404(Oneplus,pk=op_id)
    if not cart.item1:
        cart.item1=oneplus.model_name
        cart.price1=oneplus.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=oneplus.model_name
        cart.price2=oneplus.price
        cart.qt2=1
        addindex=2
    elif not cart.item3:
        cart.item3=oneplus.model_name
        cart.price3=oneplus.price
        cart.qt3=1
        addindex=3
    else :
        cart.item1=oneplus.model_name
        cart.price1=oneplus.price
        cart.qt1=1
    if oneplus.stock<=0:
        return redirect('devices:outofstock','Oneplus',oneplus.model_name)
    cart.save()
    oneplus.stock-=1
    oneplus.save()
    return redirect('devices:cartdetails')


def limi(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_mis=Xiaomi.objects.all()
        return render(request,'devices/xiaomi.html',{'all_mis':all_mis})
def mide(request,mi_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        xiaomi=get_object_or_404(Xiaomi,pk=mi_id)
        return render(request,'devices/mide.html',{'xiaomi':xiaomi})
def mibuy(request,mi_id):
    cart=Cart.objects.get(user_name=request.user.username)
    xiaomi=get_object_or_404(Xiaomi,pk=mi_id)
    if not cart.item1:
        cart.item1=xiaomi.model_name
        cart.price1=xiaomi.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=xiaomi.model_name
        cart.price2=xiaomi.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=xiaomi.model_name
        cart.price3=xiaomi.price
        cart.qt3=1
    else :
        cart.item1=xiaomi.model_name
        cart.price1=xiaomi.price
        cart.qt1=1
    if xiaomi.stock<=0:
        return redirect('devices:outofstock','Xiaomi',xiaomi.model_name)
    cart.save()
    xiaomi.stock-=1
    xiaomi.save()
    return redirect('devices:cartdetails')


def liss(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_sss=Samsung.objects.all()
        return render(request,'devices/samsung.html',{'all_sss':all_sss})
def ssde(request,ss_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        samsung=get_object_or_404(Samsung,pk=ss_id)
        return render(request,'devices/ssde.html',{'samsung':samsung})
def ssbuy(request,ss_id):
    cart=Cart.objects.get(user_name=request.user.username)
    samsung=get_object_or_404(Samsung,pk=ss_id)
    if not cart.item1:
        cart.item1=samsung.model_name
        cart.price1=samsung.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=samsung.model_name
        cart.price2=samsung.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=samsung.model_name
        cart.price3=samsung.price
        cart.qt3=1
    else :
        cart.item1=samsung.model_name
        cart.price1=samsung.price
        cart.qt1=1
    if samsung.stock<=0:
        return redirect('devices:outofstock','Samsung',samsung.model_name)
    cart.save()
    samsung.stock-=1
    samsung.save()
    return redirect('devices:cartdetails')


def liap(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_aps=Apple.objects.all()
        return render(request,'devices/apple.html',{'all_aps':all_aps})
def apde(request,ap_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        apple=get_object_or_404(Apple,pk=ap_id)
        return render(request,'devices/apde.html',{'apple':apple})
def apbuy(request,ap_id):
    cart=Cart.objects.get(user_name=request.user.username)
    apple=get_object_or_404(Apple,pk=ap_id)
    if not cart.item1:
        cart.item1=apple.model_name
        cart.price1=apple.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=apple.model_name
        cart.price2=apple.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=apple.model_name
        cart.price3=apple.price
        cart.qt3=1
    else :
        cart.item1=apple.model_name
        cart.price1=apple.price
        cart.qt1=1
    if apple.stock<=0:
        return redirect('devices:outofstock','Apple',apple.model_name)
    cart.save()
    apple.stock-=1
    apple.save()
    return redirect('devices:cartdetails')


def lilen(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_lens=Lenovo.objects.all()
        return render(request,'devices/lenovo.html',{'all_lens':all_lens})
def lende(request,len_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        lenovo=get_object_or_404(Lenovo,pk=len_id)
        return render(request,'devices/lende.html',{'lenovo':lenovo})
def lenbuy(request,len_id):
    cart=Cart.objects.get(user_name=request.user.username)
    lenovo=get_object_or_404(Lenovo,pk=len_id)
    if not cart.item1:
        cart.item1=lenovo.model_name
        cart.price1=lenovo.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=lenovo.model_name
        cart.price2=lenovo.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=lenovo.model_name
        cart.price3=lenovo.price
        cart.qt3=1
    else :
        cart.item1=lenovo.model_name
        cart.price1=lenovo.price
        cart.qt1=1
    if lenovo.stock<=0:
        return redirect('devices:outofstock','Lenovo',lenovo.model_name)
    cart.save()
    lenovo.stock-=1
    lenovo.save()
    return redirect('devices:cartdetails')

def limo(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_mos=Motorola.objects.all()
        return render(request,'devices/moto.html',{'all_mos':all_mos})
def mode(request,mo_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        motorola=get_object_or_404(Motorola,pk=mo_id)
        return render(request,'devices/mode.html',{'motorola':motorola})
def mobuy(request,mo_id):
    cart=Cart.objects.get(user_name=request.user.username)
    motorola=get_object_or_404(Motorola,pk=mo_id)
    if not cart.item1:
        cart.item1=motorola.model_name
        cart.price1=motorola.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=motorola.model_name
        cart.price2=motorola.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=motorola.model_name
        cart.price3=motorola.price
        cart.qt3=1
    else :
        cart.item1=motorola.model_name
        cart.price1=motorola.price
        cart.qt1=1
    if motorola.stock<=0:
        return redirect('devices:outofstock','Motorola',motorola.model_name)
    cart.save()
    motorola.stock-=1
    motorola.save()
    return redirect('devices:cartdetails')

def lias(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_ass=Asus.objects.all()
        return render(request,'devices/asus.html',{'all_ass':all_ass})
def asde(request,as_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        asus=get_object_or_404(Asus,pk=as_id)
        return render(request,'devices/asde.html',{'asus':asus})
def asbuy(request,as_id):
    cart=Cart.objects.get(user_name=request.user.username)
    asus=get_object_or_404(Asus,pk=as_id)
    if not cart.item1:
        cart.item1=asus.model_name
        cart.price1=asus.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=asus.model_name
        cart.price2=asus.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=asus.model_name
        cart.price3=asus.price
        cart.qt3=1
    else :
        cart.item1=asus.model_name
        cart.price1=asus.price
        cart.qt1=1
    if asus.stock<=0:
        return redirect('devices:outofstock','Asus',asus.model_name)
    cart.save()
    asus.stock-=1
    asus.save()
    return redirect('devices:cartdetails')

def ligo(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_gos=Google.objects.all()
        return render(request,'devices/google.html',{'all_gos':all_gos})
def gode(request,go_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        google=get_object_or_404(Google,pk=go_id)
        return render(request,'devices/gode.html',{'google':google})
def gobuy(request,go_id):
    cart=Cart.objects.get(user_name=request.user.username)
    google=get_object_or_404(Google,pk=go_id)
    if not cart.item1:
        cart.item1=google.model_name
        cart.price1=google.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=google.model_name
        cart.price2=google.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=google.model_name
        cart.price3=google.price
        cart.qt3=1
    else :
        cart.item1=google.model_name
        cart.price1=google.price
        cart.qt1=1
    if google.stock<=0:
        return redirect('devices:outofstock','Google',google.model_name)
    cart.save()
    google.stock-=1
    google.save()
    return redirect('devices:cartdetails')


def lison(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_sons=Sony.objects.all()
        return render(request,'devices/sony.html',{'all_sons':all_sons})
def sonde(request,son_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        sony=get_object_or_404(Sony,pk=son_id)
        return render(request,'devices/sonde.html',{'sony':sony})
def sonbuy(request,son_id):
    cart=Cart.objects.get(user_name=request.user.username)
    sony=get_object_or_404(Sony,pk=son_id)
    if not cart.item1:
        cart.item1=sony.model_name
        cart.price1=sony.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=sony.model_name
        cart.price2=sony.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=sony.model_name
        cart.price3=sony.price
        cart.qt3=1
    else :
        cart.item1=sony.model_name
        cart.price1=sony.price
        cart.qt1=1
    if sony.stock<=0:
        return redirect('devices:outofstock','Sony',sony.model_name)
    cart.save()
    sony.stock-=1
    sony.save()
    return redirect('devices:cartdetails')

def lilg(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        all_lgs=LG.objects.all()
        return render(request,'devices/lg.html',{'all_lgs':all_lgs})
def lgde(request,lg_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        lg=get_object_or_404(LG,pk=lg_id)
        return render(request,'devices/lgde.html',{'lg':lg})
def lgbuy(request,lg_id):
    cart=Cart.objects.get(user_name=request.user.username)
    lg=get_object_or_404(LG,pk=lg_id)
    if not cart.item1:
        cart.item1=lg.model_name
        cart.price1=lg.price
        cart.qt1=1
    elif not cart.item2:
        cart.item2=lg.model_name
        cart.price2=lg.price
        cart.qt2=1
    elif not cart.item3:
        cart.item3=lg.model_name
        cart.price3=lg.price
        cart.qt3=1
    else :
        cart.item1=lg.model_name
        cart.price1=lg.price
        cart.qt1=1
    if lg.stock<=0:
        return redirect('devices:outofstock','LG',lg.model_name)
    cart.save()
    lg.stock-=1
    lg.save()
    return redirect('devices:cartdetails')


def detail(request,company_id):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        company=get_object_or_404(Company,pk=company_id)
        return render(request,'devices/detail.html',{'company':company})

def cartdetails(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        cart=Cart.objects.get(user_name=request.user.username)
        return render(request,'devices/cartdetails.html',{'cart':cart})

def delete1(request):
    cart=Cart.objects.get(user_name=request.user.username)
    cart.item1=None
    cart.qt1=1
    cart.price1=0
    cart.save()
    return redirect('devices:cartdetails')
def delete2(request):
    cart=Cart.objects.get(user_name=request.user.username)
    cart.item2=None
    cart.qt2=1
    cart.price2=0
    cart.save()
    return redirect('devices:cartdetails')
def delete3(request):
    cart=Cart.objects.get(user_name=request.user.username)
    cart.item3=None
    cart.qt3=1
    cart.price3=0
    cart.save()
    return redirect('devices:cartdetails')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                cart=Cart(user_name=request.user.username)
                cart.save()
                return redirect('devices:index')
        return render(request, 'devices/register.html', {'form':form})
    return render(request, 'devices/register.html', {'form':form})

def update(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        form = UpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            opassword = form.cleaned_data['old_password']
            npassword = form.cleaned_data['new_password']
            user = authenticate(username=request.user.username,password=opassword)
            print('authenticate sucess',request.user.username)
            if user is not None:
                user.set_password(npassword)
                user.save()
                login(request,user)
                print('set successful',request.user.username,npassword)
                return redirect('devices:index')
        print('not successful')
        return render(request, 'devices/update.html', {'form':form})

def login_user(request):
    if request.user.is_authenticated():
        print('yes')
        return redirect('devices:index')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('devices:index')
                else:
                    return render(request, 'devices/login.html', {'error_message': 'Your account has been disabled','flag':flag})
            else:
                return render(request, 'devices/login.html', {'error_message': 'Invalid login','flag':flag})
        return render(request, 'devices/login.html',{'flag':flag})

def mymap(request):
    return render(request, 'devices/mymap.html')

def mailsend(request):
    if not Address.objects.filter(user_name=request.user.username).exists():
        return redirect('devices:addressreg')
    else:
        cart=Cart.objects.get(user_name=request.user.username)
        cart.status1=cart.status2=cart.status3='Purchased'
        s=''
        if cart.item1:
            s+='Item : '+cart.item1+'\n'+'Qty : '+str(cart.qt1)+'\nPrice : ₹'+str(cart.price1)
        if cart.item2:
            s+='\n\nItem : '+cart.item2+'\n'+'Qty : '+str(cart.qt2)+'\nPrice : ₹'+str(cart.price2)
        if cart.item3:
            s+='\n\nItem : '+cart.item3+'\n'+'Qty : '+str(cart.qt3)+'\nPrice : ₹'+str(cart.price3)
        s+='\n\nTotal : ₹'+str(cart.total)+'\nStatus : '+cart.status1
        emails=EmailMessage(
        'Superstore reciept:',
        'Thanks for shopping with us!!!\nBill summary:\n\n'+s,
        to=[request.user.email,'adityapramod1212@gmail.com']
        )
        emails.send()
        cart.save()
        print('sent')
        return redirect('devices:logout_user')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'devices/login.html', context)

def addressreg(request):
    if not request.user.is_authenticated():
        print('no')
        return redirect('devices:login_user')
    else:
        if Address.objects.filter(user_name=request.user.username).exists():
            print('exits')
            return render(request,'devices/exists.html')
        else:
            form = AddressForm(request.POST or None)
            if form.is_valid():
                print(dict(request.POST),request.POST['contact'])
                addre = form.save(commit=False)
                if len(request.POST['contact'])<10:
                    return render(request,'devices/addressreg.html',{'error_messagecon': 'Enter correct contact info'})
                addre.user_name=request.user.username
                addre.save()
                if addre is not None:
                    print("yes ")
                    return redirect('devices:cartdetails')
                else:
                    print("not updated")
                    form=AddressForm()
                    return render(request,'devices/addressreg.html',{'error_message': 'Your account has been disabled'})
            else:
                print("not going")
                return render(request,'devices/addressreg.html',{'error_message': 'Enter Valid creditials'})
