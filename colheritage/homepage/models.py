__author__ = 'Jeff'
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType



class Users(AbstractUser):
    address1 = models.TextField(max_length=50)
    city = models.TextField(max_length=30)
    state = models.TextField(max_length=2)
    zip = models.TextField(max_length=13)

    #user = models.OneToOneField(User)

    #class Meta:
    #abstract = True

class HistoricalFigures(models.Model):
    name = models.TextField(max_length=100)
    birthDate = models.TextField(max_length=30)
    birthPlace = models.TextField(max_length=100)
    deathDate = models.TextField(max_length=30)
    deathPlace = models.TextField(max_length=100)
    biographicalNote= models.TextField(max_length=300)
    isFictional = models.TextField(max_length=30)

class Organization(Users):
    organizationType = models.TextField(max_length=30)


class Person(Users):
    familyName = models.TextField(max_length=30)


class Agent(Person):
    appointmentDate = models.DateField()


class Participant(Person):
    biographicalSketch = models.TextField(max_length=100)
    contactRelationship = models.TextField(max_length=30)
    emergencyContact = models.ForeignKey(Person, related_name='+')


class Phone(models.Model):
    number = models.IntegerField()
    extension = models.IntegerField()
    type = models.TextField(max_length=20)
    Users = models.ForeignKey(Users)


class Items(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    standardRentalPrice = models.DecimalField(max_digits=10, decimal_places=2)

#Added a lot of new fields to store all the
#information about the address of the event
class Events(models.Model):
    name = models.TextField(max_length= 100, blank=False, null=False)
    type = models.TextField(max_length=100, blank=False, null=False)
    location = models.TextField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    address1 = models.TextField(max_length=100, blank=True, null=True)
    address2 = models.TextField(max_length=100, blank=True, null=True)
    city = models.TextField(max_length=100, blank=True, null=True)
    state = models.TextField(max_length=100, blank=True, null=True)
    zip = models.TextField(max_length=100, blank=True, null=True)
    mapURL = models.TextField(max_length=300, blank=True, null=True)

class Areas(models.Model):
    name = models.TextField(max_length= 50)
    description = models.TextField(max_length=100, blank=True, null=True)
    coordinator = models.ForeignKey(Users, blank=True, null=True)
    supervisor = models.ForeignKey(Users, related_name='+', blank=True, null=True)
    event = models.ForeignKey(Events, related_name='+', blank=True, null=True)
    image = models.TextField(max_length=200, blank=True, null=True)

class Products(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200, blank=True, null=True)
    category = models.TextField(max_length=30)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.TextField(null=True)
    isrental = models.BooleanField(default=False)
    isartisan = models.BooleanField(default=False)
    event = models.ForeignKey(Events, related_name='+', blank=True, null=True)

class Serialized_Product(Products):
    serial_number = models.TextField(max_length=200, blank=True, null=True)
    date_acquired = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    status = models.TextField(max_length=200, blank=True, null=True)
    for_sale = models.BooleanField(default=False)
    condition_new = models.TextField(max_length=200, blank=True, null=True)
    notes = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.serial_number


class WardrobeItem(Serialized_Product):
    size = models.TextField(max_length=15, blank=True, null=True)
    size_modifier = models.TextField(max_length=30, blank=True, null=True)
    gender = models.TextField(max_length=10, blank=True, null=True)
    color = models.TextField(max_length=30, blank=True, null=True)
    pattern = models.TextField(max_length=30, blank=True, null=True)
    start_year = models.TextField(max_length=4, blank=True, null=True)
    end_year = models.TextField(max_length=4, blank=True, null=True)

class Return(models.Model):
    returnTime = models.DateTimeField()
    feesPaid = models.DecimalField(max_digits=10, decimal_places=2)
    agent = models.ForeignKey(Agent)





class RentableItem(models.Model):
    type = models.TextField(max_length=20)


class Rental(models.Model):
    rentalTime = models.DateTimeField()
    dueDate = models.DateField()
    discountPercent = models.DecimalField(max_digits=4, decimal_places=2)
    organization = models.ForeignKey(Organization)
    person = models.ForeignKey(Person, null=True)
    agent = models.ForeignKey(Agent, related_name='+', null=True)
    RentableItem = models.ManyToManyField(RentableItem, null=True)


    #legalEntity = models.ForeignKey(Users)
    #class Meta:
    #abstract = True

class Order(models.Model):
    orderDate = models.DateTimeField()
    phone = models.TextField(max_length=12)
    datePacked = models.DateTimeField()
    datePaid = models.DateTimeField()
    dateShipped = models.DateTimeField()
    trackingNumber = models.TextField(max_length=35)
    packedBy = models.ForeignKey(Agent, related_name='+', null=True)
    paymentProcessedBy = models.ForeignKey(Agent, related_name='+', null=True)
    shippedBy = models.ForeignKey(Agent, related_name='+', null=True)

#class BulkProduct(Products):
    #quantityOnHand = models.TextField(max_length=10)
    #Products = models.ManyToManyField(Products, related_name='+')

#class IndividualProduct(Products):
 #   dateMade = models.DateTimeField()
  #  order = models.ForeignKey(Order)

#class PersonalProduct(Products):
 #   orderFormName = models.TextField(max_length=50)
  #  productionTime = models.DateTimeField()

class PersonalDetail(models.Model):
    orderFile = models.TextField(max_length=100)
    order = models.ManyToManyField(Order)

class BulkDetail(models.Model):
    quantity = models.TextField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)

#Added Rental Product as a way of keeping track of rentals
class Rental_Product(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200, blank=True, null=True)
    category = models.TextField(max_length=30)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.TextField(null=True)
    is_wardrobe_item = models.BooleanField(default=False)
    times_rented = models.IntegerField(blank=True, null=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    replacement_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Rented_Item(models.Model):
    date_out = models.DateField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    rental_product = models.ForeignKey(Rental_Product, related_name='+', blank=True, null=True)
    renter = models.ForeignKey(Users, blank=True, null=True)

#Added a Fee class to keep track of the fees for each rental
class Fee(models.Model):
    waived = models.BooleanField()
    rented_item = models.ForeignKey(Rented_Item, related_name='+', blank=True, null=True)

#added a late_fee class that inherits from fee
class Late_Fee(Fee):
    days_late = models.IntegerField(blank=True, null=True)

#added a damage_fee class that inherits from fee
class Damage_Fee(Fee):
    description = models.TextField(max_length=200, blank=True, null=True)



class SaleItems(models.Model):
    name = models.TextField(max_length = 50)
    description = models.TextField(max_length= 100)
    lowPrice = models.DecimalField(max_digits=10, decimal_places=2)
    highPrice = models.DecimalField(max_digits=10, decimal_places=2)
    #area = models.ForeignKey(Area, null=True)

class Role(models.Model):
    name = models.TextField(max_length= 50)
    type = models.TextField(max_length= 30)