from django.urls import path
from .views import all_providers,specific_provider,all_prices,specific_price,ProvidersAPIView,SpecificProviderAPIView

urlpatterns = [
    path('all_providers/', all_providers),#http://localhost:8000/api/all_providers/
    path('specific_provider/<int:pk>',specific_provider),#http://localhost:8000/api/specific_provider/1
    path('all_prices',all_prices),#http://localhost:8000/api/all_prices
    path('specific_price/<int:pk>',specific_price),#http://localhost:8000/api/specific_price/1
    path('all_providers_apiview',ProvidersAPIView.as_view()),#http://localhost:8000/api/all_providers_apiview
    path('specific_provider_apiview/<int:pk>',SpecificProviderAPIView.as_view()),#http://localhost:8000/api/specific_provider_apiview/1
]
