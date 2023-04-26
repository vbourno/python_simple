# strange message

strange_message = "C6786od7576ing F75acto86ry"

decrypted_message = ""

for char in strange_message:
    if not char.isnumeric():
        decrypted_message += char

print("Message:", decrypted_message)