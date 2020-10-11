from ..DAL.CitiesDAL import CitiesDAL as ct
from ..Models.City import City

class CitiesBL():

	def allCities():
		act = ct.allCities()
		Cities = list()
		for i in act:
			cty = City()
			cty.Id = i.id
			cty.country_id = i.country_id
			cty.fullName = i.fullName
			cty.PhoneCode = i.PhoneCode
			cty.PostalCode = i.PostalCode
			cty.isActive = i.isActive
			Cities.append(cty)
		return Cities

	def addCity(ico):
		rcto = ct.addCity(ico)
		cty = City();
		cty.Id = rcto.id
		cty.country_id = rcto.country_id
		cty.fullName = rcto.fullName
		cty.PhoneCode = rcto.PhoneCode
		cty.PostalCode = rcto.PostalCode
		cty.isActive = rcto.isActive
		return cty

	def selectCity(ico):
		rcto = ct.selectOneCity(ico)
		cty = City();
		cty.Id = rcto.id
		cty.country_id = rcto.country_id
		cty.fullName = rcto.fullName
		cty.PhoneCode = rcto.PhoneCode
		cty.PostalCode = rcto.PostalCode
		cty.isActive = rcto.isActive
		return cty

	def updateCity(ico):
		rcto = ct.updateCity(ico)
		cty = City();
		cty.Id = rcto.id
		cty.country_id = rcto.country_id
		cty.fullName = rcto.fullName
		cty.PhoneCode = rcto.PhoneCode
		cty.PostalCode = rcto.PostalCode
		cty.isActive = rcto.isActive
		return cty

	def deleteCity(ico):
		rcto = ct.deleteCity(ico)
		return rcto