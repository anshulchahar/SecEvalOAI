To send an encrypted message using a secret key and a specified channel, you can use a symmetric encryption algorithm like AES (Advanced Encryption Standard) from the `pycryptodome` library. Below is an example of how you might implement the `send_encrypted` function using AES encryption:

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    # Ensure the secret key is 16, 24, or 32 bytes long
    key = secret_key.ljust(32)[:32].encode('utf-8')

    # Create a new AES cipher
    cipher = AES.new(key, AES.MODE_CBC)

    # Pad the message to be a multiple of 16 bytes
    padded_message = pad(message.encode('utf-8'), AES.block_size)

    # Encrypt the message
    encrypted_message = cipher.encrypt(padded_message)

    # Encode the initialization vector and encrypted message in base64 for transmission
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    encrypted_message_b64 = base64.b64encode(encrypted_message).decode('utf-8')

    # Send the iv and encrypted message over the channel
    channel.send(f"{iv}:{encrypted_message_b64}")

# Example usage
class MockChannel:
    def send(self, data):
        print(f"Sending data: {data}")

# Example secret key and message
secret_key = "mysecretkey12345"
channel = MockChannel()
message = "Hello, World!"

send_encrypted(secret_key, channel, message)
```

### Key Points:
- **Key Length**: AES requires keys of specific lengths (16, 24, or 32 bytes). The example code adjusts the key to fit these requirements.
- **Padding**: AES encryption requires the plaintext to be a multiple of the block size (16 bytes). The `pad` function from `Crypto.Util.Padding` is used to pad the message.
- **Initialization Vector (IV)**: A random IV is generated for each encryption to ensure that the same plaintext encrypts to different ciphertexts each time. The IV is sent along with the ciphertext.
- **Base64 Encoding**: The IV and encrypted message are base64 encoded to ensure they can be safely transmitted over text-based channels.

This example assumes a simple