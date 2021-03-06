from django.urls import path
from .import views
from airline import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # leave as empty string fo base url
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),

    path('homepage/', views.homepage, name="homepage"),
    path('addairport/', views.addairport, name="addairport"),
    path('changeEmail/', views.changeEmail, name="changeEmail"),
    path('changePassword/', views.changePassword, name="changePassword"),
    path('creditcards/', views.creditcards, name="creditcards"),
    path('delete_creditcard/<int:pk>', views.delete_creditcard, name="delete_creditcard"),
    path('delete_ticket/<int:pk>', views.delete_ticket, name="delete_ticket"),
    path('cancel_flight/<int:id>', views.cancel_flight, name="cancel_flight"),
    path('response_feedback/<int:id>', views.response_feedback, name="response_feedback"),
    path('feedbacklist', views.feedbacklist , name="feedbacklist"),

    path('completed/', views.completed, name="completed"),
    path('myflights/', views.myflights, name="myflights"),
    path('buyticket/<str:values>', views.buyticket, name="buyticket"),
    path('choose_class/<int:id>', views.choose_class, name="choose_class"),
    path('selected_flight/<int:flight_id>', views.selected_flight, name="selected_flight"),
    path('ticket_has_been_purchased/<int:id>', views.ticket_has_been_purchased, name="ticket_has_been_purchased"),
    path('view_ticket/<int:id>', views.view_ticket, name="view_ticket"),
    path('cancel_ticket/<int:id>', views.cancel_ticket, name="cancel_ticket"),

    path('checkin/', views.checkin, name="checkin"),
    path('FeedbackPage/', views.FeedbackPage, name="FeedbackPage"),



    path('ChooseSeat/<str:values>', views.ChooseSeat, name="ChooseSeat"),

    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name="home/password_reset.html") , name="reset_password"),
    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_sent.html") , name="password_reset_done"),
    path('reser/<uidb64>/<token>' , auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_form.html") ,name="password_reset_confirm"),
    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_done.html") , name="password_reset_complete"),


   ]
