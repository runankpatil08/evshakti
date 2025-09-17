from django.db import models
from django.core.exceptions import ValidationError


# ------------------------------
# EV Two-Wheeler Model
# ------------------------------
class ElectricTwoWheeler(models.Model):
    model_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    battery_capacity = models.DecimalField(max_digits=5, decimal_places=2, help_text="kWh")
    range_per_charge = models.PositiveIntegerField(help_text="Range in km")
    price = models.IntegerField()
    color = models.CharField(max_length=30)

    # Allow up to 3 images
    image1 = models.ImageField(upload_to="two_wheelers/", blank=True, null=True)
    image2 = models.ImageField(upload_to="two_wheelers/", blank=True, null=True)
    image3 = models.ImageField(upload_to="two_wheelers/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Custom validation: Max 3 images allowed"""
        images = [self.image1, self.image2, self.image3]
        filled_images = [img for img in images if img]
        if len(filled_images) > 3:
            raise ValidationError("You can upload a maximum of 3 images.")

    def __str__(self):
        return f"{self.company} {self.model_name}"

