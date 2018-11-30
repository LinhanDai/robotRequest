# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import views


urlpatterns = [
    url(r'^navigate$', views.setNavigateGoal),
]