from ..Entities.Currencies import Currencies as cc
import datetime

class CurrenciesDAL:
	def allCurrencies():
		return cc.objects.all()
	def addCurrency(ico):
		return cc.objects.create(fullName=ico.fullName, Sign=ico.Sign, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneCurrency(ico):
		return cc.objects.get(id=ico.Id)
	def updateCurrency(ico):
		qrr = cc.objects.filter(id=ico.Id).update(fullName=ico.fullName, Sign=ico.Sign, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, cc.objects.get(id=ico.Id)) [qrr != 0]
	def deleteCurrency(ico):
		qrr = cc.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]