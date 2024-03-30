def write_to_file():
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line of text.\n")
      file.write("Here's a line with a number: 42\n")
      file.write("And some more text to add.\n")
  except Exception as e:
    print(f"Error writing to file: {e}")

def read_from_file():
  
  try:
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError:
    print("File 'my_file.txt' not found.")
  except Exception as e:
    print(f"Error reading from file: {e}")

def append_to_file():
 
  try:
    with open("my_file.txt", "a") as file:
      file.write("Appending this line.\n")
      file.write("Adding another line of text.\n")
      file.write("This is the final appended line.\n")
  except Exception as e:
    print(f"Error appending to file: {e}")


write_to_file()
read_from_file()
append_to_file()
read_from_file()  
