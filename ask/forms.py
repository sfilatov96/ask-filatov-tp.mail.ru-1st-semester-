from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from ask.models import CustomUser,Question,Answer

class AnswerForm(forms.Form):
	answer = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control ask-message','placeholder':'Text........'}))

	def SaveAnswer(self,request,qnum):
		if self.is_valid():
			answer = self.cleaned_data.get('answer')
			u = User.objects.get(username = request.user)
			c = CustomUser.objects.get(user = u)
			q = Question.objects.get(id = qnum)
			a = Answer.objects.create(user = c,question = q,text = answer)
			a.save()
			return True
		else: 
			return False
class AskForm(forms.Form):
	theme = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Them'}))
	tags = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'#tag'}))
	question = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control ask-message','placeholder':'Text........'}))

	def AskUser(self,request):
		user = request.user
		if form.is_valid():
			theme = form.cleaned_data.get('theme')
			quest = form.cleaned_data.get('question')
			c = CustomUser.objects.get(user = user)
			
			q = Question(user=c,title=theme,text=quest)
			q.save()
			tags = form.cleaned_data.get('tags').split(',')
			for tag in tags:
				if ' ' in tag:
					tag = tag.replace(' ', '_')
				try:
					t = Tag.objects.get(name=tag)
				except Tag.DoesNotExist:
					t = Tag.objects.create(name=tag)
					t.save()

				q.tags.add(t)
			redirect_to= '/question/'+str(q.id)+'/'
			return True
		else:
			return False


class Profile(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nickname'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	avatar = forms.ImageField()

	def SaveProfile(self,request):
		if self.is_valid():
			username_data = self.cleaned_data.get('username')
			email_data = self.cleaned_data.get('email')
			password_data = self.cleaned_data.get('password')
			repeat_data = self.cleaned_data.get('repeat')
			avatar_data = self.cleaned_data.get('avatar')
			u = User.objects.get(username = request.user)
			if username_data:
				u.username = username_data
			if email_data:
				u.email = email_data
			if password_data and repeat_data and password_data == repeat_data:
				u.password = password_data
			if avatar_data:
				u.avatar = avatar_data
			user.save()
			return True
		else: 
			return False


class UserForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nickname'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	def SaveUser(self,request):
		if self.is_valid():
			username_data = self.cleaned_data.get('username')
			email_data = self.cleaned_data.get('email')
			password_data = self.cleaned_data.get('password')
			repeat_data = self.cleaned_data.get('repeat')
			#found = User.objects.get(email=email_data)
			#if found:
			if password_data == repeat_data:
				user = User.objects.create_user(username_data,email_data,password_data)
				c = CustomUser(user=user)
				user.save()
				c.save()
				return True
			else:
				return False
			#else:
			#	return False
		else: 
			return False



class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	def LoginUser(self,request):
		if self.is_valid():
			user = auth.authenticate(username=self.cleaned_data.get('username'),password=self.cleaned_data.get('password'))
			if user is not None:
				auth.login(request,user)
				return True
			else:
				return False
		else:
			return False