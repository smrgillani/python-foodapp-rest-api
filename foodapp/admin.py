from django.contrib import admin
from .Entities.Users import Users
from .Entities.Contacts import Contacts
from .Entities.ContactTypes import ContactTypes
from .Entities.Currencies import Currencies
from .Entities.Countries import Countries
from .Entities.Cities import Cities
from .Entities.LocalAddresses import LocalAddresses
from .Entities.UserRoles import UserRoles
from .Entities.Passwords import Passwords

# Register your models here.
admin.site.register(Users)
admin.site.register(Contacts)
admin.site.register(ContactTypes)
admin.site.register(Currencies)
admin.site.register(Countries)
admin.site.register(Cities)
admin.site.register(LocalAddresses)
admin.site.register(UserRoles)
admin.site.register(Passwords)