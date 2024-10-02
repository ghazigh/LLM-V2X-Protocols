# src/main.py

from semantic_compression import SemanticCompressor
from context_aware_messaging import ContextAwareMessenger
from multi_language_support import MultiLanguageSupport

def main():
    # Initialize modules
    compressor = SemanticCompressor()
    messenger = ContextAwareMessenger()
    translator = MultiLanguageSupport()

    # Sample message and context
    message = "Heavy traffic reported ahead, consider alternative routes."
    context = {"location": "Interstate 80", "time": "08:30 AM"}

    # Process flow
    compressed = compressor.compress(message)
    context_message = messenger.create_message(compressed, context)
    translated_message = translator.translate(context_message, target_language='de')

    print("Final Message to Transmit:")
    print(translated_message)

if __name__ == "__main__":
    main()
