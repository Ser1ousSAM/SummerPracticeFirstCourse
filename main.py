#User Gleb: writting into file
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
