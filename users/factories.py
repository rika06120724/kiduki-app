import factory
from users.models import CustomUser


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
    
    email = factory.Faker('email')
    password = 'TestPassword123'
    
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default _create to use create_user."""
        manager = cls._get_manager(model_class)
        password = kwargs.pop('password', None)
        obj = manager.create_user(*args, **kwargs)
        if password:
            obj.set_password(password)
            obj.save()
        return obj