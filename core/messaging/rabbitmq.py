import json
import pika

class RabbitMQConnectionManager:
    def __init__(self, host: str = "localhost"):
        self.host = host
        self.connection = None
        self.channel = None
        self.exchange = None
        self.routing_key = None
        self.queue = None

    def __enter__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.channel and not self.channel.is_closed:
            self.channel.close()

        if self.connection and not self.connection.is_closed:
            self.connection.close()

        # Handle any exception that might have occurred within the context
        if exc_type:
            print(f"An error occurred: {exc_val}")

    def exchange_declare(self, exchange: str, exchange_type: str = "direct") -> None:
        self.exchange = exchange
        self.channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)

    def queue_declare(self, queue: str) -> None:
        """Declare a queue to be used for consuming messages"""
        self.queue = queue
        self.channel.queue_declare(queue=queue)

    def bind_queue(self, routing_key:str) -> None:
        """Bind the queue to the exchange with the routing key"""
        self.routing_key = routing_key
        if not self.queue:
            raise ValueError("Queue not declared. Declare a queue first.")
        if not self.exchange:
            raise ValueError("Exchange not declared. Declare an exchange first.")
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue, routing_key=self.routing_key)

    def publish(self, body: dict) -> None:
        self.channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=json.dumps(body))