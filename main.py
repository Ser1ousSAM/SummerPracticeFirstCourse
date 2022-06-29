import os

# User Victor: Function to del a file
def delete_file():
    file_path = 'file.txt'
    try:
        os.remove(file_path)
        return True
    except:
        print("The system cannot find the file specified")
        return False
=======
# User Kovylin: Reading a file
def read_txt_file():
    file = 'file.txt'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
        return data
=======
# User Gleb: writting into file
def write_in_txt_file():
    with open('test.txt', 'w') as writer:
        writer.write('I love my Git')
        return True
if __name__ == "__main__":
    if write_int_txt_file(): # create and write in file "I love my Git"
        print("[OK] write")
    print(read_txt_file()) # read content

    if delete_file(): # delete file
        print("[OK] delete")
