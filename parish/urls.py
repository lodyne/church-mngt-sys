from django.urls import path
from .views import (
    HomeView,
    PriestListView,
    PriestCreateView,
    PriestDetailView, 
    PriestUpdateView,
    PriestDeleteView,
    MemberListView,
    MemberCreateView,
    MemberDetailView,
    MemberUpdateView, 
    MemberDeleteView,
    CommunityListView,
    CommunityCreateView,
    CommunityDetailView,
    CommunityUpdateView,
    CommunityDeleteView,
    ContributionListView,
    ContributionCreateView,
    ContributionDetailView,
    ContributionUpdateView,
    ContributionDeleteView,
    CommitteeListView,
    CommitteeCreateView,
    CommitteeDeleteView,
    CommitteeUpdateView,
    CommitteeDetailView,
    SubParishListView,
    SubParishCreateView,
    SubParishDetailView,
    SubParishUpdateView,
    SubParishDeleteView,
)

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),

    #* urls for PriestViews

    path('priest/',PriestListView.as_view(), name = 'priest-list'),
    path('priest/new',PriestCreateView.as_view(), name = 'priest-create'),
    path('priest/<int:pk>',PriestDetailView.as_view(), name = 'priest-detail'),
    path('priest/<int:pk>/update',PriestUpdateView.as_view(), name = 'priest-update'),
    path('priest/<int:pk>/delete',PriestDeleteView.as_view(), name = 'priest-delete'),

    #* urls for CommunityViews

    path('community/',CommunityListView.as_view(), name = 'community-list'),
    path('community/new',CommunityCreateView.as_view(), name = 'community-create'),
    path('community/<int:pk>',CommunityDetailView.as_view(), name = 'community-detail'),
    path('community/<int:pk>/update',CommunityUpdateView.as_view(), name = 'community-update'),
    path('community/<int:pk>/delete',CommunityDeleteView.as_view(), name = 'community-delete'),

    #* urls for MemberViews

    path('member/',MemberListView.as_view(), name = 'member-list'),
    path('member/new',MemberCreateView.as_view(), name = 'member-create'),
    path('member/<int:pk>',MemberDetailView.as_view(), name = 'member-detail'),
    path('member/<int:pk>/update',MemberUpdateView.as_view(), name = 'member-update'),
    path('member/<int:pk>/delete',MemberDeleteView.as_view(), name = 'member-delete'),

    #* urls for CommitteeViews

    path('committee/',CommitteeListView.as_view(), name = 'committee-list'),
    path('committee/new',CommitteeCreateView.as_view(), name = 'committee-create'),
    path('committee/<int:pk>',CommitteeDetailView.as_view(), name = 'committee-detail'),
    path('committee/<int:pk>/update',CommitteeUpdateView.as_view(), name = 'committee-update'),
    path('committee/<int:pk>/delete',CommitteeDeleteView.as_view(), name = 'committee-delete'),

    #* urls for ContributionViews

    path('contribution/',ContributionListView.as_view(), name = 'contribution-list'),
    path('contribution/new',ContributionCreateView.as_view(), name = 'contribution-create'),
    path('contribution/<int:pk>',ContributionDetailView.as_view(), name = 'contribution-detail'),
    path('contribution/<int:pk>/update',ContributionUpdateView.as_view(), name = 'contribution-update'),
    path('contribution/<int:pk>/delete',ContributionDeleteView.as_view(), name = 'contribution-delete'),

    #* urls for SubParishViews

    path('subparish/',SubParishListView.as_view(), name = 'subparish-list'),
    path('subparish/new',SubParishCreateView.as_view(), name = 'subparish-create'),
    path('subparish/<int:pk>',SubParishDetailView.as_view(), name = 'subparish-detail'),
    path('subparish/<int:pk>/update',SubParishUpdateView.as_view(), name = 'subparish-update'),
    path('subparish/<int:pk>/delete',SubParishDeleteView.as_view(), name = 'subparish-delete'),
]