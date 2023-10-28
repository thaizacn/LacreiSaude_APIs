from django.urls import path
from .views import PessoaProfissionalListCreateView, PessoaProfissionalDetailView, ConsultaListCreateView, ConsultaDetailView

urlpatterns = [
    path('profissionais/', PessoaProfissionalListCreateView.as_view(), name='profissional-list-create'),
    path('profissionais/<int:pk>/', PessoaProfissionalDetailView.as_view(), name='profissional-detail'),
    path('consultas/', ConsultaListCreateView.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', ConsultaDetailView.as_view(), name='consulta-detail'),
]