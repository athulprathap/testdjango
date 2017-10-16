from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm, UsersRegisterForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .testscript import es_class
from elasticsearch import Elasticsearch, RequestsHttpConnection
import requests

def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect("/")
	return render(request, "accounts/form.html", {
		"form" : form,
		"title" : "Login",
	})


def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def register_view(request):
	form = UsersRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		return redirect("/accounts/login")
	return render(request, "accounts/form.html", {
		"title" : "Register",
		"form" : form,
	})


def elasticsearch_view(request):
	#if request.method == 'POST':
	#	import subprocess
		#output = subprocess.check_output(["C:\Users\sp00452423\adobepro1\accounts\testscript.py", "--", request.POST['es']])
	#output = es_class
	#print(output.connect(request))
	#res = requests.get("https://476b88cf7673e52be40c536ef8ff2ff3.us-east-1.aws.found.io:9243/")
	es = Elasticsearch(
            ["476b88cf7673e52be40c536ef8ff2ff3.us-east-1.aws.found.io"],
            connection_class=RequestsHttpConnection,
            http_auth=("elastic", "testdjango123$"),
            port=9243,
            use_ssl=False,
            verify_certs=False,
             #ca_certs=certifi.where(),
        )
	# print(res)
	# return res
	# connect to our cluster
	#es = Elasticsearch([{'host': '476b88cf7673e52be40c536ef8ff2ff3.us-east-1.aws.found.io', 'port': 9243}])
	mapping = {
		"type1": {
			"properties": {
				"field1": {"type": "text"}
			}
		}
	}
	#create index
	es.indices.create(index="adobe-index", body=mapping)
	#insert
	res = es.index(index='adobe-index', doc_type='test11', id=1, body={'test': 'success'})
	#return res
	return HttpResponse(res)
		#return HttpResponseRedirect(output, content_type='text/plain')
	#return render(request, "accounts/form.html", {
	#	"title": "Register",
	#	"form": output,
	#})