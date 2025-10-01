from django import forms
from .models import ElectricTwoWheeler,Review


# ------------------------------
# EV Two Wheeler Form
# ------------------------------
class ElectricTwoWheeler_form(forms.ModelForm):
    class Meta:
        model = ElectricTwoWheeler
        fields = "__all__"




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "image"]
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Write your review..."}),
        }
