from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from random import randrange
from EmailAuth.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def usignup(request):
	if request.method == "POST":
		un=request.POST.get('un')
		em=request.POST.get('em')
		try:
			usr=User.objects.get(username=un)
			return render(request,'usignup.html',{'msg':'Username Taken'})
		except User.DoesNotExist :
			try:
				usr=User.objects.get(email=em)
				return render(request,'usignup.html',{'msg':'This Email is already registered'})
			except User.DoesNotExist :
				pw=""
				text="1234567890"

				for i in range(3):
					pw+=text[randrange(len(text))]
				print(pw)
				subject="Welcome to Rahul's Wall!"
				msg="Please Find the otp for Your Login @ rahulbhatia.tech "+"\n Username:"+str(un)+"\n password:"+str(pw)
				
				usr=User.objects.create_user(username=un,email=em,password=pw)
				send_mail(subject,msg,EMAIL_HOST_USER,[em])
				messages.info(request,"Password  sent on your email")
				usr.save()
				return redirect('ulogin')
	else:
		return render(request,'usignup.html')

def ulogin(request):
	if request.method =="POST":
		un=request.POST.get('un')
		pw=request.POST.get('pw')
		usr=authenticate(username=un,password=pw)
		print('None',usr)
		if usr is None:
			return render(request,'ulogin.html',{'msg':'No user Found'})
		else:
			login(request,usr)
			return redirect('home')
	else:
		return render(request,'ulogin.html')

def ulogout(request):
	logout(request)
	return redirect('ulogin')



def uresetpass(request):
	if request.method == "POST":
		un=request.POST.get('un')
		em=request.POST.get('em')
		try:
			usr=User.objects.get(username=un) and User.objects.get(email=em)  
			pw=""
			text="1234567890"
			for i in range(3):
				pw+=text[randrange(len(text))]
			print(pw)
			subject="Welcome to Rahul's Wall!"
			msg="Please Find the otp for your CHANGE PASSWORD REQUEST @ rahulbhatia.tech "+"\n Username:"+str(un)+"\n password:"+str(pw)
			send_mail(subject,msg,EMAIL_HOST_USER,[em])
			messages.info(request,"Password  sent on your email")
			usr.set_password(pw)
			usr.save()
			return redirect('ulogin')
		except User.DoesNotExist:
			return render(request,'uresetpass.html',{'msg':'Username/Email doesnot exists'})
	else:
		return render(request,'uresetpass.html')




