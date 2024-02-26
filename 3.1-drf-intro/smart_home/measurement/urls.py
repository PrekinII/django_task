from django.urls import path

from measurement.views import MeasurementView, SensorView, SensorUpView

urlpatterns = [
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorUpView.as_view()),
    path('sensors/', SensorView.as_view()),
]
