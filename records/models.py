from django.db import models

# Create your models here.
from pets.models import Pet

class Record(models.Model):
    """ペットの日々の記録"""
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='records')
    target_date = models.DateField()
    
    # 7つの記録項目
    pacing = models.IntegerField()
    reaction_to_sight = models.IntegerField()
    reaction_to_call = models.IntegerField()
    night_behavior = models.IntegerField()
    activity_level = models.IntegerField()
    toilet = models.IntegerField()
    appetite = models.IntegerField()
    
    # タイムスタンプ
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('pet', 'target_date')  # 複合ユニーク制約
    
    def __str__(self):
        return f"{self.pet.name} - {self.target_date}"