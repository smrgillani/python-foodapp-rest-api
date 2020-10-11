from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.UsersBL import UsersBL as ubl
from ..Models import *
import json
class UserController:
	def loginUser(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			Usr = User.User();
			Usr.emailAddr = ud['emailorusername']
			Usr = ubl.selectUserbyUsername(Usr)
		return HttpResponse(Common.Common().ConverttoJson(Usr), content_type="application/json")

	def latestUser(self,request):
		return HttpResponse(Common.Common().ConverttoJson(ubl.latestUser()), content_type="application/json")