user_input = input("Enter some text to write to output.txt: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')

append_input = input("Enter additional text to append to output.txt: ")
with open('output.txt', 'a') as file:
    file.write(append_input + '\n')

print(f"\nFinal content of '{"output.txt"}':")
with open("output.txt", 'r') as file:
    print(file.read())
