from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import scmapp
from scmapp.models import User, Admin, Event, Book_ground
import datetime
from django.core.paginator import Paginator

from .filters import OrderFilter
import SCM

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# User Registration / Login Page


def rphome(request):
    if 'uname' in request.session:

        if request.method == "POST":
            name = request.POST.get('name')
            amount = 50000
            client = SCM.Client(
                auth=("rzp_test_U68XoHD9LUi8r6", "qshoen3NYzYQa1ijYv2rwWQA"))
            payment = client.order.create(
                {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        return render(request, 'index.html')
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'registration.html', context=data)


@csrf_exempt
def success(request):
    if 'uname' in request.session:
        return render(request, "success.html")


def index(request):
    return render(request, 'registration.html')


def base(request):
    return render(request, 'base.html')


def base2(request):
    return render(request, 'base2.html')


def rpbase(request):
    return render(request, 'rpbase.html')


def admintablepagination(request):
    if 'aname' in request.session:
        event = Event.objects.all()

        paginator = Paginator(event, 10)
        page_number = request.GET.get('page')
        event = paginator.get_page(page_number)

        data = {'event': event}
        return render(request, 'admin_list4pagination.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'registration.html', context=data)


def tablepagination(request):
    if 'uname' in request.session:
        event = Event.objects.all()

        paginator = Paginator(event, 10)
        page_number = request.GET.get('page')
        event = paginator.get_page(page_number)

        data = {'event': event}
        return render(request, 'user_list4pagination.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'registration.html', context=data)


# User Home Page


def user_home(request):
    if 'uname' in request.session:
        data = {'name': request.session.get('uname')}

        if 'book_status' in request.session:
            data['status'] = request.session['book_status']

        return render(request, 'user_home.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'registration.html', context=data)

# User Event Page


def user_event(request):
    if 'uname' in request.session:
        event = Event.objects.all()

        myFilter = OrderFilter(request.GET, queryset=event)
        events = myFilter.qs

        paginator = Paginator(event, 10)
        page_number = request.GET.get('page')
        event = paginator.get_page(page_number)

        data = {'event': event, 'events': events,
                'myFilter': myFilter}
        return render(request, 'user_event.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'registration.html', context=data)

# User Ground Booking Page


def ground_booking(request):
    if 'uname' in request.session:
        data = {'start_date': datetime.date.today()}
        return render(request, 'ground_booking.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'registration.html', context=data)

# User Logout


def user_logout(request):
    if 'uname' in request.session:
        del request.session['uname']

    if 'book_status' in request.session:
        del request.session['book_status']

    return render(request, 'registration.html')

# Admin Login Page


def admin_login(request):
    return render(request, 'admin_login.html')

# Admin Home Page


def admin_home(request):
    if 'aname' in request.session:
        data = {'name': request.session.get('aname')}
        return render(request, 'admin_home.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'admin_login.html', context=data)

# Admin View Bookings


def admin_booking(request):
    if 'aname' in request.session:
        booking = Book_ground.objects.all()
        data = {'booking': booking}
        return render(request, 'admin_booking.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'admin_login.html', context=data)

# Admin Manage Event Page


def admin_event(request):
    if 'aname' in request.session:
        event = Event.objects.all()

        myFilter = OrderFilter(request.GET, queryset=event)
        events = myFilter.qs

        paginator = Paginator(event, 10)
        page_number = request.GET.get('page')
        event = paginator.get_page(page_number)

        data = {'event': event, 'events': events,
                'myFilter': myFilter}
        return render(request, 'admin_event.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'admin_login.html', context=data)

# Admin Update Event Page


def update_event(request, id):
    if 'aname' in request.session:
        event = Event.objects.get(eid=id)
        event.start_date = event.start_date.strftime('%Y-%m-%d')

        data = {'event': event}
        return render(request, 'update_event.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'admin_login.html', context=data)

# Admin Add Event Page


def add_event(request):
    if 'aname' in request.session:
        return render(request, 'add_event.html')
    else:
        return HttpResponse('Something went wrong')

# Admin Logout


def admin_logout(request):
    if 'aname' in request.session:
        del request.session['aname']

    if 'event_status' in request.session:
        del request.session['event_status']

    return render(request, 'admin_login.html')

# BACKEND -> For User Registration


def test(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')

        if(password == re_password):
            user = User(name=name, email=email,
                        gender=gender, password=password)
            user.save()
            request.session['uname'] = name
            return user_home(request)
        else:
            data = {'status': "Password and Re-entered password must be same"}
            return render(request, 'registration.html', context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

# BACKEND -> For User Login


def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)

            if user.password == password:
                request.session['uname'] = name
                return user_home(request)
            else:
                data = {'status': "Incorrect Password!!!"}
                return render(request, 'registration.html', context=data)

        except Exception as e:
            data = {'status': "User does not exists! You have to register first."}
            return render(request, 'registration.html', context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

# BACKEND -> For Admin Login


def login_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Admin.objects.get(name=name)

            if user.password == password:
                request.session['aname'] = name
                # return HttpResponse('ffaf')
                return admin_home(request)
            else:
                data = {'status': "Incorrect Password!!!"}
                return render(request, 'admin_login.html', context=data)

        except Exception as e:
            data = {'status': "Invalid Username"}
            return render(request, 'admin_login.html', context=data)
    else:
        return HttpResponse("Something went wrong faffsffa!!!!!")

# BACKEND -> For Ground Booking


def db_ground_booking(request):
    if request.method == 'POST':

        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        paid = request.POST.get('paid')
        category = request.POST.get('category')

        try:
            image = request.FILES['image']
        except:
            image = f'media/default.jpg'
        published = request.POST.get('published')

        try:
            book = Book_ground.objects.get(start_date=start_date)
            data = {'status': 'Please select other date'}
            return render(request, 'ground_booking.html', context=data)
        except Exception as e:
            user = User.objects.get(name=request.session['uname'])
            book = Book_ground(uid=user.uid, name=user.name, start_date=start_date, end_date=end_date, title=title,
                               description=description, location=location, paid=paid, image=image, published=published, category=category)
            book.save()
            request.session['book_status'] = "Booking successful"
            return user_home(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

# BACKEND -> For Update Event


def db_update_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(eid=id)
        event.name = request.POST.get('name')
        event.start_date = request.POST.get('start_date')
        event.end_date = request.POST.get('end_date')
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.location = request.POST.get('location')
        event.paid = request.POST.get('paid')
        event.published = request.POST.get('published')
        event.category = request.POST.get('category')
        try:
            event.image = request.FILES['image']

        except:
            pass
        event.save()
        request.session['event_status'] = 'Event updated successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

# BACKEND -> For Delete Events


def db_delete_event(request, id):
    if request.method == 'GET':
        event = Event.objects.get(eid=id)
        event.delete()

        request.session['event_status'] = 'Event deleted successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

# BACKEND -> For Add Event


def db_add_event(request):
    if request.method == 'POST':

        posts = Event.objects.all()

        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        paid = request.POST.get('paid')
        try:
            image = request.FILES['image']
        except:
            image = f'media/default.jpg'
        published = request.POST.get('published')
        category = request.POST.get('category')

        event = Event(name=name, start_date=start_date, end_date=end_date, title=title,
                      description=description, location=location, paid=paid, image=image, published=published, category=category)
        context = {"posts": posts}
        event.save()
        request.session['event_status'] = 'Event added successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")
