from django.db import models

from django.utils.translation import gettext_lazy


# Create your models here.
class Person(models.Model):
    ID = models.BigAutoField(primary_key=True)
    NAME = models.CharField(max_length=30)
    SURNAME = models.CharField(max_length=30)
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
    
    # class EngineVolume(models.TextChoices):
    #     ZERO = "0", gettext_lazy("0")
    #     ZERO_ONE = "0.1", gettext_lazy("0.1")
    #     ZERO_TWO = "0.2", gettext_lazy("0.2")
    #     ZERO_TWO_TURBO = "0.2 Turbo", gettext_lazy("0.2 Turbo")
    #     ZERO_THREE = "0.3", gettext_lazy("0.3")
    #     ZERO_THREE_THREE = "0.3 Turbo", gettext_lazy("0.3 Turbo")
    #     ZERO_FOUR = "0.4", gettext_lazy("0.4")
    #     ZERO_FOUR_TURBO = "0.4 Turbo", gettext_lazy("0.4 Turbo")
    #     ZERO_FIVE = "0.5", gettext_lazy("0.5")
    #     ZERO_SIX = "0.6", gettext_lazy("0.6")
    #     ZERO_SIX_TURBO = "0.6 Turbo", gettext_lazy("0.6 Turbo")
    #     ZERO_SEVEN = "0.7", gettext_lazy("0.7")
    #     ZERO_SEVEN_TURBO = "0.7 Turbo", gettext_lazy("0.7 Turbo")
    #     ZERO_EIGHT = "0.8", gettext_lazy("0.8")
    #     ZERO_EIGHT_TURBO = "0.8 Turbo", gettext_lazy("0.8 Turbo")
    #     ZERO_NINE = "0.9", gettext_lazy("0.9")

    #     ONE = "1", gettext_lazy("1")
    #     ONE_TURBO = "1.0 Turbo", gettext_lazy("1.0 Turbo")
    #     ONE_ONE = "1.1", gettext_lazy("1.1")
    #     ONE_ONE_TURBO = "1.1 Turbo", gettext_lazy("1.1 Turbo")
    #     ONE_TWO = "1.2", gettext_lazy("1.2")
    #     ONE_TWO_TURBO = "1.2 Turbo", gettext_lazy("1.2 Turbo")
    #     ONE_THREE = "1.3", gettext_lazy("1.3")
    #     ONE_THREE_TURBO = "1.3 Turbo", gettext_lazy("1.3 Turbo")
    #     ONE_FOUR = "1.4", gettext_lazy("1.4")
    #     ONE_FOUR_TURBO = "1.4 Turbo", gettext_lazy("1.4 Turbo")
    #     ONE_FIVE = "1.5", gettext_lazy("1.5")
    #     ONE_FIVE_TURBO = "1.5 Turbo", gettext_lazy("1.5 Turbo")
    #     ONE_SIX = "1.6", gettext_lazy("1.6")
    #     ONE_SIX_TURBO = "1.6 Turbo", gettext_lazy("1.6 Turbo")
    #     ONE_SEVEN = "1.7", gettext_lazy("1.7")
    #     ONE_SEVEN_TURBO = "1.7 Turbo", gettext_lazy("1.7 Turbo")
    #     ONE_EIGHT = "1.8", gettext_lazy("1.8")
    #     ONE_EIGHT_TURBO = "1.8 Turbo", gettext_lazy("1.8 Turbo")
    #     ONE_NINE = "1.9", gettext_lazy("1.9")
    #     ONE_NINE_TURBO = "1.9 Turbo", gettext_lazy("1.9 Turbo")

    #     TWO = "2", gettext_lazy("2"),
    #     TWO_TURBO = "2.0 Turbo", gettext_lazy("2.0 Turbo")
    #     TWO_ONE = "2.1", gettext_lazy("2.1")
    #     TWO_ONE_TURBO = "2.1 Turbo", gettext_lazy("2.1 Turbo")
    #     TWO_TWO = "2.2", gettext_lazy("2.2")
    #     TWO_TWO_TURBO = "2.2 Turbo", gettext_lazy("2.2 Turbo")
    #     TWO_THREE = "2.3", gettext_lazy("2.3")
    #     TWO_THREE_TURBO = "2.3 Turbo", gettext_lazy("2.3 Turbo")
    #     TWO_FOUR = "2.4", gettext_lazy("2.4"),
    #     TWO_FOUR_TURBO = "2.4 Turbo", gettext_lazy("2.4 Turbo")
    #     TWO_FIVE = "2.5", gettext_lazy("2.5")
    #     TWO_FIVE_TURBO = "2.5 Turbo", gettext_lazy("2.5 Turbo")
    #     TWO_SIX = "2.6", gettext_lazy("2.6")
    #     TWO_SEVEN = "2.7", gettext_lazy("2.7")
    #     TWO_SEVEN_TURBO = "2.7 Turbo", gettext_lazy("2.7 Turbo")
    #     TWO_EIGHT = "2.8", gettext_lazy("2.8")
    #     TWO_EIGHT_TURBO = "2.8 Turbo", gettext_lazy("2.8 Turbo")
    #     TWO_NINE = "2.9", gettext_lazy("2.9")
    #     TWO_NINE_TURBO = "2.9 Turbo", gettext_lazy("2.9 Turbo")
    #     SIX_THREE_TURBO = "6.3 Turbo", gettext_lazy("6.3 Turbo")
    #     SIX_FOUR = "6.4", gettext_lazy("6.4")
    #     SIX_SEVEN = "6.7", gettext_lazy("6.7")
    #     SIX_EIGHT = "6.8", gettext_lazy("6.8")

    #     SEVEN_THREE = "7.3", gettext_lazy("7.3")
    #     TWENTY = "20", gettext_lazy("20")
    #     THREE = "3", gettext_lazy("3")
    #     THREE_TURBO = "3.0 Turbo", gettext_lazy("3.0 Turbo")
    #     THREE_ONE = "3.1", gettext_lazy("3.1")
    #     THREE_TWO = "3.2", gettext_lazy("3.2")
    #     THREE_TWO_TURBO = "3.2 Turbo", gettext_lazy("3.2 Turbo")
    #     THREE_THREE = "3.3", gettext_lazy("3.3")
    #     THREE_FOUR = "3.4", gettext_lazy("3.4")
    #     THREE_FIVE = "3.5", gettext_lazy("3.5")
    #     THREE_FIVE_TURBO = "3.5 Turbo", gettext_lazy("3.5 Turbo")
    #     THREE_SIX = "3.6", gettext_lazy("3.6")
    #     THREE_SIX_TURBO = "3.6 Turbo", gettext_lazy("3.6 Turbo")
    #     THREE_SEVEN = "3.7", gettext_lazy("3.7")
    #     THREE_SEVEN_TURBO = "3.7 Turbo", gettext_lazy("3.7 Turbo")
    #     THREE_EIGHT = "3.8", gettext_lazy("3.8")
    #     THREE_NINE = "3.9", gettext_lazy("3.9")

    #     FOUR = "4", gettext_lazy("4")
    #     FOUR_TURBO = "4.0 Turbo", gettext_lazy("4.0 Turbo")
    #     FOUR_TWO = "4.2", gettext_lazy("4.2")
    #     FOUR_TWO_TURBO = "4.2 Turbo", gettext_lazy("4.2 Turbo")
    #     FOUR_THREE = "4.3", gettext_lazy("4.3")
    #     FOUR_FOUR = "4.4", gettext_lazy("4.4")
    #     FOUR_FOUR_TURBO = "4.4 Turbo", gettext_lazy("4.4 Turbo")
    #     FOUR_FIVE = "4.5", gettext_lazy("4.5")
    #     FOUR_FIVE_TURBO = "4.5 Turbo", gettext_lazy("4.5 Turbo")
    #     FOUR_SIX = "4.6", gettext_lazy("4.6")
    #     FOUR_SIX_TURBO = "4.6 Turbo", gettext_lazy("4.6 Turbo")
    #     FOUR_SEVEN = "4.7", gettext_lazy("4.7")
    #     FOUR_SEVEN_TURBO = "4.7 Turbo", gettext_lazy("4.7 Turbo")
    #     FOUR_EIGHT = "4.8", gettext_lazy("4.8")
    #     FOUR_EIGHT_TURBO = "4.8 Turbo", gettext_lazy("4.8 Turbo")

    #     FIVE = "5", gettext_lazy("5")
    #     FIVE_TURBO = "5.0 Turbo", gettext_lazy("5.0 Turbo")
    #     FIVE_TWO = "5.2", gettext_lazy("5.2")
    #     FIVE_THREE = "5.3", gettext_lazy("5.3")
    #     FIVE_FOUR = "5.4", gettext_lazy("5.4")
    #     FIVE_FOUR_TURBO = "5.4 Turbo", gettext_lazy("5.4 Turbo")
    #     FIVE_FIVE = "5.5", gettext_lazy("5.5")
    #     FIVE_FIVE_TURBO = "5.5 Turbo", gettext_lazy("5.5 Turbo")
    #     FIVE_SIX = "5.6", gettext_lazy("5.6")
    #     FIVE_SEVEN = "5.7", gettext_lazy("5.7")
    #     FIVE_SEVEN_TURBO = "5.7 Turbo", gettext_lazy("5.7 Turbo")
    #     FIVE_EIGHT = "5.8", gettext_lazy("5.8")
    #     FIVE_NINE = "5.9", gettext_lazy("5.9")

    #     SIX = "6", gettext_lazy("6")
    #     SIX_TWO = "6.2", gettext_lazy("6.2")
    #     SIX_THREE = "6.3", gettext_lazy("6.3")
    #     SIX_THREE_TURBO = "6.3 Turbo", gettext_lazy("6.3 Turbo")
    #     SIX_FOUR = "6.4", gettext_lazy("6.4")
    #     SIX_SEVEN = "6.7", gettext_lazy("6.7")
    #     SIX_EIGHT = "6.8", gettext_lazy("6.8")

    #     SEVEN_THREE = "7.3", gettext_lazy("7.3")
    #     TWENTY = "20", gettext_lazy("20")
         
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
    USER_ID = models.ForeignKey(Person, on_delete=models.CASCADE)

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