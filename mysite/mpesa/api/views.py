
from mpesa.api.serializers import LNMOnlineSerializer
from rest_framework.generics import CreateAPIView
from mpesa.models import LNMOnline


class LNMCallbackurlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    # permission_classes = [IsAdminUser]

    # to capute the data
    def create(self, request):
        print(request.data(),'this is request.data')

 