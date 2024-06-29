from django.shortcuts import render
from news.models import News,Contact
from .forms import DataFrom
from django.http import HttpResponse
# Create your views here.

def page_404(request):
    return render(request=request,template_name='pages/404.html')




def contact(request):
    print('--------34',request.POST)
    if request.method=='POST':
        data=request.POST
        form=DataFrom(data=data)
        print('--------->',form)
        if form.is_valid():
            print('-------->3',3)
            name=form.data['name']
            email=form.data['email']
            message=form.data['message']
            print('------->',data,message)
            contact=Contact(
                name=name,
                email=email,
                message=message,
            )
            contact.save()
            context={
                'message':'malumotlaringiz kiriltildi'
            }
            return render(request=request,template_name='pages/contact.html',context=context)
        
    return render(request=request,template_name='pages/contact.html')


def homeindex(request):
    news=News.published.get_queryset()
    print('--------->',news)
    news_list=News.objects.last()
    new_last=News.objects.last()

    context={
        'news':news,
        'news_one': news_list,
        'new_last':new_last
    }
    return render(request=request,template_name='index.html',context=context)



