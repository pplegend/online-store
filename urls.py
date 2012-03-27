from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('preview.views',
    #(r'^catalog/$','views.home'),
    (r'^catalog/$','home'),
    (r'^catalog/about/','about'),
    (r'^catalog/privacy/','privacy'),
    (r'^catalog/projects/','projects'),
    (r'^catalog/contacts/','contacts'),
    (r'^accounts/', include('accounts.urls')),
    (r'^accounts/',include('django.contrib.auth.urls')),
    # Example:
    # (r'^iStore/', include('iStore.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
urlpatterns+=patterns('',
     (r'^search/',include('search.urls')),
     (r'^comment/product/add','comments.views.addComments'),
     #(r'^admin/(.*)',admin.site.root),
     (r'^admin/', include(admin.site.urls)),
     (r'^cart/',include('cart.urls')),
     (r'^',include('catalog.urls')),
     (r'rating/$','rate.views.addRating'),
     (r'^checkout/$','checkout.views.check_out'),
     (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/yongzhen/iStore/static'}),
)
handler404 = 'iStore.views.file_not_found_404'
