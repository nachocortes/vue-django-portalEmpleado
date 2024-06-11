from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework import viewsets, permissions, renderers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.Calendario.models import Calendario, CalendarioItem
from core.Calendario.serializers import CalendarioSerializer, CalendarioItemSerializer, UserSerializer
from core.RRHH.models import Empleado
from core.RRHH.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.RRHH.serializers import EmpleadoSerializer

# La clase DepartamentoViewSet extiende ModelViewSet para proporcionar operaciones CRUD para el modelo Departamento.
class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = CalendarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Añade rutas personalizadas a las acciones de tu viewset.
    # Permite definir métodos adicionales que pueden ser invocados desde la API
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        calendario = self.get_object()
        return Response(calendario.highlighted)

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        calendario = self.get_object()
        items = CalendarioItem.objects.filter(calendario=calendario)
        serializer = CalendarioItemSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)

# La clase EmpleadoViewSet extiende ModelViewSet para proporcionar operaciones CRUD para el modelo Empleado.
class CalendarioItemViewSet(viewsets.ModelViewSet):
    queryset = CalendarioItem.objects.all()
    serializer_class = CalendarioItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Añade rutas personalizadas a las acciones de tu viewset.
    # Permite definir métodos adicionales que pueden ser invocados desde la API
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        calendario_item = self.get_object()
        return Response(calendario_item.highlighted)

class UserCalendarioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CalendarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'empleado'):
            return Calendario.objects.filter(empleado=user.empleado)
        else:
            return Calendario.objects.none()

# Vista proporciona una interfaz de solo lectura para el modelo User,
# permitiendo listar y recuperar detalles de los usuarios
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Vista permite a cualquier usuario obtener un par de tokens JWT, vista necesaria para validar por token
class CustomTokenObtainPairView(TokenObtainPairView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

# Vista permite a cualquier usuario refrescar su token JWT, vista necesaria para validar por token
class CustomTokenRefreshView(TokenRefreshView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

# Vista permite a cualquier usuario registrarse creando
# un nuevo usuario, verificando que los campos requeridos
# están presentes y que el nombre de usuario no existe ya, vista necesaria para validar por token
class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'User created successfully'}, status=201)

# Vista para validar un token JWT recibido en la URL, vista necesaria para validar por token
class TokenAuthenticationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token, format=None):
        try:
            # Validar el token
            UntypedToken(token)

            # Obtener el usuario del token
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validated_token)

            # Autenticar al usuario
            return Response({'message': 'Token is valid', 'user': user.username})
        except (InvalidToken, TokenError):
            return Response({'error': 'Invalid token'}, status=400)
