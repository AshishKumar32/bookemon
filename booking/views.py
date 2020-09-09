from django.shortcuts import render
from django.http import HttpResponse
from . models import movie,ticket,Profile
from django.contrib.auth.models import User
from datetime import datetime
from io import BytesIO
import base64

# Create your views here.
def home (requests):
    movies = movie.objects.all()
    return render(requests,'home.html',{'movies':movies})

def book (requests):
    movie1=requests.GET['movie']
    obj=movie.objects.get(name=movie1)
    arr=obj.booked
    return render(requests,'booking.html',{'seats':arr,'movie':movie1})

def bookticket(requests):
    seats=requests.POST['seatno']
    movie1=requests.POST['movie']
    username=requests.POST['username']
    phone=requests.POST['phone']

    seatarri1 = [int(x) for x in seats.split(',') if x]
    seatarr = [int(x)-1 for x in seats.split(',') if x]
    obj=movie.objects.get(name=movie1)
    length=len(seatarr)
    nos=obj.bookings
    nos=nos-length
    bookarr=obj.booked

    for i in seatarr:
        bookarr[i]=1

    movie.objects.filter(name=movie1).update(bookings=nos,booked=bookarr)
    
    book_time=datetime.now()
    ticket1 = ticket.objects.create(movie=movie1, book_time=book_time,user=username,phone=phone,nos=length,seats=seatarri1)
    obj= ticket.objects.get(movie=movie1, book_time=book_time,user=username,phone=phone,nos=length)
    username = None
    if requests.user.is_authenticated:
        user_id = requests.user.id
    user = User.objects.get(pk=user_id)
    user.profile.tickets.append(obj.id)
    user.save()
    id=obj.id
    seatqr= ""
    for i in seatarr:
        seatqr=seatqr+str(i)+","
    dataqr="id:"+str(id)+","+"movie:"+movie1+","+"seats:"+seatqr
    dataqr=dataqr.rstrip(',')
    print (dataqr)
    # qr.add_data(dataqr)
    # qr.make(fit=True)
    # img = qr.make_image(fill='black', back_color='white')

    # buffer = BytesIO()
    # img.save(buffer, format="PNG")
    # img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return render(requests,'booked.html',{'obj':obj,'my_qr_code': dataqr })

def test(requests):
    
    return render(requests,'search.html')

def search(requests):
    if requests.method == 'GET': # this will be GET now      
        movie_name =  requests.GET.get('keyword') # do some research what it does       
        try:
            movlist = movie.objects.filter(name__icontains=movie_name) # filter returns a list so you might consider skip except part
            return render(requests,"search.html",{"movies":movlist})
        except:
            return render(requests,"search.html",{'movies':movlist})
    else:
        return render(requests,"search.html",{})