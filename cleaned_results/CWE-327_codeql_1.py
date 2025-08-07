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