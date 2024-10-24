from rest_framework import viewsets
from .models import *
from .serializers import *

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class NeighborhoodViewSet(viewsets.ModelViewSet):  # Mahalle viewset'i
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

class FarmerViewSet(viewsets.ModelViewSet):  # Farmer viewset'i
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Land
from .serializers import LandSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Land
from .serializers import LandSerializer
from rest_framework import generics

class LandViewSet(viewsets.ModelViewSet):
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]
    queryset = Land.objects.all()  # Burada queryset tanımlaması yapıyoruz

    def get_queryset(self):
        user_id = self.request.user.id
        return Land.objects.filter(farmer__user_id=user_id) | Land.objects.filter(partner__user_id=user_id)



class LandDetailViewSet(viewsets.ModelViewSet):
    queryset = LandDetail.objects.all()
    serializer_class = LandDetailSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoListByLandView(generics.ListAPIView):
    serializer_class = TodoListSerializer

    def get_queryset(self):
        land_id = self.kwargs['land_id']
        return TodoList.objects.filter(land_id=land_id)

class TodoDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = TodoListSerializer

    def get_queryset(self):
        land_id = self.kwargs['land_id']
        return TodoList.objects.filter(land_id=land_id)

    def get_object(self):
        todo_id = self.kwargs['todo_id']
        queryset = self.get_queryset()
        try:
            return queryset.get(id=todo_id)
        except TodoList.DoesNotExist:
            raise NotFound("Todo not found")  # Http404 yerine NotFound kullan

    def put(self, request, *args, **kwargs):
        todo = self.get_object()  # Todo nesnesini al
        serializer = self.get_serializer(todo, data=request.data, partial=False)  # partial=False ile tüm alanları kontrol et

        if serializer.is_valid():  # Serializer geçerliliğini kontrol et
            serializer.save()  # Güncelle
            return Response(serializer.data, status=status.HTTP_200_OK)  # Güncellenmiş veriyi döndür
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Hata mesajlarını döndür

    # GET isteği için varsayılan davranış zaten sağlanıyor


class WeatherAlertViewSet(viewsets.ModelViewSet):
    queryset = WeatherAlert.objects.all()
    serializer_class = WeatherAlertSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            token = request.data.get('refresh')
            token_obj = RefreshToken(token)
            token_obj.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
