from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    """Марка автомобіля (Toyota, BMW, Mercedes)"""
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Car brand name"
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}"

class Model(models.Model):
    """Модель автомобіля (Camry, 3 Series, C-Class)"""
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='models'
    )
    year_from = models.IntegerField(help_text="Production year from")
    year_to = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"
        unique_together = ['name', 'brand']
    
    def __str__(self):
        return f"{self.brand.name} {self.name}"
    

class Car(models.Model):
    """Автомобіль користувача"""
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    year = models.IntegerField(
        help_text="Year of manufacture"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    description = models.TextField(blank=True)
    license_plate = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )
    vin = models.CharField(
        max_length=17,
        unique=True,
        null=True,
        blank=True,
        help_text="Vehicle Identification Number"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['owner', '-created_at']),
            models.Index(fields=['license_plate']),
        ]
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.owner}"
    
    def get_age(self):
        """Вік машини"""
        from datetime import datetime
        return datetime.now().year - self.year
    