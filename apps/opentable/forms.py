# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings

from models import Reservation, Restaurant


NUM_PEOPLE = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),   
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),

)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation 
        exclude = ('notified',) 
        widgets = { 
            'num_people': forms.Select(choices=NUM_PEOPLE)    
        }
