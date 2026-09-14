from django import forms
from .models import Record

# 1-5スケールの選択肢
SCALE_CHOICES = [(i, i) for i in range(1, 6)]


class RecordFormStep1(forms.ModelForm):
    """Step 1/3：徘徊・姿への反応・名前への反応"""

    class Meta:
        model = Record
        fields = ['pacing', 'reaction_to_sight', 'reaction_to_call']
        widgets = {
            'pacing': forms.RadioSelect(choices=SCALE_CHOICES),
            'reaction_to_sight': forms.RadioSelect(choices=SCALE_CHOICES),
            'reaction_to_call': forms.RadioSelect(choices=SCALE_CHOICES),
        }


class RecordFormStep2(forms.ModelForm):
    """Step 2/3：夜間の落ち着き・活動量"""

    class Meta:
        model = Record
        fields = ['night_behavior', 'activity_level']
        widgets = {
            'night_behavior': forms.RadioSelect(choices=SCALE_CHOICES),
            'activity_level': forms.RadioSelect(choices=SCALE_CHOICES),
        }


class RecordFormStep3(forms.ModelForm):
    """Step 3/3：トイレの失敗・食欲"""

    class Meta:
        model = Record
        fields = ['toilet', 'appetite']
        widgets = {
            'toilet': forms.RadioSelect(choices=SCALE_CHOICES),
            'appetite': forms.RadioSelect(choices=SCALE_CHOICES),
        }