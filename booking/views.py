from django.shortcuts import render
from django.http import HttpResponse
from . models import movie,ticket
from datetime import datetime

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
    id=obj.id
    return render(requests,'booked.html',{'obj':obj})
