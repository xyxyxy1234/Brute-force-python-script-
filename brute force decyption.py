import os

def bruteforce_decrypt(encrypted_file, password_list):
  with open(password_list, 'r') as f:
    for password in f:
      password = password.strip()
      try:
       
        decrypted_data = decrypt_data(encrypted_file, password)
        with open('decrypted_file.txt', 'wb') as out_file:
          out_file.write(decrypted_data)
        print("Decryption successful with password:", password)
        return
      except Exception as e:
        print(f"Password '{password}' failed: {e}")

# Placeholder for the actual decryption function
def decrypt_data(encrypted_file, password):
  # This would contain the logic to decrypt the file using the given password
  # Replace with the appropriate decryption code for your encryption method
  pass


encrypted_file = "encrypted_data.bin"
password_list = "password_list.txt"
bruteforce_decrypt(encrypted_file, password_list)
