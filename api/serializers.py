from rest_framework import serializers
from car_part_sale.models import *
from django.contrib.auth.models import User



###Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description']

###Category
class CategoryAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


###Part
class PartSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Part
        fields = ['id','slug','name','model','description','price','creted','category']
    
    def get_category(self,obj):
        return obj.Category.name
    

class PartAllSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Part
        fields = '__all__'
    
    def get_category_name(self,obj):
        return obj.Category.name

###Cart
class CartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    part = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = '__all__'
    
    def get_user(self,obj):
        return obj.user.username

    def get_part(self,obj):
            return obj.part.name
    

###Order
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_user(self,obj):
        return obj.user.username
    

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
    
    
    

### User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active']



class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],


        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()

        return user