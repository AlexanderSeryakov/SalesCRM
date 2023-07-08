from rest_framework.response import Response
from rest_framework.views import APIView
from apps.supply.api.serializers import SupplySerializer
from apps.common_utils import add_product_quantity


class SupplyApiView(APIView):
    def get(self, request):
        return Response({'SupplyApiView': 200})
    
    def post(self, request):
        user_id = request.user.pk
        data = request.data

        try:
            total_products_count = 0
            for p in data['products']:
                total_products_count += int(p['quantity'])

            prepare_data = {'user': user_id, 'products': data['products'], 'total_products':total_products_count,
                            'shipper': data['shipping'][0]['shipper'], 
                            'shipper_phone': data['shipping'][1]['shipper-phone'], 
                            'shipper_buisnes': data['shipping'][2]['shipper-buisnes'],
                            'shipper_address': data['shipping'][3]['shipper-address'],
                            'comments': data['shipping'][4]['shipper-comments']}
        except KeyError:
            return Response({'Incorrect data': 400})
        

        serializer = SupplySerializer(data=prepare_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        add_product_quantity(data['products'])

        return Response({'status': 200, 'new-supply': 'created'})
