from rest_framework import serializers

class UdSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Csv
        fields = ('c1', 'c2')