from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


class ItemInfo(models.Model):
    item_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="veg_images")

    def __str__(self) -> str:
        return self.item_name
    

class Items(models.Model):
    name = models.ForeignKey(ItemInfo, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.name





class Purchase(models.Model):
    purchase_date = models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items, related_name= "date_vegetables")
    amount_spent = models.IntegerField()

    def __str__(self) -> str:
        return self.purchase_date
    

class Amount(models.Model):
    last_month_amount_left  = models.IntegerField(default=0)
    default_amount          = models.IntegerField(default=14000)
    extra_amount_last_month = models.IntegerField(default=0)

class Month(models.Model):
    amount = models.OneToOneField(Amount, on_delete=models.CASCADE)
    month_name = models.CharField(max_length=10, null=False)
    purchases = models.ManyToManyField(Purchase, related_name="month_purchases")
    money_spent = models.IntegerField()

    def __str__(self) -> str:
        return f"Year : {self.get_months.year}==> Month : {self.month_name}"

class Year(models.Model):
    year = models.CharField(max_length = 4, null=False, blank=False)
    months = models.ManyToManyField(Month, related_name="get_months")

    def __str__(self) -> str:
        return f"Year is {self.year}"



