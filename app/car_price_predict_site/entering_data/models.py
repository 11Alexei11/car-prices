from django.db import models

from django.utils.translation import gettext_lazy


# Create your models here.
class User(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAME = models.CharField(max_length=30)
    SURNAME = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=30)
    REGISTRATION_DATE = models.DateTimeField()


class Car(models.Model):
    class ColumnNames:
        ID = "id"
        USER_ID = "user_id"
        LEVY = "levy"
        MANUFACTURER = "manufacturer"
        MODEL = "model"
        PROD_YEAR = "prod_year"
        CATEGORY = "category"
        LEATHER_INTERIOR = "leather_interior"
        FUEL_TYPE = "fuel_type"
        ENGINE_VOLUME = "engine_volume"
        MILEAGE = "mileage"
        CYLINDERS = "cylinders"
        GEAR_BOX_TYPE = "gear_box_type"
        DRIVE_WHEELS = "drive_wheels"
        DOORS = "doors"
        WHEEL = "wheel"
        COLOR = "color"
        AIRBUGS = "airbugs"
        PRICE = "price"

        @classmethod
        def column_names(cls):
            return [value for key, value in cls.__dict__.items() if not key.startswith('__') and key.isupper()]
        
        @classmethod
        def numeric_column_names(cls):
            return [
                cls.LEVY,
                cls.PROD_YEAR, 
                cls.LEATHER_INTERIOR,
                cls.MILEAGE,
                cls.CYLINDERS,
                cls.AIRBUGS
            ]
        
        @classmethod
        def string_column_names(cls):
            return [
                cls.MANUFACTURER,
                cls.MODEL,
                cls.CATEGORY,
                cls.FUEL_TYPE,
                cls.ENGINE_VOLUME,
                cls.GEAR_BOX_TYPE,
                cls.DRIVE_WHEELS,
                cls.DOORS,
                cls.WHEEL,
                cls.COLOR
            ]

    class Category(models.TextChoices):
        SEDAN = "Sedan", gettext_lazy("Sedan")
        JEEP = "Jeep", gettext_lazy("Jeep")
        HATCHBACK = "Hatchback", gettext_lazy("Hatchback")
        MINIVAN = "Minivan", gettext_lazy("Minivan")
        COUPE = "Coupe", gettext_lazy("Coupe")
        UNIVERSAL = "Universal", gettext_lazy("Universal")
        MICROBUS = "Microbus", gettext_lazy("Microbus")
        GOODS_WAGON = "Goods wagon", gettext_lazy("Goods wagon")
        PICKUP = "Pickup", gettext_lazy("Pickup")
        Cabriolet = "Cabriolet", gettext_lazy("Cabriolet")
        LIMOUSINE = "Limousine", gettext_lazy("Limousine")
    
    class FuelType(models.TextChoices):
        PETROL = "Petrol", gettext_lazy("Petrol")
        DISEL = "Diesel", gettext_lazy("Diesel")
        HYBRID = "Hybrid", gettext_lazy("Hybrid")
        LPG = "LPG", gettext_lazy("LPG")
        CNG = "CNG", gettext_lazy("CNG")
        HYDROGEN = "Hydrogen", gettext_lazy("Hydrogen")
         
    class GearBoxType(models.TextChoices):
        AUTOMATIC = 'Automatic', gettext_lazy("Automatic")
        TIPTRONIC = 'Tiptronic', gettext_lazy("Tiptronic")
        VARIATOR = 'Variator', gettext_lazy("Variator")
        MANUAL = 'Manual', gettext_lazy("Manual")
    
    class DriveWheels(models.TextChoices):
        FOUR = "4x4", gettext_lazy("4x4")
        FRONT = "Front", gettext_lazy("Front") 
        REAR = 'Rear', gettext_lazy("Rear")
    
    class Wheel(models.TextChoices):
        LEFT_WHEEL = "Left wheel", gettext_lazy("Left wheel") 
        RIGHT_HAND_DRIVE = "Right-hand drive", gettext_lazy("Right-hand drive")

    class Color(models.TextChoices):
        SILVER = 'Silver', gettext_lazy("Silver")
        BLACK = 'Black', gettext_lazy("Black")
        WHITE = 'White', gettext_lazy("White")
        GREY = 'Grey', gettext_lazy("Grey")
        BLUE = 'Blue', gettext_lazy("Blue")
        GREEN = 'Green', gettext_lazy("Green")
        RED = 'Red', gettext_lazy("Red")
        SKY_BLUE = 'Sky blue', gettext_lazy("Sky blue")
        ORANGE = 'Orange', gettext_lazy("Orange")
        YELLOW = 'Yellow', gettext_lazy("Yellow")
        BROWN = 'Brown', gettext_lazy("Brown")
        GOLDEN = 'Golden', gettext_lazy("Golden")
        BEIGE = 'Beige', gettext_lazy("Beige")
        CARNELIAN_RED = 'Carnelian red', gettext_lazy("Carnelian red")
        PURPLE = 'Purple', gettext_lazy("Purple")
        PINK = 'Pink', gettext_lazy("Pink")
    
    class Doors(models.TextChoices):
        FOUR = "04-may", gettext_lazy("04-may")
        TWO = "02-mar", gettext_lazy("02-mar")
        FIVE_GRATER = ">5", gettext_lazy(">5")

    ID = models.BigAutoField(verbose_name='id', primary_key=True)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)

    LEVY = models.IntegerField(verbose_name='levy')
    MANUFACTURER = models.CharField(verbose_name='manufacturer', max_length=15)
    MODEL = models.CharField(verbose_name='model', max_length=30)
    PROD_YEAR = models.IntegerField(verbose_name='prod_year')
    CATEGORY = models.CharField(db_column='category', max_length=30, choices=Category.choices)
    LEATHER_INTERIOR = models.BinaryField(verbose_name='leather_interior')
    FUEL_TYPE = models.CharField(verbose_name='fuel_type', max_length=30, choices=FuelType.choices)
    ENGINE_VOLUME = models.CharField(verbose_name='engine_volume', max_length=30)
    MILEAGE = models.IntegerField(verbose_name='mileage')
    CYLINDERS = models.IntegerField(verbose_name='cylinders')
    GEAR_BOX_TYPE = models.CharField(verbose_name='gear_box_type', max_length=30, choices=GearBoxType.choices)
    DRIVE_WHEELS = models.CharField(verbose_name='drive_wheels', max_length=30, choices=DriveWheels.choices)
    DOORS = models.CharField(verbose_name='doors', max_length=30, choices=Doors.choices)
    WHEEL = models.CharField(verbose_name='wheel', max_length=30, choices=Wheel.choices)
    COLOR = models.CharField(verbose_name='color', max_length=30, choices=Color.choices)
    AIRBUGS = models.IntegerField(verbose_name='airbugs')
    PRICE = models.FloatField(verbose_name='price')