
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,Group,Permission,BaseUserManager
# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email,username, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email,username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email,username, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self.create_user(email,username, password, **extra_fields)

class CustomUser(AbstractUser,PermissionsMixin):
    USER_TYPES = [
        ('Client', 'Client'),
        ('Admin', 'Admin'),
    ]
    

    user_type = models.CharField(choices=USER_TYPES, max_length=100)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="customuser_groups",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="customuser_permissions",
        verbose_name="user permissions"
    )
    # objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email','user_type')
    def __str__(self):
        return "{}".format(self.username)
