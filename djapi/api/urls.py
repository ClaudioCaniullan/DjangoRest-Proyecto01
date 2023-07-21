from django.urls import path

# swagger no operativo 
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
# inicializar instancia de view swagger
squema_view = get_swagger_view(title="Restful Api Rest Curso Udemy julio 2023")

from api.apiviews import ProductoList, ProductoDetalle, CategoriaList, SubCategoriaList, CategoriaDetalle, SubCategoriaAdd,ProductoViewSet
from api.apiviews import UserCreate, LoginView

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


<<<<<<< HEAD
from  rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

# inicializar vista de swagger
schema_view = get_swagger_view(title='Restful API DRF UDEMY')
=======


>>>>>>> main

router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(),name='producto_list' ),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(),name='producto_detalle' ),
    path('v1/categorias/', CategoriaList.as_view(),name='categoria_save' ),
    #path('v1/subcategorias/', SubCategoriaList.as_view(),name='subcategoria_list' )
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(),name='categoria_detalle' ),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(),name='sc_list' ),

    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(),name='subcategoria_apiview' ),

    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear'),

    path("v4/login/", LoginView.as_view(), name="login"),

    #Importar vistas de DRF para authtoken
    path("v4/login-drf/", views.obtain_auth_token, name="login_drf"),
<<<<<<< HEAD
    
    path('swagger-docs/', schema_view), 
    path('coreapi-docs/', include_docs_urls(title = 'Documentacion COREAPI'))
=======

    path('swagger-docs/', squema_view),
    path('coreapi-docs/', include_docs_urls('Documentacion RestAPI Curso Udemy Julio 2023 COREAPI')),
>>>>>>> main
]


#luego de iniciar urlpatterns
urlpatterns += router.urls