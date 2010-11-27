from django.utils import simplejson
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.core.urlresolvers import reverse
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
    if request.POST:
        pass
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

