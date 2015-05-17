from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from book.models import Book, UserProfile
import datetime


def log_in(request):
	if request.method == 'GET':
		return render_to_response("login.html",context_instance=RequestContext(request))
	elif request.method == 'POST':
		user = authenticate(username=request.POST.get("username",False), password=request.POST.get("password",False))
		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect("/profile/")
			else:
				return render(request, "login.html",
							  {"error":"Your account has been disabled. Please contact a site admin!"})
		else:
			return render(request, "login.html",
						 {"error":"Credentials entered are incorrect. Please try again!"})

def log_out(request):
	logout(request)
	return HttpResponseRedirect("/")


@login_required
def profile(request):
	return render(request, "profile.html", {"books": Book.objects.filter(user=request.user.id)})

@login_required
def add_book(request):
	if request.method == 'POST':
		book = Book(user=request.user,
					title=request.POST.get("title"),
					author=request.POST.get("author"),
					reading_status=request.POST.get("status"),
					end_date=datetime.datetime.now())
		book.save()
		return HttpResponseRedirect("/profile")
	else:
		return HttpResponseNotAllowed(["POST"])

@login_required
def delete_book(request, id):
	book = Book.objects.filter(id=id)
	if book is not None:
		book.delete()
		#TODO: delete all QUOTES associated with book
	else:
		print "something's wrong"
	return HttpResponseRedirect("/profile")

@login_required
def friend_list(request):
	return render(request, "friends.html", {"info": UserProfile.objects.filter(user=request.user.id)})


