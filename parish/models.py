from django.db import models

# Create your models here.

class Priest(models.Model):
    STATUS = (
        ('main', 'Main'),
        ('deputy', 'Deputy'),
        ('normal', 'Normal')
    )
    
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices = STATUS)

    class Meta:

        verbose_name = 'Priest'
        verbose_name_plural = 'Priests'

    def __str__(self):
        return self.name


class SubParish(models.Model):

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'SubParish'
        verbose_name_plural = 'SubParishs'

    def __str__(self):
        return self.name


class Member(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    STATUS = (
        ('single', 'Single'),
        ('married', 'Married')
    )

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices = GENDER)
    marital_status = models.CharField(max_length=50, choices = STATUS)
    is_contributed = models.BooleanField(null = True, blank = True)
    is_baptized = models.BooleanField(null = True, blank = True)

    class Meta:

        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.name

class Community(models.Model):
    ROLES = (
        ('chairman', 'Chairman'),
        ('deputy_chairman', 'Deputy Chairman'),
        ('general_secretary', 'General Secretary'),
        ('deputy_secretary', 'Deputy Secretary'),
        ('accountant', 'Accountant'),
        ('member', 'Member')
    )

    name = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default= 'MEMBER')
    role = models.CharField(max_length = 50, choices = ROLES)


    class Meta:

        verbose_name = 'Community'
        verbose_name_plural = 'Communities'

    def __str__(self):
        return self.name
class Contribution(models.Model):
    RANK = (
        ('above','Above'),
        ('standard','Standard'),
        ('below', 'Below')
        
    )

    TYPE = (
        ('tithe', 'Tithe'),
        ('construction','Construction'),
        ('thanksgiving','Thanksgiving')
    )

    amount = models.DecimalField(max_digits=25, decimal_places=2)
    member = models.ManyToManyField(Member)
    rank = models.CharField(max_length=50, choices = RANK)
    type = models.CharField(max_length=50, choices = TYPE)

    class Meta:

        verbose_name = 'Contribution'
        verbose_name_plural = 'Contributions'

    def __str__(self):
        return self.member

class Committee(models.Model):
    ROLES = (
        ('chairman', 'Chairman'),
        ('deputy_chairman', 'Deputy Chairman'),
        ('general_secretary', 'General Secretary'),
        ('deputy_secretary', 'Deputy Secretary'),
        ('accountant', 'Accountant')
    )

    name = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices = ROLES)

    class Meta:

        verbose_name = 'Committee'
        verbose_name_plural = 'Committee'

    def __str__(self):
        return self.name


