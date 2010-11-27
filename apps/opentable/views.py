from django.utils import simplejson
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.core.urlresolvers import reverse
from django import forms
from django.forms.util import ErrorList
from models import Restaurant
from forms import ReservationForm

def index(request):
    template_name = 'base.html'
    context = RequestContext(request)
    dict = {}
    dict['restaurants'] = Restaurant.objects.all().order_by('-num_reservations')[:8]
    dict['MAPS_ID'] = settings.GOOGLE_MAPS_ID
    return render_to_response(
        template_name,
        dict,
        context,
    )
    
def reservation(request, restaurant_id=None):
    template_name = 'reservation.html'
    context = RequestContext(request)
    dict = {}
    if restaurant_id:
        dict['restaurant'] = Restaurant.objects.get(pk=restaurant_id)
    if request.POST:
        if request.POST.get('cancel'):
            return HttpResponseRedirect(reverse('index'))
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user:
                reservation.user = request.user
            restaurant = reservation.restaurant
            restaurant.num_reservations += 1
            restaurant.lat = str(reservation.restaurant.lat)
            restaurant.lon = str(reservation.restaurant.lon)
            if restaurant.capacity - reservation.num_people < 0:
                form._errors['num_people'] = ErrorList([u"Unfortunately this restaurant doesn't like you and can't accomodate you.  Actually, they are just busy.  Try another time..."])
                dict['form'] = form
                if dict.get('restaurant'):
                    dict['form'].fields['restaurant'].widget = forms.HiddenInput()
                return render_to_response( template_name, dict, context, )
            else:
                restaurant.capacity -= reservation.num_people 
            restaurant.save()
            reservation.save()
            dict['msg'] = 'Thank you for your reservation.'
        else:
            dict['form'] = form
            if dict.get('restaurant'):
                dict['form'].fields['restaurant'].widget = forms.HiddenInput()
    else:
        if dict.get('restaurant'):
            dict['form'] = ReservationForm(initial={'restaurant':dict['restaurant']})
            dict['form'].fields['restaurant'].widget = forms.HiddenInput()
        else:
            dict['form'] = ReservationForm()
    return render_to_response(
        template_name,
        dict,
        context,
    )

def restaurants(request, restaurant_id=None):
    template_name = 'restaurants.html'
    context = RequestContext(request)
    dict = {}
    if restaurant_id:
        dict['restaurant'] = Restaurant.objects.get(pk=restaurant_id)
        template_name = 'restaurant.html'
    else:
        dict['restaurants'] = Restaurant.objects.all().order_by('name')
    return render_to_response(
        template_name,
        dict,
        context,
    )

