from django.utils import simplejson
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.core.urlresolvers import reverse
from django import forms
from models import Restaurant
from forms import ReservationForm

def index(request):
    template_name = 'base.html'
    context = RequestContext(request)
    dict = {}
    dict['restaurants'] = Restaurant.objects.all().order_by('-num_reservations')[:8]
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
                assert False, 'no mores room'
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

def restaurants(request):
    template_name = 'restaurants.html'
    context = RequestContext(request)
    dict = {}
    dict['restaurants'] = Restaurant.objects.all()
    return render_to_response(
        template_name,
        dict,
        context,
    )

