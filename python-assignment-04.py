try:
    file1 = open('python_assignment_04.txt', 'r')
    read_file = file1.read()
    print(read_file)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'python_assignment_04.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")



