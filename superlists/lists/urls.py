from django.conf.urls import include, url
from django.contrib import admin

from views import home_page, view_list, new_list, add_item

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)/$', view_list, name = 'view_list'),
    url(r'^new/$', new_list, name = 'new_list'),
]