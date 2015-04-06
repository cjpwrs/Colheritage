#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'colheritage.settings'
import django
import datetime
import sys
django.setup()


#reular imports
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess
import django
django.setup()
import homepage.models as hmod

print(hmod)

#empty or drop the tables
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

#### Create permissions/groups ######
Permission.objects.all().delete()
Group.objects.all().delete()


##Admin
permission = Permission()
permission.codename = 'admin_rights'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'AdminRights'
permission.save()

agroup = Group()
agroup.name = "Admin"
agroup.save()
agroup.permissions.add(permission)
subprocess.call([sys.executable, "manage.py", "migrate"])

###Manager
permission = Permission()
permission.codename = 'manager_rights'
permission.content_type = ContentType.objects.get(id=5)
permission.name = 'ManagerRights'
permission.save()

mgroup = Group()
mgroup.name = "Manager"
mgroup.save()
mgroup.permissions.add(permission)


######Guest
permission = Permission()
permission.codename = 'guest_rights'
permission.content_type = ContentType.objects.get(id=2)
permission.name = 'GuestRights'
permission.save()

gugroup = Group()
gugroup.name = "Guest"
gugroup.save()
gugroup.permissions.add(permission)

############ MAKE USERS ####################
u = hmod.Users()
u.username = 'cjpwrs'
u.set_password('cj24')
u.first_name = 'CJ'
u.last_name = 'Powers'
u.email = 'cjpwrs@gmail.com'
u.address1 = '111'
u.city = 'Orem'
u.state = 'UT'
u.zip = '84058'
u.is_superuser = True
u.save()

agroup.user_set.add(u)

u = hmod.Users()
u.username = 'Spencer'
u.set_password('Spencer')
u.first_name = 'Spencer'
u.last_name = 'Smith'
u.email = 'spencer.smith@yahoo.com'
u.address1 = 'KryptonLane'
u.city = 'Metropolis'
u.state = 'NY'
u.zip = '87847'
u.save()

agroup.user_set.add(u)

u = hmod.Users()
u.username = 'Spiderman'
u.set_password('spiderman')
u.first_name = 'Peter'
u.last_name = 'Parker'
u.email = 'pete@sman.com'
u.address1 = 'broadway'
u.city = 'New York City'
u.state = 'NY'
u.zip = '88779'
u.save()

gugroup.user_set.add(u)

u = hmod.Users()
u.username = 'Michael'
u.set_password('michael')
u.first_name = 'Michael'
u.last_name = 'Scott'
u.email = 'greatscott@dundermifflin.com'
u.address1 = '234 quarry lane'
u.city = 'Scranton'
u.state = 'PA'
u.zip = '74456'
u.save()

mgroup.user_set.add(u)


u = hmod.Users()
u.username = 'EzioA'
u.set_password('ezioa')
u.first_name = 'Ezio'
u.last_name = 'Auditore'
u.email = 'ezio@assassins.org'
u.address1 = '789 Nowhere'
u.city = 'unknown'
u.state = 'unknown'
u.zip = '11111'
u.save()

agroup.user_set.add(u)


u = hmod.Users()
u.username = 'Eminem'
u.set_password('eminem')
u.first_name = 'Marshall'
u.last_name = 'Mathers'
u.email = 'slimshady@fu.com'
u.address1 = '16 Trailer Park'
u.city = 'Detroit'
u.state = 'MI'
u.zip = '44896'
u.save()

mgroup.user_set.add(u)


u = hmod.Users()
u.username = 'CR7ya'
u.set_password('cr7ya')
u.first_name = 'Cristiano'
u.last_name = 'Ronaldo'
u.email = 'cr7@realmadrid.org'
u.address1 = '769 futbol camino'
u.city = 'Real Madrid'
u.state = 'Espana'
u.zip = '66325'
u.save()

gugroup.user_set.add(u)


u = hmod.Users()
u.username = 'Curry'
u.set_password('curry')
u.first_name = 'Stephen'
u.last_name = 'Curry'
u.email = 'steph@gstate.com'
u.address1 = '8890 colliseum way'
u.city = 'Oakland'
u.state = 'CA'
u.zip = '95316'
u.save()

gugroup.user_set.add(u)


u = hmod.Users()
u.username = 'GreenArrow'
u.set_password('greenarrow')
u.first_name = 'Oliver'
u.last_name = 'Queen'
u.email = 'ollie@queenindustries.org'
u.address1 = '1 Queen Blvd.'
u.city = 'Starling City'
u.state = 'NY'
u.zip = '88749'
u.save()

agroup.user_set.add(u)


ag = hmod.Agent()
ag.username = 'Ironman'
ag.set_password('ironman')
ag.first_name = 'Tony'
ag.last_name = 'Stark'
ag.email = 'ironman@si.com'
ag.address1 = '334 Crescent Lane'
ag.city = 'Huntington Beach'
ag.state = 'CA'
ag.zip = '91203'
ag.appointmentDate = datetime.datetime.now()
ag.save()

mgroup.user_set.add(u)


ag = hmod.Agent()
ag.username = 'ProfessorX'
ag.set_password('professorx')
ag.first_name = 'Charles'
ag.last_name = 'Xavier'
ag.email = 'profx@gifted.org'
ag.address1 = '345 Lane'
ag.city = 'Richmond'
ag.state = 'VA'
ag.zip = '78445'
ag.appointmentDate = datetime.datetime.now()
ag.save()

mgroup.user_set.add(u)


ag = hmod.Agent()
ag.username = 'JBourne'
ag.set_password('jbourne')
ag.first_name = 'Jason'
ag.last_name = 'Bourne'
ag.email = 'jbourne@capitolhill.gov'
ag.address1 = '554 cherry ave'
ag.city = 'Langley'
ag.state = 'VA'
ag.zip = '88465'
ag.appointmentDate = datetime.datetime.now()
ag.save()

mgroup.user_set.add(u)
e = hmod.Events()
e.name = 'The Colonial Heritage Festival'
e.description = 'The Colonial Heritage Festival is an annual event scheduled for the ' \
                'week of the Fourth of July. Running three or four days, the event attracts ' \
                'around 40,000 visitors each year. Held in the Scera Park in Orem, Utah, it ' \
                'has become the largest colonial living and reenactment event in the western ' \
                'United States. The festival comprises dozens of exhibits and presentations ' \
                'from more than 100 volunteers. The festival is free to the public'
e.startDate = '2015-07-04'
e.endDate = '2015-07-6'
e.mapURL = 'https://www.google.com/maps/place/Nielson''s+Grove+Park/@40.261895,-111.70259,15z/data=!4m2!3m1!1s0x0:0x8c91b1c0bb0af9ba'
e.save()

a = hmod.Areas()
a.name = 'Security'
a.description = 'This is where things are secure'
a.coordinator = hmod.Users.objects.get(username='cjpwrs')
a.supervisor = hmod.Users.objects.get(username='cjpwrs')
a.event = hmod.Events.objects.get(id=1)
a.image = '/homepage/media/areas/security.jpg'
a.save()

a = hmod.Areas()
a.name = 'Information Booths'
a.description = 'You can find all your information here'
a.coordinator = hmod.Users.objects.get(username='cjpwrs')
a.supervisor = hmod.Users.objects.get(username='cjpwrs')
a.event = hmod.Events.objects.get(id=1)
a.image = '/homepage/media/areas/information.jpg'
a.save()

a = hmod.Areas()
a.name = 'Bakehouse Exibit'
a.description = 'This is a house for baking'
a.coordinator = hmod.Users.objects.get(username='cjpwrs')
a.supervisor = hmod.Users.objects.get(username='cjpwrs')
a.event = hmod.Events.objects.get(id=1)
a.image = '/homepage/media/areas/bakehouse.jpg'
a.save()

a = hmod.Areas()
a.name = 'Jamestowne Exibit'
a.description = 'This is a cool exibit that will show you what' \
                'life was like in Jamestowne'
a.coordinator = hmod.Users.objects.get(username='cjpwrs')
a.supervisor = hmod.Users.objects.get(username='cjpwrs')
a.event = hmod.Events.objects.get(id=1)
a.image = '/homepage/media/areas/jamestowne.jpg'
a.save()

a = hmod.Areas()
a.name = 'Old South Church'
a.description = 'Various performances take place here'
a.coordinator = hmod.Users.objects.get(username='cjpwrs')
a.supervisor = hmod.Users.objects.get(username='cjpwrs')
a.event = hmod.Events.objects.get(id=1)
a.image = '/homepage/media/areas/church.jpg'
a.save()
print("area made")


p = hmod.Products()
p.name = 'Colonial Bell'
p.description = 'Handmade Brass Bell'
p.category = 'Individual'
p.image = '/homepage/media/products/colonialbell.jpg'
p.currentPrice = '14.00'
p.save()

p = hmod.Products()
p.name = 'Colonial Hat'
p.currentPrice = '20.99'
p.description = 'A tricorn hat used in the late 1700s'
p.image = '/homepage/media/products/colonialhat.jpg'
p.category = ''
p.save()


p = hmod.Products()
p.name = 'Printer Breeches'
p.currentPrice = '30.99'
p.description = 'size 36x32 magenta colonial style'
p.image = '/homepage/media/products/breeches.jpeg'
p.category = ''
p.save()

p = hmod.Products()
p.name = 'Printer Breeches'
p.currentPrice = '2.99'
p.description = 'size 36x32 magenta colonial style'
p.image = '/homepage/media/products/breeches.jpeg'
p.isrental = True
p.category = ''
p.save()

p = hmod.Products()
p.name = 'Colonial Hat'
p.currentPrice = '1.99'
p.description = 'A tricorn hat used in the late 1700s'
p.image = '/homepage/media/products/colonialhat.jpg'
p.isrental = True
p.category = ''
p.save()

p = hmod.Products()
p.name = 'Printer Breeches'
p.currentPrice = '30.99'
p.description = 'size 36x32 magenta colonial style'
p.image = '/homepage/media/products/breeches.jpeg'
p.isartisan = True
p.event = hmod.Events.objects.get(id=1)
p.category = ''
p.save()

p = hmod.Products()
p.name = 'Colonial Hat'
p.currentPrice = '20.99'
p.description = 'A tricorn hat used in the late 1700s'
p.image = '/homepage/media/products/colonialhat.jpg'
p.isartisan = True
p.event = hmod.Events.objects.get(id=1)
p.category = ''
p.save()



w = hmod.WardrobeItem()
w.size = 'mens 10'
w.Mmodifier = 'narrow'
w.gender = 'male'
w.color = 'brown'
w.pattern = ''
w.startYear = '1710'
w.endYear = '1780'
w.note = "runs big"
w.save()

rp = hmod.Rental_Product()
rp.name = 'Colonial Hat'
rp.currentPrice = '20.99'
rp.description = 'A tricorn hat used in the late 1700s'
rp.image = '/homepage/media/products/colonialhat.jpg'
rp.category = ''
rp.times_rented = '4'
rp.price_per_day = '2.00'
rp.replacement_price = '20.00'
rp.save()

sai = hmod.SaleItems()
sai.name = 'Pistol'
sai.description = ''
sai.lowPrice = '15.00'
sai.highPrice = '20.00'
sai.save()

ri = hmod.Rented_Item()
ri.amount = '12.99'
#ri.transaction = hmod.Transaction.objects.get(tracking_number='10')
ri.date_out = '2015-03-01'
ri.date_due = '2015-05-03'
ri.date_in = None
ri.discount_percent = '0.00'
#ri.rental_product = hmod.Rental_Product.objects.get(serial_number='0005')
ri.renter = hmod.Users.objects.get(username='cjpwrs')
ri.save()
print("Rental Made")

ri = hmod.Rented_Item()
ri.amount = '5.99'
#ri.transaction = hmod.Transaction.objects.get(tracking_number='15')
ri.date_out = '2015-03-09'
ri.date_due = '2015-05-09'
ri.date_in = None
ri.discount_percent = '0.00'
#ri.rental_product = hmod.Rental_Product.objects.get(serial_number='0006')
ri.renter = hmod.Users.objects.get(username='cjpwrs')
ri.save()
print("Rental Made")




hf = hmod.HistoricalFigures()
hf.name = 'Paul Revere'
hf.birthDate = '1720-06-26'
hf.birthPlace = 'Boston'
hf.deathDate = '1789-12-08'
hf.deadPlace = 'Boston'
hf.biographicalNote = 'Paul Revere was a member of the Sons of Liberty that is famous for riding his horse to warn the Americans that the British were coming'
hf.is_functional = 'True'
hf.save()


ro = hmod.Role()
ro.name = 'Lawyer John Adams'
ro.type = 'Real Person'
ro.save()