with open("notes.txt",'w')as f:
    f.write("Learning python I/O file")


with open("notes.txt",'a')as f1:
    f1.write("\nDay 24 session")


with open("notes.txt",'r')as f2:
    for line in f2:
        print(line)


with open("demo day15.bin",'wb')as f3:
    f3.write(b"Hello 123")


with open("notes.txt",'r')as f4:
    lines=f4.readlines()
    print("number of lines:",len(lines))


with open("source.txt",'r')as src,open("backup.txt",'w')as dest:
    for line in src:
        dest.write(line)

