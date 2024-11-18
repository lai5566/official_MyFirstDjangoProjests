from tempfile import template
from unittest import loader

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from polls.models import Question , Choice
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
def vote(request, question_id):
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                     "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
# 前端註冊資料驗證
@api_view(['POST'])
def register_user(request):
    permission_classes = [AllowAny]
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .serializers import LoginSerializer
# 登入視圖
@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.validated_data['user']
        if user.is_admin:
            print(f"Admin login: {user.email}")
        else:
            print(f"User login: {user.email}")
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)