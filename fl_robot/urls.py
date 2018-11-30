# -*- coding: utf-8 -*-
from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^real_time_data/', include('fl_robot.real_time_data.urls')),
    url(r'^cmd/', include('fl_robot.cmd.urls')),
]