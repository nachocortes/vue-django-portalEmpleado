from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from core.RRHH.models import Empleado, Departamento
from core.RRHH.permissions import IsOwnerOrReadOnly
from core.RRHH.serializers import UserSerializer, EmpleadoSerializer, DepartamentoSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


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


# La clase DepartamentoViewSet extiende ModelViewSet para proporcionar operaciones CRUD para el modelo Departamento.
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Añade rutas personalizadas a las acciones de tu viewset.
    # Permite definir métodos adicionales que pueden ser invocados desde la API
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        departamento = self.get_object()
        return Response(departamento.highlighted)


# La clase EmpleadoViewSet extiende ModelViewSet para proporcionar operaciones CRUD para el modelo Empleado.
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Añade rutas personalizadas a las acciones de tu viewset.
    # Permite definir métodos adicionales que pueden ser invocados desde la API
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        empleado = self.get_object()
        return Response(empleado.highlighted)

    # Asigna propietario al empleado, copia estado de staff del usuario actual, y guarda los cambios.
    def perform_create(self, serializer):
        empleado = serializer.save(owner=self.request.user)
        empleado.is_staff = self.request.user.is_staff
        empleado.save()

    # Actualiza empleado, copia estado de staff del propietario al empleado, y guarda los cambios.
    def perform_update(self, serializer):
        empleado = serializer.save()
        empleado.is_staff = empleado.owner.is_staff
        empleado.save()


# Vista proporciona una interfaz de solo lectura para el modelo User,
# permitiendo listar y recuperar detalles de los usuarios
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer






# # Vista que peermitir todas las operaciones CRUD para el modelo User,list: Recupera una lista de todos los usuarios.
# retrieve: Recupera los detalles de un usuario específico.
# create: Crea un nuevo usuario.
# update: Actualiza todos los campos de un usuario existente.
# partial_update: Actualiza algunos campos de un usuario existente.
# destroy: Elimina un usuario existente.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Vista que permiten todas las operaciones CRUD.
# class UserViewSet(mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.ListModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Vista base que no incluye ninguna acción predeterminada. Debes definir las acciones manualmente.
# class UserViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['post'])
#     def create(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#     @action(detail=True, methods=['put'])
#     def update(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     @action(detail=True, methods=['delete'])
#     def destroy(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         user.delete()
#         return Response(status=204)
