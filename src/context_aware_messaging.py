# src/context_aware_messaging.py

class ContextAwareMessenger:
    def create_message(self, compressed_message, context):
        # Attach context to the compressed message
        context_str = ";".join([f"{k}={v}" for k, v in context.items()])
        context_message = {
            "message": compressed_message.tolist(),
            "context": context_str
        }
        return context_message

    def parse_message(self, context_message):
        # Extract compressed message and context
        compressed_message = context_message["message"]
        context_items = context_message["context"].split(";")
        context = {k: v for item in context_items for k, v in [item.split("=")]}
        return compressed_message, context