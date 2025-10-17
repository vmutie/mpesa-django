
from mpesa.api.serializers import LNMOnlineSerializer
from rest_framework.generics import CreateAPIView
from mpesa.models import LNMOnline
from rest_framework.permissions import AllowAny


class LNMCallbackurlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_class = [AllowAny]

    # to capute the data
    def create(self, request):
        print(request.data(),'this is request.data')

 