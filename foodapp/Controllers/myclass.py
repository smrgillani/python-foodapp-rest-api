from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.UsersBL import UsersBL as bl
from ..Models.Common import *
import json
class MyClass:
	def index(self,request):
		if request.method == 'POST':
			y = json.loads(request.body)
			print('Data of Meta:' + y['meta'])
		au = bl.allUsers()
		return HttpResponse(Common().ConverttoJson(au), content_type="application/json")