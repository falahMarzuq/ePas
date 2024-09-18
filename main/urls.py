from django.urls import path
from main.views import show_main, create_products, create_accounts, show_xml, show_json, show_xml_by_id, show_json_by_id, clear_session

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-products', create_products, name="create_products"),
    path("create-accounts", create_accounts, name="create_accounts"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('clear-session/', clear_session, name='clear_session')
]