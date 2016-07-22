from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from possum_mdr import views

from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    #url(r'^login/?', views.login_user),
    url(r'^sign-up/?$', views.new_user_account),
    url(r'^sign-up/success/?$', TemplateView.as_view(template_name="registration_new/success.html")),

    url(r'^labs/?$', TemplateView.as_view(template_name="site/labs.html")),
    url(r'^labs/theseus/', include('theseus_data_matcher.urls',app_name="theseus",namespace="theseus")),
    url(r'^labs/plate/', include('django_spaghetti.urls',namespace="spaghetti")),

    
    url(r'^share/', include('aristotle_sharing.urls',app_name="aristotle_sharing",namespace="aristotle_sharing")),
    url(r'^', include('aristotle_mdr.urls')),
    url(r'^ddi/', include('aristotle_ddi_utils.urls',app_name="aristotle_ddi_utils",namespace="aristotle_ddi_utils")),
    url(r'^dse/', include('aristotle_dse.urls',app_name="aristotle_dse",namespace="aristotle_dse")),
    url(r'^comet/', include('comet.urls',app_name="comet",namespace="comet")),
    url(r'^glossary/', include('aristotle_glossary.urls',app_name="aristotle_glossary",namespace="glossary")),
    url(r'^api/', include('aristotle_mdr_api.urls',app_name="aristotle_mdr_api",namespace="aristotle_mdr_api")),


    url(r'^about/?$', TemplateView.as_view(template_name='site/about.html'), name="aboutThisSite"),
    url(r'^copyright/?$', TemplateView.as_view(template_name='site/copyright.html'), name="copyright"),
    url(r'^disclaimer/?$', TemplateView.as_view(template_name='site/disclaimer.html'), name="disclaimer"),
    url(r'^contact/?$', TemplateView.as_view(template_name='site/contact.html'), name="contact"),

    )
