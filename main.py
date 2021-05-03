# Import the required module
import os


def word_searching(filename):

    word = 'python'

    with open(filename,'r') as f:
        fileText = f.read().lower()
        if word in fileText:
            return True
        else:
            return False





if __name__ == "__main__":

    number_of_files = 0 # Files in which word found

    current_working_dir = os.getcwd()
    dir_contents = os.listdir()

    print(f"Your current working directory is --> {current_working_dir}")
    print(f"You current working directory contains --> {dir_contents}")

    for file in dir_contents:
        if file.endswith('txt'):
            print(f'Searching for word in {file}')
            with open(file,'r') as f:
                found = word_searching(file)
                if found == True:
                    print(f'word found in {file}')
                    number_of_files += 1
                else:
                    print(f"Not found in {file}")
    print(f"Word found in  --> {number_of_files} files")
    print("Code Completed 🔥")