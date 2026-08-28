from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from pets.models import Pet
from .models import Record
from .forms import RecordFormStep1, RecordFormStep2, RecordFormStep3

@login_required(login_url="users:login")
def create_record(request, pet_id):
    """ペット記録作成ビュー（複数ステップ）"""
    pet = get_object_or_404(Pet, id=pet_id)
    
    # 権限チェック
    if pet.owner != request.user:
        return redirect("pets:my_page")
    
    # ステップ管理
    step = request.session.get("record_step", 1)
    
    # ステップごとのフォームクラスを選択
    form_classes = {
        1: RecordFormStep1,
        2: RecordFormStep2,
        3: RecordFormStep3,
    }
    FormClass = form_classes[step]
    
    if request.method == "POST":
        form = FormClass(request.POST)
        
        # セッションからこれまでのデータを取得
        record_data = request.session.get("record_data", {})
        
        if form.is_valid():
            # このステップのデータを保存
            current_data = form.cleaned_data.copy()
            record_data.update(current_data)
            
            # 次のステップへ
            if step < 3:
                request.session["record_step"] = step + 1
                request.session["record_data"] = record_data
                return redirect("records:create", pet_id=pet_id)
            else:
                # 最終ステップ：保存
                record = Record(
                    pet=pet,
                    target_date=timezone.now().date(),
                    pacing=int(record_data.get("pacing")),
                    reaction_to_sight=int(record_data.get("reaction_to_sight")),
                    reaction_to_call=int(record_data.get("reaction_to_call")),
                    night_behavior=int(record_data.get("night_behavior")),
                    activity_level=int(record_data.get("activity_level")),
                    toilet=int(record_data.get("toilet")),
                    appetite=int(record_data.get("appetite")),
                )
                record.save()
                
                # セッションをクリア
                request.session.pop("record_step", None)
                request.session.pop("record_data", None)
                
                return redirect("pets:my_page")
    else:
        # 前のステップのデータを取得
        record_data = request.session.get("record_data", {})
        form = FormClass(initial=record_data)
    
    context = {
        "form": form,
        "pet": pet,
        "step": step,
        "total_steps": 3,
        "today": timezone.now().date(),
    }
    
    return render(request, "records/record_form.html", context)
