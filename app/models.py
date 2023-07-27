import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SiteUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = SiteUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class Product(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=True)


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)


class Order(BaseModel):
    order_number = models.IntegerField(unique=True)
    items = models.JSONField()
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='customer', null=True, blank=True)
