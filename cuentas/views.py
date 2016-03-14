from django.shortcuts import render
from django.views.generic import View

class LoginView(View):
	def get(self,request):
		template_name="cuentas/login.html"
		return render(request,template_name)

