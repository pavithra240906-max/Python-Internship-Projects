import random
import string

length = int(input("Enter password length: "))

# Ensure at least one from each category
password = [
    random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]

# Fill remaining length
all_chars = string.ascii_letters + string.digits + string.punctuation

for i in range(length - 4):
    password.append(random.choice(all_chars))

# Shuffle to avoid fixed pattern
random.shuffle(password)

# Convert list to string
password = "".join(password)

print("Strong Password:", password)