from django import forms
from .models import ElectricTwoWheeler


# ------------------------------
# EV Two Wheeler Form
# ------------------------------
class ElectricTwoWheeler_form(forms.ModelForm):
    class Meta:
        model = ElectricTwoWheeler
        fields = "__all__"

