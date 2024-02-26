from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer