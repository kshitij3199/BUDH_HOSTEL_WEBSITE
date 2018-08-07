from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from . models import Complain
from django.urls import reverse_lazy
from braces.views import SelectRelatedMixin
#this is for function
from django.contrib.auth.decorators import login_required
#this is for class
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)


def home(request):
	return render(request, 'home.html')

class ComplainListView(ListView):
    model = Complain

    def get_queryset(self):
        return Complain.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')


class CreateComplainView(LoginRequiredMixin,SelectRelatedMixin,CreateView):




    model = Complain
    fields = ('title','text','room',)

    def form_valid(self,form):
    #    if UserProfileInfo.objects.get(user=self.request.user)== null:
    #        return redirect('/post')
        #if UserProfileInfo.objects.get(user=self.request.user).is_club_member== False:
        #    return redirect('/post')

                    self.object =form.save(commit=False)
                    self.object.name = self.request.user.first_name + " "+self.request.user.last_name
                    self.object.rollno = self.request.user.username
                    self.object.student_email = self.request.user.email

                    self.object.save()
                    return super().form_valid(form)
