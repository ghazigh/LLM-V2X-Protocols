# API Reference

## SemanticCompressor

- **compress(text)**
  - Compresses input text into a semantic vector.
  - **Parameters**: `text` (str)
  - **Returns**: `compressed_vector` (np.array)

- **decompress(compressed_vector)**
  - Decompresses a semantic vector back into text.
  - **Parameters**: `compressed_vector` (np.array)
  - **Returns**: `text` (str)

## ContextAwareMessenger

- **create_message(compressed_message, context)**
  - Combines compressed message with context.
  - **Parameters**:
    - `compressed_message` (list)
    - `context` (dict)
  - **Returns**: `context_message` (dict)

- **parse_message(context_message)**
  - Separates compressed message from context.
  - **Parameters**: `context_message` (dict)
  - **Returns**:
    - `compressed_message` (list)
    - `context` (dict)

...