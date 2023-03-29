import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UdSerializer, RowSerializer
from .models import Csv

class UploadAPIView(APIView):
    def post(self, request):
        serializer = UdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['csv_file']

        reader = csv.reader(csv_file)
        for row in reader:
            csv_row = Csv()
            csv_row.c1 = row[0]
            csv_row.c2 = row[1]
            csv_row.save()

        return Response({'status': 'success'})

class Top60Rows(APIView):
    def get(self, request):
        c_name = request.query_params.get('c_name')
        s_order = request.query_params.get('s_order', 'asc')

        if c_name not in [f.name for f in Csv._meta.fields]:
            return Response({'error': f'Invalid column name: {c_name}'})

        if s_order not in ['asc', 'desc']:
            return Response({'error': f'Invalid sort order: {s_order}'})

        queryset = Csv.objects.order_by(f'{s_order}{c_name}')[:60]
        serializer = RowSerializer(queryset, many=True)
        return Response(serializer.data)
