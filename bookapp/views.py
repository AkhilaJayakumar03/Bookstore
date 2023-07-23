import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

# Create your views here.
def index(request):
    return render(request,"index.html")

class register(generic.CreateView):
    form_class = regform
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class login(generic.View):
    form_class = logform
    template_name = 'login.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        if request.method == 'POST':
            a = logform(request.POST)
            if a.is_valid():
                un = a.cleaned_data['username']
                ps = a.cleaned_data['password']
                request.session['username'] = un
                b = User.objects.all()
                for i in b:
                    if un == i.username and ps == i.password:
                        return redirect(userprofile)
                else:
                    return HttpResponse("Login Failed")
            else:
                return HttpResponse("Invalid Credentials")

def userprofile(request):
    username=request.session['username']
    return render(request, "userprofile.html",{'username':username})

class bookupload(generic.CreateView):
    form_class=bookupform
    template_name="bookupload.html"
    success_url= reverse_lazy('bookupload')
    def get(self, request):
        a =bookupmodel.objects.all()
        img = []
        nm = []
        uid = []
        fl = []
        ath = []
        dt = []
        for i in a:
            bookname = i.bookname
            nm.append(bookname)
            date = i.date
            dt.append(date)
            author = i.author
            ath.append(author)
            id = i.id
            uid.append(id)
            bookimage = i.bookimage
            img.append(str(bookimage).split('/')[-1])
            bookpdf = i.bookpdf
            fl.append(str(bookpdf).split('/')[-1])
        mylist = zip(nm, ath, dt, img, fl,uid)
        return render(request,self.template_name,{'mylist': mylist})

class home(generic.CreateView):
    form_class=bookupform
    template_name="home.html"
    success_url= reverse_lazy('home')
    def get(self, request):
        a =bookupmodel.objects.all()
        img = []
        nm = []
        uid = []
        ath = []
        fl=[]
        for i in a:
            bookname = i.bookname
            nm.append(bookname)
            author = i.author
            ath.append(author)
            id = i.id
            uid.append(id)
            bookimage = i.bookimage
            img.append(str(bookimage).split('/')[-1])
            bookpdf = i.bookpdf
            fl.append(str(bookpdf).split('/')[-1])
        mylist = zip(nm, ath,img,fl,uid)
        return render(request,self.template_name,{'mylist': mylist})


class bookdelete(generic.DeleteView):
    model = bookupmodel
    template_name = 'bookdelete.html'
    success_url = reverse_lazy('bookupload')

class bookupdate(generic.UpdateView):
    model=bookupmodel
    template_name='bookupdate.html'
    fields='__all__'
    form_class=bookupform
    def get(self,request,**kwargs):
        id1 = kwargs.get('pk')
        a = self.model.objects.get(id=id1)
        name=a.bookname
        author=a.author
        pdf= str(a.bookpdf).split('/')[-1]
        image = str(a.bookimage).split('/')[-1]
        return render(request,'bookupdate.html',{'name':name,'image':image,'author':author,'pdf':pdf})
    def post(self,request,**kwargs):
        id1=kwargs.get('pk')
        a = self.model.objects.get(id=id1)
        if request.method=='POST':
            if len(request.FILES)!=0:
                if len(a.bookimage) > 0:
                    os.remove(a.bookimage.path)
                a.bookimage = request.FILES['bookimage']
                if len(a.bookpdf) > 0:
                    os.remove(a.bookpdf.path)
                a.bookpdf = request.FILES['bookpdf']
            a.bookname = request.POST.get('bookname')
            a.author = request.POST.get('author')
            a.save()
            return redirect('http://127.0.0.1:8000/bookapp/bookupload')

class bookdownload(generic.ListView):
    model = bookupmodel
    template_name = 'bookdownload.html'
    def get(self, request):
        a = self.model.objects.all()
        pdf = []
        name = []
        for i in a:
            fl = str(i.bookpdf).split('/')[-1]
            pdf.append(fl)
            nm = i.bookname
            name.append(nm)
        mylist = zip(pdf, name)
        return render(request, self.template_name, {'mylist': mylist})


class lgview(LogoutView):
    next_page = reverse_lazy('login') #url name

