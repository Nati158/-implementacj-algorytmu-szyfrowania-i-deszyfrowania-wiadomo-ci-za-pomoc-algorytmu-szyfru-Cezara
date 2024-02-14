def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

if __name__ == "__main__":
    message = "Hello, World!"
    shift = 3
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)
    decrypted_message = caesar_decipher(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)
