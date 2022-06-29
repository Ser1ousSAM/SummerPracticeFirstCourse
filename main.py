#User Gleb: writting into file
def write_in_txt_file():
    with open('test.txt', 'w') as writer:
        writer.write('I love my Git')
        return True
