from ..DAL.CountriesDAL import CountriesDAL as ct
from ..Models.Country import Country

class CountriesBL():

	def allCountries():
		act = ct.allCountries()
		Countries = list()
		for i in act:
			cntry = Country()
			cntry.Id = i.id
			cntry.currency_id = i.currency_id
			cntry.fullName = i.fullName
			cntry.ISO = i.ISO
			cntry.PhoneCode = i.PhoneCode
			cntry.isActive = i.isActive
			Countries.append(cntry)
		return Countries

	def addCountry(ico):
		rcto = ct.addCountry(ico)
		cntry = Country();
		cntry.Id = rcto.id
		cntry.currency_id = rcto.currency_id
		cntry.fullName = rcto.fullName
		cntry.ISO = rcto.ISO
		cntry.PhoneCode = rcto.PhoneCode
		cntry.isActive = rcto.isActive
		return cntry

	def selectCountry(ico):
		rcto = ct.selectOneCountry(ico)
		cntry = Country();
		cntry.Id = rcto.id
		cntry.currency_id = rcto.currency_id
		cntry.fullName = rcto.fullName
		cntry.ISO = rcto.ISO
		cntry.PhoneCode = rcto.PhoneCode
		cntry.isActive = rcto.isActive
		return cntry

	def updateCountry(ico):
		rcto = ct.updateCountry(ico)
		cntry = Country();
		cntry.Id = rcto.id
		cntry.currency_id = rcto.currency_id
		cntry.fullName = rcto.fullName
		cntry.ISO = rcto.ISO
		cntry.PhoneCode = rcto.PhoneCode
		cntry.isActive = rcto.isActive
		return cntry

	def deleteCountry(ico):
		rcto = ct.deleteCountry(ico)
		return rcto