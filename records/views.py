from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from pets.models import Pet
from .models import Record
from .forms import RecordFormStep1, RecordFormStep2, RecordFormStep3
from django.contrib import messages

# ステップとフォームクラスの対応
STEP_FORMS = {
    1: RecordFormStep1,
    2: RecordFormStep2,
    3: RecordFormStep3,
}


@login_required(login_url="users:login")
def create_record(request, pet_id):
    """ペット記録作成ビュー（複数ステップ）"""
    pet = get_object_or_404(Pet, id=pet_id)

    # 権限チェック
    if pet.owner != request.user:
        return redirect("pets:my_page")

    # ステップ管理（1〜3の範囲に制限）
    step = request.session.get("record_step", 1)
    if step not in STEP_FORMS:
        step = 1

    form_class = STEP_FORMS[step]

    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            # これまでのステップのデータとマージしてセッションに保存
            record_data = request.session.get("record_data", {})
            record_data.update(form.cleaned_data)
            request.session["record_data"] = record_data

            if step < 3:
                # 次のステップへ
                request.session["record_step"] = step + 1
                return redirect("records:create", pet_id=pet_id)
            else:
                # 最終ステップ：全データをまとめて保存
              
               
                Record.objects.update_or_create(
                    pet=pet,
                    target_date=timezone.localdate(),
                    defaults=record_data,
                )

                # セッションをクリア
                request.session.pop("record_step", None)
                request.session.pop("record_data", None)

                messages.success(request, "記録を保存しました。")
                return redirect("pets:my_page")
    else:
        form = form_class()

    context = {
        "form": form,
        "pet": pet,
        "step": step,
        "total_steps": 3,
        "today": timezone.localdate(),
    }

    return render(request, "records/record_form.html", context)