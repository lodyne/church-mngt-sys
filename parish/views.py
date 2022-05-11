from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ( 
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from parish.models import (
    Committee, 
    Community, 
    Contribution, 
    Member,
    Priest,
    SubParish
)

# Create your views here.

class HomeView(TemplateView):
    template_name = "parish/layout/home.html"

#* CRUD for Priest Model

class BasePriestView(View):
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
    template_name = "parish/pages/priest/priest_confirm_detail.html"

#* CRUD for Member Model

class BaseMemberView(View):
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
    template_name = "parish/pages/member/member_confirm_detail.html"

#* CRUD for Community Model
class BaseCommunityView(View):
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
    template_name = "parish/pages/community/community_confirm_detail.html"

#* CRUD for Contribution Model
class BaseContributionView(View):
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
    template_name = "parish/pages/contribution/contribution_confirm_detail.html"

#* CRUD for Committee Model

class BaseCommitteeView(View):
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
    template_name = "pages/committee/committee_form.html"

class CommitteeDeleteView(BaseCommitteeView,DeleteView):
    template_name = "parish/pages/committee/committee_confirm_detail.html"

#* CRUD for SubParish Model

class BaseSbParishView(View):
    model = SubParish
    fields = '__all__'
    success_url = reverse_lazy('subparish-list')

class SubParishListView(BaseCommitteeView,ListView):
    template_name = "parish/pages/subparish/subparish_list.html"
    
class SubParishCreateView(BaseCommitteeView,CreateView):
    template_name = "parish/pages/subparish/subparish_form.html"

class SubParishDetailView(BaseCommitteeView,DetailView):
    template_name = "parish/pages/subparish/subparish_detail.html"

class SubParishUpdateView(BaseCommitteeView,UpdateView):
    template_name = "parish/pages/subparish/subparish_form.html"

class SubParishDeleteView(BaseContributionView,DeleteView):
    template_name = "parish/pages/subparish/subparish_confirm_detail.html"