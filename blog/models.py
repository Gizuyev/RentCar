from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=255,)
    description = models.CharField('Описание', max_length=455)
    image = models.ImageField("Фото", upload_to='blogs')
    date = models.DateField('Дата')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    


class FeedBacks(models.Model):
    CHOISES = (
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
    )
    text = models.CharField("Текст", max_length=255)
    gender = models.CharField("Пол", choices=CHOISES, max_length=10)
    name = models.CharField("Имя", max_length=20)
    profession = models.CharField("Профессия", max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Callback(models.Model):
    name = models.CharField("Имя", max_length=20)
    phone = models.CharField("Номер телефона", max_length=20)
    email = models.EmailField('email адрес')
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'




class CarMark(models.Model):
    name = models.CharField('Модель',max_length=255, unique=True)

    def __str__(self):
        return self.name





class Car(models.Model):
    make = models.ForeignKey(CarMark, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars')

    def __str__(self):
        return f"{self.year} {self.make.name} {self.model}"





class CustomUserManage(BaseUserManager):
    def create_user(self, **kwargs):
        user = self.model(**kwargs)
        user.set_password(kwargs.get('password'))
        user.save()
        return user

    def create(self, **kwargs):
        return self.create_user(**kwargs)

    def create_superuser(self, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(**kwargs)


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    
    objects = CustomUserManage()

    def __str__(self):
        return self.username