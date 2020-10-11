from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.UsersBL import UsersBL as ubl
from ..BL.ContactsBL import ContactsBL as cbl
from ..BL.PasswordsBL import PasswordsBL as pbl
from ..Models import *
import json
class SignUp:
	def addUser(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)

			uco = Contact.Contact();
			uco.contacttype_id = 1
			uco.salutation = ud['salutation']
			uco.firstName = ud['firstName']
			uco.middleName = ud['middleName']
			uco.lastName = ud['lastName']
			uco.mobileNumber = ud['mobileNumber']
			uco.isActive = True
			
			uco = cbl.addContact(uco)
			
			udo = User.User()
			udo.contact_id = uco.id
			udo.username = ud['username']
			udo.emailAddr = ud['emailAddr']
			udo.userRole_id = 1

			udo = ubl.addUser(udo)

			upo = Password.Password();
			upo.user_id = udo.Id
			upo.password = ud['password']
			upo.isActive = True
			pbl.addPassword(upo)

			sjo = JsonStandardOutput.JsonStandardOutput()
			sjo.data = udo

		return HttpResponse(Common.Common().ConverttoJson(sjo), content_type="application/json")