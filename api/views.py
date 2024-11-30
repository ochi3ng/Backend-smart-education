from rest_framework.decorators import action
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['enrolled_courses']
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def recommendations(self, request, pk=None):
        student = self.get_object()
        interests = student.interests.split(',')
        recommended_courses = Course.objects.filter(
            title__icontains=interests[0]  # Simplistic matching for demo
        )
        serializer = CourseSerializer(recommended_courses, many=True)
        return Response(serializer.data)
