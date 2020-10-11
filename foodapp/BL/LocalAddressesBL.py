from ..DAL.LocalAddressesDAL import LocalAddressesDAL as la
from ..Models.LocalAddress import LocalAddress

class LocalAddressesBL():

	def allLocalAddresses():
		ala = la.allLocalAddresses()
		LocalAddresses = list()
		for i in ala:
			LclAddr = LocalAddress()
			LclAddr.Id = i.id
			LclAddr.city_id = i.city_id
			LclAddr.fullAddress = i.fullAddress
			LclAddr.isActive = i.isActive
			LocalAddresses.append(LclAddr)
		return LocalAddresses

	def addLocalAddress(ico):
		rlao = la.addLocalAddress(ico)
		LclAddr = LocalAddress();
		LclAddr.Id = rlao.id
		LclAddr.city_id = rlao.city_id
		LclAddr.fullAddress = rlao.fullAddress
		LclAddr.isActive = rlao.isActive
		return LclAddr

	def selectLocalAddress(ico):
		rlao = la.selectOneLocalAddress(ico)
		LclAddr = LocalAddress();
		LclAddr.Id = rlao.id
		LclAddr.city_id = rlao.city_id
		LclAddr.fullAddress = rlao.fullAddress
		LclAddr.isActive = rlao.isActive
		return LclAddr

	def updateLocalAddress(ico):
		rlao = la.updateLocalAddress(ico)
		LclAddr = LocalAddress();
		LclAddr.Id = rlao.id
		LclAddr.city_id = rlao.city_id
		LclAddr.fullAddress = rlao.fullAddress
		LclAddr.isActive = rlao.isActive
		return LclAddr

	def deleteLocalAddress(ico):
		rlao = la.deleteLocalAddress(ico)
		return rlao