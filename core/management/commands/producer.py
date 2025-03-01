from django.core.management.base import BaseCommand

# Importing rabbitmq context manager
from core.messaging.rabbitmq import RabbitMQConnectionManager

# Implementing custom commands
class Command(BaseCommand):
    help = "This command produces a message in rabbitmq. "

    def add_arguments(self, parser):
        parser.add_argument('-m','--message', type=str, help="Message to send")
        parser.add_argument('-i','--iteration', type=int, help="Iteration number")

    def handle(self, *args, **options):
        message = options['message']
        iteration = options.get('iteration', None)

        with RabbitMQConnectionManager("rabbitmq") as rabbitmq:
            body = {"message": message}

            rabbitmq.exchange_declare(exchange='q.message', exchange_type='direct', durable=True)

            rabbitmq.queue_declare(queue='q.message')
            rabbitmq.bind_queue(routing_key="message_key")

            # Publish the message
            for i in range(iteration):
                rabbitmq.publish(body=body)
                print(f"Sent: {message}")