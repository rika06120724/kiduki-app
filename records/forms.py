from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    """ペット記録フォーム（基本）"""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    class Meta:
        model = Record
        fields = ["pacing", "reaction_to_sight", "reaction_to_call", 
                  "night_behavior", "activity_level", "toilet", "appetite"]


class RecordFormStep1(forms.Form):
    """Step 1: ①②③"""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    pacing = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="① 徘徊")
    reaction_to_sight = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="② 姿への反応")
    reaction_to_call = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="③ 名前への反応")


class RecordFormStep2(forms.Form):
    """Step 2: ④⑤"""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    night_behavior = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="④ 夜間の落ち着き")
    activity_level = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="⑤ 活動量")


class RecordFormStep3(forms.Form):
    """Step 3: ⑥⑦"""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    toilet = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="⑥ トイレの失敗")
    appetite = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="⑦ 食欲")
