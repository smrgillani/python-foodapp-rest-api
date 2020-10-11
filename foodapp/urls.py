"""foodapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
"""
from .FolderName.FileName import ClassName

upper statement means import a class from a file which exist in a folder 

.			=>	current Folder where urls.py reside
FolderName	=>	Controllers is a folder name
FileName	=>	MyClass is a file which exists in Controllers folder as MyClass.py
ClassName	=>	MyClass is Python class which syntax exists in MyClass.py

"""
from .Controllers import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:question_id>/', myclass.MyClass().detail, name='detail'),
    path('register', SignUp.SignUp().addUser, name='addUser'),
    #Contact Type Module
    path('allcontacttypes', ContactTypeController.ContactTypeController().allContactTypes, name='allContactTypes'),
    path('addcontacttype', ContactTypeController.ContactTypeController().addContactType, name='addContactType'),
    path('selectcontacttype', ContactTypeController.ContactTypeController().selectContactType, name='selectContactType'),    
    path('updatecontacttype', ContactTypeController.ContactTypeController().updateContactType, name='updateContactType'),
    path('deletecontacttype', ContactTypeController.ContactTypeController().deleteContactType, name='deleteContactType'),
    #Contact Type Module
    path('allcurrencies', CurrencyController.CurrencyController().allCurrencies, name='allCurrencies'),
    path('addcurrency', CurrencyController.CurrencyController().addCurrency, name='addCurrency'),
    path('selectcurrency', CurrencyController.CurrencyController().selectCurrency, name='selectCurrency'),    
    path('updatecurrency', CurrencyController.CurrencyController().updateCurrency, name='updateCurrency'),
    path('deletecurrency', CurrencyController.CurrencyController().deleteCurrency, name='deleteCurrency'),
    #Country Type Module
    path('allcountries', CountryController.CountryController().allCountries, name='allCountries'),
    path('addcountry', CountryController.CountryController().addCountry, name='addaddCountry'),
    path('selectcountry', CountryController.CountryController().selectCountry, name='selectCountry'),    
    path('updatecountry', CountryController.CountryController().updateCountry, name='updateCountry'),
    path('deletecountry', CountryController.CountryController().deleteCountry, name='deleteCountry'),
    #City Type Module
    path('allcities', CityController.CityController().allCities, name='allCities'),
    path('addcity', CityController.CityController().addCity, name='addCity'),
    path('selectcity', CityController.CityController().selectCity, name='selectCity'),    
    path('updatecity', CityController.CityController().updateCity, name='updateCity'),
    path('deletecity', CityController.CityController().deleteCity, name='deleteCity'),
    #Local Address Type Module
    path('alllocaladdresses', LocalAddressController.LocalAddressController().allLocalAddresses, name='allLocalAddresses'),
    path('addlocaladdress', LocalAddressController.LocalAddressController().addLocalAddress, name='addLocalAddress'),
    path('selectlocaladdress', LocalAddressController.LocalAddressController().selectLocalAddress, name='selectLocalAddress'),    
    path('updatelocaladdress', LocalAddressController.LocalAddressController().updateLocalAddress, name='updateLocalAddress'),
    path('deletelocaladdress', LocalAddressController.LocalAddressController().deleteLocalAddress, name='deleteLocalAddress'),
    #User Role Type Module
    path('alluserroles', UserRoleController.UserRoleController().allUserRoles, name='allUserRoles'),
    path('adduserrole', UserRoleController.UserRoleController().addUserRole, name='addUserRole'),
    path('selectuserrole', UserRoleController.UserRoleController().selectUserRole, name='selectUserRole'),    
    path('updateuserrole', UserRoleController.UserRoleController().updateUserRole, name='updateUserRole'),
    path('deleteuserrole', UserRoleController.UserRoleController().deleteUserRole, name='deleteUserRole'),
    #System Permission Type Module
    path('allsystempermissions', SystemPermissionController.SystemPermissionController().allSystemPermissions, name='allSystemPermissions'),
    path('addsystempermission', SystemPermissionController.SystemPermissionController().addSystemPermission, name='addSystemPermission'),
    path('selectsystempermission', SystemPermissionController.SystemPermissionController().selectSystemPermission, name='selectSystemPermission'),    
    path('updatesystempermission', SystemPermissionController.SystemPermissionController().updateSystemPermission, name='updateSystemPermission'),
    path('deletesystempermission', SystemPermissionController.SystemPermissionController().deleteSystemPermission, name='deleteSystemPermission'),
    #System Permission Type Module
    path('alluserpermissions', UserPermissionController.UserPermissionController().allUserPermissions, name='allUserPermissions'),
    path('adduserpermission', UserPermissionController.UserPermissionController().addUserPermission, name='addUserPermission'),
    path('selectuserpermission', UserPermissionController.UserPermissionController().selectUserPermission, name='selectUserPermission'),    
    path('updateuserpermission', UserPermissionController.UserPermissionController().updateUserPermission, name='updateUserPermission'),
    path('deleteuserpermission', UserPermissionController.UserPermissionController().deleteUserPermission, name='deleteUserPermission'),
    #System Permission Type Module
    path('latestuser', UserController.UserController().latestUser, name='latestUser'),
    path('loginuser', UserController.UserController().loginUser, name='loginUser')
    # path('adduserpermission', UserPermissionController.UserPermissionController().addUserPermission, name='addUserPermission'),
    # path('selectuserpermission', UserPermissionController.UserPermissionController().selectUserPermission, name='selectUserPermission'),    
    # path('updateuserpermission', UserPermissionController.UserPermissionController().updateUserPermission, name='updateUserPermission'),
    # path('deleteuserpermission', UserPermissionController.UserPermissionController().deleteUserPermission, name='deleteUserPermission')
]
