from ..DAL.CurrenciesDAL import CurrenciesDAL as cc
from ..Models.Currency import Currency

class CurrenciesBL():

	def allCurrencies():
		acc = cc.allCurrencies()
		Currencies = list()
		for i in acc:
			currncy = Currency()
			currncy.Id = i.id
			currncy.fullName = i.fullName
			currncy.Sign = i.Sign
			currncy.isActive = i.isActive
			Currencies.append(currncy)
		return Currencies

	def addCurrency(ico):
		rcco = cc.addCurrency(ico)
		currncy = Currency();
		currncy.Id = rcco.id
		currncy.fullName = rcco.fullName
		currncy.Sign = rcco.Sign
		currncy.isActive = rcco.isActive
		return currncy

	def selectCurrency(ico):
		rcco = cc.selectOneCurrency(ico)
		currncy = Currency();
		currncy.Id = rcco.id
		currncy.fullName = rcco.fullName
		currncy.Sign = rcco.Sign
		currncy.isActive = rcco.isActive
		return currncy

	def updateCurrency(ico):
		rcco = cc.updateCurrency(ico)
		currncy = Currency();
		currncy.Id = rcco.id
		currncy.fullName = rcco.fullName
		currncy.Sign = rcco.Sign
		currncy.isActive = rcco.isActive
		return currncy

	def deleteCurrency(ico):
		rcco = cc.deleteCurrency(ico)
		return rcco