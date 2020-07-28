def openFile(filename):
    f = open(filename)
    sample = f.readlines()
    output = []
    for line in sample:
        line_words = []
        for word in line.split():
            line_words.append(word)
        output.append(line_words)
    print(output)
    return output
 
# write file function #
# instructions: create a function that takes the name of a text file and a list of lists as a parameter, and creates a textfile with each inner list as a sentence in the text file. print it.


def writeFile(filename, content):
    new_file = open(filename, "w")
    for sentence in content:
        for word in sentence:
            new_file.write(word + " ")
        new_file.write("\n")
    new_file.close()


output = openFile("sample.txt")
output[0][1] = "new"
writeFile("new_file.txt", output)