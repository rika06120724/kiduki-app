from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pet(models.Model):
    """ペットモデル"""
    
    SEX_CHOICES = [
        (1, 'オス'),
        (2, 'メス'),
    ]
    
    SIZE_CHOICES = [
        (1, '小'),
        (2, '中'),
        (3, '大'),
    ]
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.IntegerField(choices=SEX_CHOICES)
    size = models.IntegerField(choices=SIZE_CHOICES)
    icon = models.ImageField(upload_to='pets/', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
