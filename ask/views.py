from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, EmptyPage
from ask.paginator import paginate
from ask.models import Question, Answer, Tag, CustomUser
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ask.forms import UserForm,LoginForm,AskForm,Profile,AnswerForm
import json


pointer= 'class=active'

title= 'Tag:'
def index(request, page=None):
	#pager =Paginator(questions, 4)
	
	#qlist = pager.page(page or 1)
	try:
		questions=Question.objects.newest()
	except Question.DoesNotExist:
		raise Http404
	  
	questions_on_page = paginate(questions, request, 4, page)
	return render(request,'ask/index.html',{
		'questions':questions_on_page,
		'page' : page,
		}
	)

def question(request, page=None, qnum=None):
	try:
		q = Question.objects.get(id=qnum)
	except Question.DoesNotExist:
		raise Http404
	answers = Answer.objects.filter(question=qnum)
	answer_on_page = paginate(answers, request, 4, page)

	if request.POST:
		form = AnswerForm(request.POST)
		if form.SaveAnswer(request,qnum):
			redirect_to = '/question/'+qnum+'/'
			return HttpResponseRedirect(redirect_to)
		else:
			mistake = 'failed!'
			return render(request,'ask/question.html',{
				'form':form,
				'answers':answer_on_page,
				'qnum':qnum,
				'page' : page,
				'q':q,
				'mistake':mistake,
				}
		)

	else:
		form = AnswerForm()
		return render(request,'ask/question.html',{
			'form':form,
			'answers':answer_on_page,
			'qnum':qnum,
			'page' : page,
			'q':q
			}
		)
def tag(request, page=None, tag=None):
	t=Tag.objects.get(name=tag)
	q = Question.objects.filter(tags=t)
	#question_on_page = paginate(q, request, 4, page)
	return render(request,'ask/index.html',{
		'questions':q,
		'title':title,
		'tag':tag,
		'page' : page
		}
	)
def hot(request, page=None):
	questions=Question.objects.hot()
	question_on_page = paginate(questions, request, 4, page)
	return render(request,'ask/index.html',{
		'questions':question_on_page,
		'pointer_hot':pointer,
		'page' : page,
		}
	)

def login(request):
	try:
		redirect_to = request.GET['next']
	except KeyError:
		redirect_to = '/'

	if request.POST:
		form = LoginForm(request.POST) 
		if form.LoginUser(request):
			return HttpResponseRedirect(redirect_to)
		else:
			mistake = 'login or password are not correct,please try again'
			return render(request, 'ask/login.html', {'pointer_login':pointer,'form' : form,'redirecter':redirect_to,'mistake':mistake })
	else: 
		form = LoginForm() 
		return render(request, 'ask/login.html', {'pointer_login':pointer,'form' : form,'redirecter':redirect_to })

	
def logout(request):
	try:
		redirect_to = request.GET['next']
	except KeyError:
		redirect_to = '/'
	auth.logout(request)
	return HttpResponseRedirect(redirect_to)
def register(request):
	try:
		redirect_to = request.GET['next']
	except KeyError:
		redirect_to = '/'

	if request.POST:
		form = UserForm(request.POST)
		if form.SaveUser(request):
			return HttpResponseRedirect(redirect_to)
		else:
			mistake = 'sorry,password and repeated password are not the same,please try again'
			return render(request,'ask/register.html',{'pointer_register':pointer,'form':form,'mistake':mistake})
	else:
		form = UserForm()
		return render(request,'ask/register.html',{'pointer_register':pointer,'form':form})

@login_required(login_url='/login/')
def ask(request):
	if request.POST:
		form = AskForm(request.POST)
		if form.AskUser(request):
			return HttpResponseRedirect(redirect_to)
		else:
			return render(request,'ask/ask.html',{'pointer_ask':pointer,'form':form})
	else:
		form = AskForm()
		return render(request,'ask/ask.html',{'pointer_ask':pointer,'form':form})

def profile(request):
	user = request.user
	form = Profile(request.POST)
	if request.POST:
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			if username:
				user.username = username
				return HttpResponseRedirect('/')

			if password:
				user.username = username
				return HttpResponseRedirect('/')

			if email:
				user.email = email
				return HttpResponseRedirect('/')
		else:
			return render(request,'ask/profile.html',{'form':form})

	else:
		form = Profile()
		return render(request,'ask/profile.html',{'form':form})


