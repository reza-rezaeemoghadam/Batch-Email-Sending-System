# Importing rest modules
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Importing swagger modules
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

# Importing utils
from core.utils.send_email import send_batch_email, send_single_email

# Importing custom serializer
from .serializers import EmailSerializer

# Create your views here.
class EmailAPIView(APIView):
    """
    View to trigger batch email sending asynchronously.
    This view will receive a list of emails, a subject, and a body, and then send the emails asynchronously using RabbitMQ and Celery.
    """
    permissions_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        request=EmailSerializer,  # Request body schema
        responses={
            202: OpenApiResponse(description="Email task is being processed asynchronously."),
            400: OpenApiResponse(description="Invalid input data."),
        },
    )
    def post(self, request, *args, **kwargs):
        # Validate input data
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email_list = serializer.validated_data['email_list']
            subject = serializer.validated_data['subject']
            body = serializer.validated_data['body']

            # Call the Celery task asynchronously
            send_batch_email.apply_async(args=[email_list, subject, body])

            return Response(
                {"message": "Email task is being processed in the background."},
                status=status.HTTP_202_ACCEPTED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)