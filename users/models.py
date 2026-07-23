from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """メールアドレスをログインIDとするユーザーを作成するマネージャー"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('メールを登録してください')
        
        # 大文字小文字の違いで別アカウント扱いになるのを防ぐ
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # 平文で保存しないためハッシュ化する
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # 呼び出し側が False を渡してきた矛盾を弾く
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ユーザー名ではなくメールアドレスでログインするユーザーモデル"""

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # 管理画面にアクセスできるか
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    # ログインIDとして使うフィールド
    USERNAME_FIELD = 'email'
    # create_superuser で追加入力を求めるフィールドを指定する。USERNAME_FIELD は含めない
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



    



    