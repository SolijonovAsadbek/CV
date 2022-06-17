from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
from django.utils import timezone


class Head(models.Model):
    hi = models.CharField(max_length=30, null=False)
    fullname = models.CharField(max_length=30, null=False)
    about = models.TextField(max_length=200)
    button = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname


class About(models.Model):
    Nam = 'Namangan'
    And = 'Andijon'
    Far = 'Farg`ona'
    Tosh = 'Toshkent shahri'
    Tosh2 = 'Toshkent viloyat'
    Sir = 'Sirdaryo'
    Qash = 'Qashqadaryo'
    Sur = 'Surxandaryo'
    Nav = 'Navoiy'
    Bux = 'Buxoro'
    Xor = 'Xorazim'
    Qora = 'Qoraqalpog`iston Respublikasi'
    Sam = 'Samarqand'

    Junior = 'Junior'
    Midlle = 'Midlle'
    Senior = 'Senior'
    choise = [(Nam, 'Namangan'),
              (And, 'Andijon'),
              (Far, 'Farg`ona'),
              (Tosh, 'Toshkent shahri'),
              (Tosh2, 'Toshkent viloyat'),
              (Sir, 'Sirdaryo'),
              (Qash, 'Qashqadaryo'),
              (Sur, 'Surxandaryo'),
              (Nav, 'Navoiy'),
              (Bux, 'Buxoro'),
              (Xor, 'Xorazim'),
              (Qora, 'Qoraqalpog`iston Respublikasi'),
              (Sam, 'Samarqand')]

    choice = [(Junior, 'Junior'),
              (Midlle, 'Midlle'),
              (Senior, 'Senior')]
    subject = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    about_me = models.TextField(max_length=10000)
    create_date = models.DateTimeField(auto_now_add=True)
    birthday = models.DateTimeField(default=timezone.now())
    age = models.PositiveIntegerField(default=10)
    website = models.URLField()
    email = models.EmailField()
    level = models.CharField(max_length=7, choices=choice, default=Junior)
    phone = models.CharField(max_length=13, default='+998')
    city = models.CharField(max_length=30, choices=choise, default=Nam)
    freelance = models.BooleanField(default=False)
    cv = models.FileField(upload_to='media/cv/')

    def __str__(self):
        return self.subject


class Skills(models.Model):
    py = 'Python'
    dj = 'Django'
    fl = 'Flask'
    js = 'JavaScript'
    php = 'PHP'
    lv = 'Laravel'
    jv = 'Java'
    html = 'HTML'
    css = 'CSS'
    bot = 'Bootstrap'
    c = 'C'
    c_puls = 'C++'
    default = ''
    choice = [
        (default, ''),
        (py, 'Python'),
        (dj, 'Django'),
        (fl, 'Flask'),
        (js, 'JavaScript'),
        (php, 'PHP'),
        (lv, 'Laravel'),
        (jv, 'Java'),
        (html, 'HTML'),
        (css, 'CSS'),
        (bot, 'Bootstrap'),
        (c, 'C'),
        (c_puls, 'C++')
    ]

    subject = models.CharField(max_length=20, choices=choice, default=default)
    protsent = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    about_for = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
