
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('ncertadmin/',views.ncertAdmin, name = 'ncertuser'),
    path('districtmanagement/',views.districtManagement, name = 'districtuser'),
    path('schoolmanagement/',views.schoolManagement, name = 'schooluser'),
    path('teacher/',views.teacherUser, name = 'teacheruser'),
    path('state/',views.stateUser, name = 'stateuser'),
    path('logout/',views.logout_user, name = 'logoutU'),
    path('login/',views.login_user, name = 'login'),
    path('info/',views.infoAndUpdate, name = 'infoandupdate'),
    path('ncertinfo/',views.ncertInfoAndUpdate, name = 'ncertinfoandupdate'),



    path('usermanagement/',views.userManagement, name = 'usermanage'),#ncert
    path('learning_outcome/',views.learningOutcomeReport, name = 'lout'),#ncert
    path('resource_management/',views.resourceManagement, name = 'rmanage'),#ncert
    path('information_and_update/',views.informationAndUpdate, name = 'infoup'),#ncert
    path('support_and_supervision/',views.supportAndSupervision, name = 'sas'),#ncert

    path('teacher_performance/',views.teacherPerformance, name = 'tp'),#ncert/support
    path('student_performance/',views.studentPerformance, name = 'sp'),#ncert/support
    path('teacher_support/',views.teacherSupport, name = 'ts'),#ncert/support
    path('student_support/',views.studentSupport, name = 'ss'),#ncert/support
    path('teacher_performance/mapping',views.performanceMapping, name = 'mapping'),#ncert/support/teacherperformance
    path('teacher_performance/evidence',views.performanceEvidence, name = 'evidencing'),#ncert/support/teacherperformance

    path('new_upload/',views.newUpload, name = 'newup'),#ncert/resourcemanagement
    path('review_upload/',views.reviewUpload, name = 'reviewup'),#ncert/resourcemanagement


    path('uploadevidence/',views.uploadEvidence, name = 'uploadEvi'),#teacher
    path('activityplan/',views.activityPlan, name = 'activityP'),#teacher
    path('llo/',views.lowestLearningOutcome, name = 'lowestlo'),#teacher
    path('student_learning_outcome/',views.studentLearningOutcome, name = 'slo'),#teacher
    path('progress_report/',views.progressReport, name = 'pr'),#teacher
    path('view_content_and_resource/',views.viewContentAndResource, name = 'vcar'),#teacher


    path('state/progress_report',views.stateProgressReport, name = 'pr'),#tstate
    path('state/district_management',views.stateDistrictManagement, name = 'dm'),#tstate
    path('state/resource_management',views.stateResourceManagement, name = 'rm'),#tstate
    path('state/support_and_supervision',views.stateSupportAndSupervision, name = 'statesas'),#tstate
    path('state/feedback',views.stateFeedback, name = 'feed'),#tstate

    path('state/support_and_supervision/teacher_performance/',views.stateTeacherPerformance, name = 'statetp'),#state/support
    path('state/support_and_supervision/teacher_support/',views.stateTeacherSupport, name = 'statets'),#state/support
    path('state/support_and_supervision/district_support/',views.stateDistrictSupport, name = 'stateds'),#state/support
    path('state/support_and_supervision/student_support/',views.stateStudentSupport, name = 'statess'),#state/support
    path('state/support_and_supervision/student_performance/',views.stateStudentPerformance, name = 'statesp'),#state/support
    path('state/support_and_supervision/information_and_update',views.stateInformationAndUpdate, name = 'iau'),#tstate





    

]