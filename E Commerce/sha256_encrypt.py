from passlib.hash import sha256_crypt

# Your plaintext password
plaintext_password = "welcome123"

# Generate the SHA-256 Crypt hash
hashed_password = sha256_crypt.using(rounds=535000).hash(plaintext_password)

# Print the hashed password
print("Hashed Password:", hashed_password)
