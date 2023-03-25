from django.db import transaction
from rest_framework import serializers

from apps.order.models import Order, OrderItems, ORDER_STATUS, CURRENCY


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]


class OrderItemsSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItems
        # fields = ('product', 'description')
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    order_items = OrderItemsSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    status = ChoiceField(choices=ORDER_STATUS, read_only=True)
    currency = ChoiceField(choices=CURRENCY, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_items')
        with transaction.atomic():
            order = Order.objects.create(**validated_data)
            order_item_serializer = self.fields['order_items']
            total = 0
            for item in order_item_data:
                item['order'] = order
                item['price'] = item["product"].price
                total += (item["product"].price * item.get("quantity"))
            order.total = total
            order.save()
            order_item_serializer.create(order_item_data)
        return order


class OrderStatusUpdateSerializer(serializers.ModelSerializer):

    status = ChoiceField(choices=ORDER_STATUS)

    class Meta:
        model = Order
        fields = ('status',)