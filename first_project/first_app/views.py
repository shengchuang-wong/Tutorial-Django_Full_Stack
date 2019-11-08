from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
from first_app.forms import NewUserForm
# Create your views here.

def index(request):
  webpages_list = AccessRecord.objects.order_by('date')
  date_dict = { 'access_records': webpages_list }
  return render(request, 'first_app/index.html', context=date_dict)

def users(request):
  users_list = User.objects.order_by('first_name')
  context_dict = {'users': users_list}
  return render(request, 'first_app/users.html', context=context_dict)

def register(request):
  form = NewUserForm()
  if request.method == "POST":
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return users(request)
    else:
      print("ERROR! FORM INVALID!")

  return render(request, 'first_app/register.html', { 'form': form })