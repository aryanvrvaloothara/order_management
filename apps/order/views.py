from django.db.models import Q
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.order.models import Order, ORDER_STATUS
from apps.order.serializers import OrderSerializer, OrderStatusUpdateSerializer


class OrderViewSet(viewsets.ModelViewSet):
    '''
    Viewset for operations related to order
    '''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        filter queryset based on status
        filter queryset based on currency
        filter queryset based on total price range(start_range and end_range)
        order queryset based on total price in ascending and descending order
        """
        queryset = Order.objects.all()
        status = self.request.query_params.get('status')
        currency = self.request.query_params.get('currency')
        start_range = self.request.query_params.get('start_range', None)
        end_range = self.request.query_params.get('end_range', None)
        ordering = self.request.query_params.get('ordering', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        if currency is not None:
            queryset = queryset.filter(currency=currency)
        if start_range and end_range:
            queryset = queryset.filter(Q(total__gte=start_range), Q(total__lte=end_range))
        if ordering is not None:
            if ordering == 'total_asc':
                queryset = queryset.order_by('total')
            elif ordering == 'total_desc':
                queryset = queryset.order_by('-total')
        return queryset

    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        '''
        Changes the staus of an existing order
        Params:
            status: status id corresponding to the new status value
        Return:
            1. 200 ok if the update succeeds
            2. Not found: if the order couldn't be found
            3. not a valid choice if the new status id doesn't exist
        '''
        order = self.get_object()
        serializer = OrderStatusUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

