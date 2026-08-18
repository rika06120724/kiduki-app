from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from users.factories import UserFactory

User = get_user_model()


class UserModelTests(TestCase):
    """ユーザーモデルのテスト"""

    # Sub-task 1：ユーザー作成のテスト
    def test_create_user(self):
        """一般ユーザーが作成できるか"""
        user = UserFactory(email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """管理者ユーザーが作成できるか"""
        admin = User.objects.create_superuser(
            email='admin@example.com',
            password='AdminPassword123'
        )
        self.assertEqual(admin.email, 'admin@example.com')
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    # Sub-task 2：メールアドレスバリデーションのテスト
    def test_duplicate_email_raises_error(self):
        """重複したメールアドレスでエラーが出るか"""
        UserFactory(email='duplicate@example.com')
        with self.assertRaises(Exception):
            User.objects.create_user(
                email='duplicate@example.com',
                password='TestPassword123'
            )

    def test_user_without_email_raises_error(self):
        """メールアドレスなしでエラーが出るか"""
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='TestPassword123')

    # Sub-task 3：登録からログインまでの流れのテスト
    def test_user_login_flow(self):
        """ユーザー作成からログインまでの流れ"""
        email = 'testuser@example.com'
        password = 'TestPassword123'
        
        # ユーザーを作成
        user = UserFactory(email=email)
        user.set_password(password)
        user.save()
        
        # ユーザーが取得できるか
        retrieved_user = User.objects.get(email=email)
        self.assertEqual(retrieved_user.email, email)
        self.assertTrue(retrieved_user.check_password(password))