from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ( 
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from parish.forms import UserRegisterForm

from parish.models import (
    Committee, 
    Community, 
    Contribution, 
    Member,
    Priest,
    SubParish
)

# Create your views here.

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "parish/layout/home.html"

#* CRUD for Priest Model

class BasePriestView(LoginRequiredMixin,View):
    model = Priest
    fields = '__all__'
    success_url = reverse_lazy('priest-list')

class PriestListView(BasePriestView,ListView):
    template_name = "parish/pages/priest/priest_list.html"
    
class PriestCreateView(BasePriestView,CreateView):
    template_name = "parish/pages/priest/priest_form.html"

class PriestDetailView(BasePriestView,DetailView):
    template_name = "parish/pages/priest/priest_detail.html"

class PriestUpdateView(BasePriestView,UpdateView):
    template_name = "parish/pages/priest/priest_form.html"

class PriestDeleteView(BasePriestView,DeleteView):
    template_name = "parish/pages/priest/priest_confirm_delete.html"

#* CRUD for Member Model

class BaseMemberView(LoginRequiredMixin,View):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('member-list')

class MemberListView(BaseMemberView,ListView):
    template_name = "parish/pages/member/member_list.html"
    
class MemberCreateView(BaseMemberView,CreateView):
    template_name = "parish/pages/member/member_form.html"

class MemberDetailView(BaseMemberView,DetailView):
    template_name = "parish/pages/member/member_detail.html"

class MemberUpdateView(BaseMemberView,UpdateView):
    template_name = "parish/pages/member/member_form.html"

class MemberDeleteView(BaseMemberView,DeleteView):
    template_name = "parish/pages/member/member_confirm_delete.html"

#* CRUD for Community Model
class BaseCommunityView(LoginRequiredMixin,View):
    model = Community
    fields = '__all__'
    success_url = reverse_lazy('community-list')

class CommunityListView(BaseCommunityView,ListView):
    template_name = "parish/pages/community/community_list.html"
    
class CommunityCreateView(BaseCommunityView,CreateView):
    template_name = "parish/pages/community/community_form.html"

class CommunityDetailView(BaseCommunityView,DetailView):
    template_name = "parish/pages/community/community_detail.html"

class CommunityUpdateView(BaseCommunityView,UpdateView):
    template_name = "parish/pages/community/community_form.html"

class CommunityDeleteView(BaseCommunityView,DeleteView):
    template_name = "parish/pages/community/community_confirm_delete.html"

#* CRUD for Contribution Model
class BaseContributionView(LoginRequiredMixin,View):
    model = Contribution
    fields = '__all__'
    success_url = reverse_lazy('contribution-list')

class ContributionListView(BaseContributionView,ListView):
    template_name = "parish/pages/contribution/contribution_list.html"
    
class ContributionCreateView(BaseContributionView,CreateView):
    template_name = "parish/pages/contribution/contribution_form.html"

class ContributionDetailView(BaseContributionView,DetailView):
    template_name = "parish/pages/contribution/contribution_detail.html"

class ContributionUpdateView(BaseContributionView,UpdateView):
    template_name = "parish/pages/contribution/contribution_form.html"

class ContributionDeleteView(BaseContributionView,DeleteView):
    template_name = "parish/pages/contribution/contribution_confirm_delete.html"

#* CRUD for Committee Model

class BaseCommitteeView(LoginRequiredMixin,View):
    model = Committee
    fields = '__all__'
    success_url = reverse_lazy('committee-list')

class CommitteeListView(BaseCommitteeView,ListView):
    template_name = "parish/pages/committee/commitee_list.html"
    
class CommitteeCreateView(BaseCommitteeView,CreateView):
    template_name = "parish/pages/committee/committee_form.html"

class CommitteeDetailView(BaseCommitteeView,DetailView):
    template_name = "parish/pages/committee/committee_detail.html"

class CommitteeUpdateView(BaseCommitteeView,UpdateView):
    template_name = "parish/pages/committee/committee_form.html"

class CommitteeDeleteView(BaseCommitteeView,DeleteView):
    template_name = "parish/pages/committee/committee_confirm_delete.html"

#* CRUD for SubParish Model

class BaseSubParishView(LoginRequiredMixin,View):
    model = SubParish
    fields = '__all__'
    success_url = reverse_lazy('subparish-list')

class SubParishListView(BaseSubParishView,ListView):
    template_name = "parish/pages/subparish/subparish_list.html"
    
class SubParishCreateView(BaseSubParishView,CreateView):
    template_name = "parish/pages/subparish/subparish_form.html"

class SubParishDetailView(BaseSubParishView,DetailView):
    template_name = "parish/pages/subparish/subparish_detail.html"

class SubParishUpdateView(BaseSubParishView,UpdateView):
    template_name = "parish/pages/subparish/subparish_form.html"

class SubParishDeleteView(BaseSubParishView,DeleteView):
    template_name = "parish/pages/subparish/subparish_confirm_delete.html"

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Hi {username}, you have been created an account. Login now")
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'parish/auth/register.html', context)