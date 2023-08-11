
from django.urls import path
from .views import UserRegistrationView, GenerateTokenView,StoreDataView, RetrieveDataView, UpdateDataView, DeleteDataView


urlpatterns = [

    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/token/', GenerateTokenView.as_view(), name='generate-token'),
    path('api/data/', StoreDataView.as_view(), name='store-data'),
    path('retrieve-data/<int:id>', RetrieveDataView.as_view(), name='retrieve-data'),
    path('update-data/<int:id>', UpdateDataView.as_view(), name='update-data'),
    path('delete-data/<int:id>', DeleteDataView.as_view(), name='delete-single-data'),


]

