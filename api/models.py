from django.db import models

help_text_Structures_address = """В случае отсутвия адресса, введите название объекта"""
help_text_Advertisements_file = """Видео в формате .ogg| .ogv. Изображения в формате .png .jpeg"""

CHOICES_Orientation = (
    ('Vertical', 'Вертикальный'),
    ('Horizontal', 'Горизонтальный'),
)

CHOICES = (
    ('Video', 'Видео'),
    ('Image', 'Изображение'),
)


class Events(models.Model):
    """
        Мероприятия
        Свойства:
                Название - CharField
                Дата начала - DateField
                Дата окончания - DateField
                Описание - TextField
                Изображения - ImageField
    """
    name = models.CharField(max_length=300, default='', verbose_name='Название')
    start_date = models.DateField(default='', verbose_name='Дата начала')
    end_date = models.DateField(default='', verbose_name='Дата окончания')
    description = models.TextField(default='', verbose_name="Описание")
    image = models.ImageField(upload_to='media/event', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Structures(models.Model):
    """
        Здания
        Свойства:
                Адресс здания - CharField
    """
    address = models.CharField(max_length=300, default="", verbose_name="Адресс",
                               help_text=help_text_Structures_address)
    index = models.CharField(max_length=300, default="", verbose_name="Индекс")

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"


class Category(models.Model):
    """
        Категория
        Свойства:
                Имя - CharField
     """
    name = models.CharField(max_length=300, default='', verbose_name="Имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Shop(models.Model):
    """
        Магазин
        Свойства:
                Имя - CharField
                Телефон - CharField
                Рабочее время - CharField
                Категория - ForeignKey - Category
                Описание - TextField
                Местоположение - CharField
                Логотип магазина - ImageField
    """
    name = models.CharField(max_length=400, default='', verbose_name="Имя")
    phone = models.CharField(max_length=250, default='', verbose_name="Телефон")
    work_time = models.CharField(max_length=250, default='', verbose_name="Рабочее время")
    category = models.ForeignKey('Category', default='', verbose_name="Категория")
    description = models.TextField(default='', verbose_name="Описание")
    location = models.ForeignKey('Structures', verbose_name='Адресс магазина', related_name='shops')
    image = models.ImageField(upload_to="media/shops", max_length=300, blank=True, verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"


class PlayListAdvertisements(models.Model):
    """
        Плэй лист реколамы
        Свойства:
                Имя - CharField
                Список рекламы - ManyToManyField
    """
    name = models.CharField(max_length=300, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Плэй лист рекламы"
        verbose_name_plural = "Плэй листы рекламы"


class Advertisements(models.Model):
    """
        Реклама
        Свойсва:
                Имя - CharField
                Количество - IntegerField
                Файл - FileField
                Положение рекламы ( вертикальный / горизонтальный ) - CharField
                Активность - BooleanField
                Тип - CharField
                Время показа в сек - IntegerField
    """
    name = models.CharField(max_length=300, verbose_name="Название рекламы")
    number_of_impressions = models.IntegerField(default=0, verbose_name="Количество показов")
    file = models.FileField(verbose_name="Файл с рекламой",
                            help_text=help_text_Advertisements_file)
    orientation = models.CharField(max_length=30, choices=CHOICES_Orientation, default='',
                                   verbose_name="Ореинтация баннера")
    active = models.BooleanField(default=False, verbose_name="Показ на экране")
    type = models.CharField(max_length=30, choices=CHOICES, verbose_name="Тип")
    time = models.IntegerField(default=0, verbose_name="Время")
    play_list = models.ForeignKey('PlayListAdvertisements', verbose_name='Плэй лист рекламы', default=1,related_name='play')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Реклама"


class Terminal(models.Model):
    """
        Терминал
        Свойства:
                Имя - CharField
                Позиция на карте ( серийный номер терминала ) - CharField
    """
    name = models.CharField(max_length=300, verbose_name="Название")
    location = models.CharField(max_length=300, verbose_name="Позиция на карте", help_text="Серийный номер терминала")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Терминал"
        verbose_name_plural = "Терминалы"
