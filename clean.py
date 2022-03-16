import os


def CleanTxt():
    # Using readlines()
    count=0
    filename = 'occ.txt';
    with open(filename) as file:
        lines = file.readlines()
    
    with open("occ_clean.txt", "w") as fp:    
        for line in lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))
            fp.write(line.strip() + "\n")

if __name__ == "__main__":
    CleanTxt();