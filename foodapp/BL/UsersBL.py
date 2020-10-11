from ..DAL.UsersDAL import UsersDAL as ud
from .ContactsBL import ContactsBL as cbl
from ..Models.User import User
from ..Models.Contact import Contact

class UsersBL():

	def allUsers():
		au = ud.allUsers()
		Users = list()
		for i in au:
			usr = User()
			usr.contact_id = i.contact_id
			usr.username = i.username
			usr.emailAddr = i.emailAddr
			Users.append(usr)
		return Users

	def addUser(ico):
		ruo = ud.addUser(ico)
		Usr = User();
		Cntct = Contact();
		Cntct.Id = ruo.contact_id
		Usr.contact = cbl.selectContact(Cntct)
		Usr.Id = ruo.unq_id
		Usr.username = ruo.username
		Usr.emailAddr = ruo.emailAddr
		Usr.isActive = ruo.isActive
		return Usr

	def latestUser():
		ruo = ud.getLatestUser()
		Usr = User();
		Cntct = Contact();
		Cntct.Id = ruo.contact_id
		Usr.contact = cbl.selectContact(Cntct)
		Usr.Id = ruo.unq_id
		Usr.username = ruo.username
		Usr.emailAddr = ruo.emailAddr
		return Usr

	def selectUserbyUsername(ico):
		ruo = ud.selectUserbyUsername(ico)
		Usr = User();
		Cntct = Contact();
		Cntct.Id = ruo.contact_id
		Usr.contact = cbl.selectContact(Cntct)
		Usr.Id = ruo.unq_id
		Usr.username = ruo.username
		Usr.emailAddr = ruo.emailAddr
		return Usr