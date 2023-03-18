from django.db import models


class BitwiseNumber:
    BIT_1 = 1
    BIT_2 = 2
    BIT_3 = 4
    BIT_4 = 8
    BIT_5 = 16
    BIT_6 = 32
    BIT_7 = 64
    BIT_8 = 128
    BIT_9 = 256


class CarColors(models.IntegerChoices):
    WHITE = BitwiseNumber.BIT_1
    BLACK = BitwiseNumber.BIT_2
    RED = BitwiseNumber.BIT_3
    BLUE = BitwiseNumber.BIT_4


class CarTypes(models.IntegerChoices):
    SEDAN = BitwiseNumber.BIT_1
    HATCHBACK = BitwiseNumber.BIT_2
    TRUCK = BitwiseNumber.BIT_3
    COUPE = BitwiseNumber.BIT_4
