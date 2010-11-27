# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings

from models import Reservation, Restaurant


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation 
