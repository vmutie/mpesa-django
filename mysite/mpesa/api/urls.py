

from django.urls import path
from mpesa.api.views import LNMCallbackurlAPIView
urlpatterns = [
    path('lnm/', LNMCallbackurlAPIView.as_view(), name='lnm-callbackurl'),
    
    
]
