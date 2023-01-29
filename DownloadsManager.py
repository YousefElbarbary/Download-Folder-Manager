import os
import time
from datetime import datetime

Downloads_dir = "D:\Downloads"
Exec_dir = Downloads_dir + "\Executables"
Compressed_dir = Downloads_dir + "\Compressed"
text_dir = Downloads_dir + "\Text"
others_dir = Downloads_dir + "\Others"
directories = ['exec', 'compressed','text','others']
def chang_dir(dir):
    match dir:
        case "down":
            os.chdir(Downloads_dir)
        case "exec":
            os.chdir(Exec_dir)
        case "compressed":
            os.chdir(Compressed_dir)
        case "text":
            os.chdir(text_dir)
        case "others":
            os.chdir(others_dir)

def makedir(dir):
    os.mkdir(dir)

def check_dir(path):
    return (os.path.exists(path))

def get_files():
    return (os.listdir())

def move_files(file, type):
    if type == "exec":
        if not check_dir(Exec_dir):
            makedir(Exec_dir)
        else:
            os.rename(Downloads_dir + "\{}".format(file) , Exec_dir + "\{}".format(file))
    if type == "compressed":
        if not check_dir(Compressed_dir):
            makedir(Compressed_dir)
        else:
            os.rename(Downloads_dir + "\{}".format(file) , Compressed_dir + "\{}".format(file))
    if type == "text":
        if not check_dir(text_dir):
            makedir(text_dir)
        else:
            os.rename(Downloads_dir + "\{}".format(file) , text_dir + "\{}".format(file))
    if type == "others":
        if not check_dir(others_dir):
            makedir(others_dir)
        else:
            os.rename(Downloads_dir + "\{}".format(file) , others_dir + "\{}".format(file))


def check_files(files):
    for file in files:
        if file.endswith(".exe"):
            move_files(file,"exec")
        elif file.endswith(".rar") or file.endswith(".iso") or file.endswith(".zip"):
            move_files(file,"compressed")
        elif file.endswith(".pdf") or file.endswith(".txt"):
            move_files(file,"text")
        elif os.path.isfile(Downloads_dir + "/{}".format(file)):
            move_files(file,"others")
        else:
            continue

def check_date(files,dir):
    for file in files:
        curr_year = int(datetime.now().year)
        file_year = int(time.strptime(time.ctime(os.path.getctime(dir + "\{}".format(file)))).tm_year)
        curr_month = int(datetime.now().month)
        file_month = int(time.strptime(time.ctime(os.path.getctime(dir + "\{}".format(file)))).tm_mon)
        if (curr_year > file_year):
            if (curr_month - (file_month-12)) >= 3:
                delete_file(dir + "\{}".format(file))
            else:
                continue
        else:
            if (curr_month - file_month) >= 3:
                delete_file(dir + "\{}".format(file))
            else:
                continue
        

def delete_file(dir):
    os.remove(dir)


def main():
    if __name__ == "__main__":
        chang_dir("down")
        files = get_files()
        check_files(files)
    for dir in directories:
        chang_dir(dir)
        check_date(get_files(),os.getcwd())

main()