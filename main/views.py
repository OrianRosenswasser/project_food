from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, FoodPost, FoodRequest
from .forms import MemberForm, FoodPostForm, FoodRequestForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer, FoodPostSerializer, FoodRequestSerializer

@api_view(['GET', 'POST'])
def post_food_page(request):
    if request.method == 'GET':
        return render(request, 'post_food.html')

    elif request.method == 'POST':
        posted_by = Member.objects.first()
        if not posted_by:
            return Response({'error': 'No members available'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['posted_by'] = posted_by.id

        serializer = FoodPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'home.html')

@api_view(['GET', 'POST'])
def request_food(request, post_id):
    food_post = get_object_or_404(FoodPost, id=post_id)

    if request.method == 'GET':
        return render(request, 'request_food.html', {'food_post': food_post})

    elif request.method == 'POST':
        request_data = request.data.copy()
        request_data['food_post'] = food_post.id
        request_data['requested_by'] = None

        serializer = FoodRequestSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Food request successfully submitted!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return render(request, 'member_list.html')

def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MemberForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')

@api_view(['GET', 'DELETE'])
def food_feed(request, pk=None):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        food_posts = FoodPost.objects.all().order_by('expiration_date')
        serializer = FoodPostSerializer(food_posts, many=True)
        return Response(serializer.data)
    
    if request.method == 'DELETE' and pk:
        try:
            food_post = FoodPost.objects.get(pk=pk)
            food_post.delete()
            return Response({'message': 'Food post deleted successfully!'}, status=204)
        except FoodPost.DoesNotExist:
            return Response({'error': 'Food post not found'}, status=404)

    return render(request, 'food_feed.html')







