from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def login_user(req):
	if req.method == 'POST':
		uname = req.POST['username']
		passw = req.POST['password']
		user = authenticate(req,username=uname, password=passw)
		if (user is not None) and (uname == 'admin'):
			login(req,user)
			return redirect('ncertuser')
		elif (user is not None) and (uname == 'teacher'):
			login(req,user)
			return redirect('teacheruser')
		elif (user is not None) and (uname == 'district'):
			login(req,user)
			return redirect('districtuser')
		elif (user is not None) and (uname == 'school'):
			login(req,user)
			return redirect('schooluser')
		elif (user is not None) and (uname == 'state'):
			login(req,user)
			return redirect('stateuser')	
	return render(req,'lms/login.html',{})


def home(req):
	return render(req,'lms/home.html',{})	

# def ncertAdmin(req):
# 	return render(req,'lms/ncertuser.html',{})

def districtManagement(req):
	return render(req,'lms/dmuser.html',{})

def schoolManagement(req):
	return render(req,'lms/smuser.html',{})

def teacherUser(req):
	return render(req,'lms/teacheruser.html',{})

def logout_user(req):
	logout(req)
	return render(req,'lms/home.html',{})

def infoAndUpdate(req):
	return render(req,'lms/informationandupdate.html',{})

def ncertInfoAndUpdate(req):
	return render(req,'lms/ncertuser/ncertinformationandupdate.html',{})

def stateUser(req):
	return render(req,'lms/stateuser.html',{'content': 'stateuser'})	

# def userManagement(req):
# 	return render(req,'lms/ncertuser/usermanagement.html',{})	

def ncertAdmin(req):
	return render(req,'lms/ncertuser.html',{'content': 'ncertuser'})	

# def ncertAdmin(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             messages.success(request,('You successfully Registered user'))
#             return redirect('ncertuser')
#     else:
#         form = UserCreationForm()
#     return render(request, 'lms/ncertuser.html', {'form': form})


#	NCERT USER PANEL
def userManagement(request):
	if request.method == 'POST':
	    form = UserCreationForm(request.POST)
	    if form.is_valid():
	        form.save()
	        username = form.cleaned_data.get('username')
	        raw_password = form.cleaned_data.get('password1')
	        user = authenticate(username=username, password=raw_password)
	        # login(request, user)
	        messages.success(request,('You successfully Registered user'))
	        return redirect('userManagement')
	else:
	    form = UserCreationForm()
	return render(request, 'lms/ncertuser/usermanagement.html', {'form': form})


def learningOutcomeReport(req):
	return render(req,'lms/ncertuser/learningoutcomereport.html',{})	

def resourceManagement(req):
	return render(req,'lms/ncertuser/resourcemanagement.html',{})	



def informationAndUpdate(req):
	return render(req,'lms/ncertuser/informationandupdate.html',{})	

def supportAndSupervision(req):
	return render(req,'lms/ncertuser/supportandsupervision.html',{})	

def teacherPerformance(req):
	return render(req,'lms/ncertuser/support/teacherperformance.html',{})

def performanceMapping(req):
	return render(req,'lms/ncertuser/support/teacherperformance/mappingbased.html',{})	

def performanceEvidence(req):
	return render(req,'lms/ncertuser/support/teacherperformance/evidencebased.html',{})	

def studentPerformance(req):
	return render(req,'lms/ncertuser/support/studentperformance.html',{})

def teacherSupport(req):
	return render(req,'lms/ncertuser/support/teachersupport.html',{})	

def studentSupport(req):
	return render(req,'lms/ncertuser/support/studentsupport.html',{})	

def newUpload(req):
	return render(req,'lms/ncertuser/resourcemanagement/newupload.html',{})	

def reviewUpload(req):
	return render(req,'lms/ncertuser/resourcemanagement/reviewupload.html',{})	


# Teacher USER PANEL
def activityPlan(req):
	return render(req,'lms/teacheruser/activityplan.html',{})	

def uploadEvidence(req):
	return render(req,'lms/teacheruser/uploadevidence.html',{})	

def lowestLearningOutcome(req):
	return render(req,'lms/teacheruser/lowestlearningoutcome.html',{})	

def studentLearningOutcome(req):
	return render(req,'lms/teacheruser/studentlearningoutcome.html',{})	


def progressReport(req):
	return render(req,'lms/teacheruser/progressreport.html',{})	


def viewContentAndResource(req):
	return render(req,'lms/teacheruser/viewcontentandresource.html',{})	

#state


def stateProgressReport(req):
	return render(req,'lms/stateuser/progressreport.html',{})	

def stateDistrictManagement(req):
	return render(req,'lms/stateuser/districtmanagement.html',{})	

def stateResourceManagement(req):
	return render(req,'lms/stateuser/resourcemanagement.html',{})		


def stateSupportAndSupervision(req):
	return render(req,'lms/stateuser/supportandsupervision.html',{})

def stateInformationAndUpdate(req):
	return render(req,'lms/stateuser/informationandupdate.html',{})

def stateFeedback(req):
	return render(req,'lms/stateuser/feedback.html',{})

	#statesupprtandsupervision	

def stateTeacherPerformance(req):
	return render(req,'lms/stateuser/support/teacherperformance.html',{})	


def stateTeacherSupport(req):
	return render(req,'lms/stateuser/support/teachersupport.html',{})	

def stateDistrictSupport(req):
	return render(req,'lms/stateuser/support/districtsupport.html',{})	

def stateStudentSupport(req):
	return render(req,'lms/stateuser/support/studentsupport.html',{})	

def stateStudentPerformance(req):
	return render(req,'lms/stateuser/support/studentperformance.html',{})

def stateInformationAndUpdate(req):
	return render(req,'lms/stateuser/support/informationandupdate.html',{})	