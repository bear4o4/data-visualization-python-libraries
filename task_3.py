import numpy as np


#task 3 a


# Step 1: Create a 2x2 key matrix
key_matrix = np.array([[3, 3], [2, 5]])

# Step 2: Define the message to be encrypted
message = "Hi"

# Step 3: Convert the message into a numerical format (ASCII values)
message_matrix = np.array([[ord(char) for char in message]])

# Step 4: Encrypt the message using matrix multiplication
encrypted_matrix = np.dot(message_matrix, key_matrix)

# Step 5: Decrypt the message using the inverse of the key matrix
inverse_key_matrix = np.linalg.inv(key_matrix)
decrypted_matrix = np.dot(encrypted_matrix, inverse_key_matrix).round().astype(int)

# Convert the decrypted numerical values back to characters
recovered_message = ''.join([chr(num) for num in decrypted_matrix[0]])

print(f"Original Message: {message}")
print(f"Encrypted Matrix:\n{encrypted_matrix}")
print(f"Decrypted Matrix:\n{decrypted_matrix}")
print(f"Recovered Message: {recovered_message}")


print("#####################")

#task 3 b
def text_to_matrix(text):
    # Ensure the text length is even by adding a space if necessary
    if len(text) % 2 != 0:
        text += ' '

    # Convert the text into ASCII values
    ascii_values = [ord(char) for char in text]

    # Reshape the ASCII values into a 2-column NumPy array
    matrix = np.array(ascii_values).reshape(-1, 2)

    return matrix


# Example usage
message = "Hello"
matrix = text_to_matrix(message)
print(matrix)

print("#####################")

#task 3 c
# Step 1: Create a 2x2 key matrix
key_matrix = np.array([[3, 3], [2, 5]])

# Step 2: Define the message to be encrypted
message = "Hello"

# Step 3: Convert the message into a numerical format (ASCII values)
def text_to_matrix(text):
    # Ensure the text length is even by adding a space if necessary
    if len(text) % 2 != 0:
        text += ' '

    # Convert the text into ASCII values
    ascii_values = [ord(char) for char in text]

    # Reshape the ASCII values into a 2-column NumPy array
    matrix = np.array(ascii_values).reshape(-1, 2)

    return matrix

message_matrix = text_to_matrix(message)

# Step 4: Encrypt the message using matrix multiplication
encrypted_matrix = np.dot(message_matrix, key_matrix)

print(f"Message Matrix:\n{message_matrix}")
print(f"Encrypted Matrix:\n{encrypted_matrix}")


print("#####################")

#task 3 d
# Step 1: Create a 2x2 key matrix
key_matrix = np.array([[3, 3], [2, 5]])

# Step 2: Define the message to be encrypted
message = "Hello"

# Step 3: Convert the message into a numerical format (ASCII values)
def text_to_matrix(text):
    # Ensure the text length is even by adding a space if necessary
    if len(text) % 2 != 0:
        text += ' '

    # Convert the text into ASCII values
    ascii_values = [ord(char) for char in text]

    # Reshape the ASCII values into a 2-column NumPy array
    matrix = np.array(ascii_values).reshape(-1, 2)

    return matrix

message_matrix = text_to_matrix(message)

# Step 4: Encrypt the message using matrix multiplication
encrypted_matrix = np.dot(message_matrix, key_matrix)

# Step 5: Compute the inverse of the key matrix
inverse_key_matrix = np.linalg.inv(key_matrix)

# Step 6: Decrypt the message using the inverse of the key matrix
decrypted_matrix = np.dot(encrypted_matrix, inverse_key_matrix).round().astype(int)

# Convert the decrypted numerical values back to characters
recovered_message = ''.join([chr(num) for num in decrypted_matrix.flatten()])

print(f"Original Message: {message}")
print(f"Encrypted Matrix:\n{encrypted_matrix}")
print(f"Decrypted Matrix:\n{decrypted_matrix}")
print(f"Recovered Message: {recovered_message}")


print("#####################")

#task 3 e

# Step 1: Create a 2x2 key matrix
key_matrix = np.array([[3, 3], [2, 5]])

# Step 2: Define the message to be encrypted
message = "Hello"

# Step 3: Convert the message into a numerical format (ASCII values)
def text_to_matrix(text):
    # Ensure the text length is even by adding a space if necessary
    if len(text) % 2 != 0:
        text += ' '

    # Convert the text into ASCII values
    ascii_values = [ord(char) for char in text]

    # Reshape the ASCII values into a 2-column NumPy array
    matrix = np.array(ascii_values).reshape(-1, 2)

    return matrix

message_matrix = text_to_matrix(message)

# Step 4: Encrypt the message using matrix multiplication
encrypted_matrix = np.dot(message_matrix, key_matrix)

# Step 5: Compute the inverse of the key matrix
inverse_key_matrix = np.linalg.inv(key_matrix)

# Step 6: Decrypt the message using the inverse of the key matrix
decrypted_matrix = np.dot(encrypted_matrix, inverse_key_matrix).round().astype(int)

# Step 7: Convert the decrypted numerical values back to characters
recovered_message = ''.join([chr(num) for num in decrypted_matrix.flatten()])

print(f"Original Message: {message}")
print(f"Encrypted Matrix:\n{encrypted_matrix}")
print(f"Decrypted Matrix:\n{decrypted_matrix}")
print(f"Recovered Message: {recovered_message}")