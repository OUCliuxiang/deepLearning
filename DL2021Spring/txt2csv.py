import os
import csv 

def txt2csv(path):
    """
    @ Params:
    path: str, "train" or "test"
    """
    if not ( path == "train" or path == "test"):
        sys.stderr.write("invalid params input.")
        return -1
    posPath = os.path.join(os.path.abspath(""), "aclImdb", path, "pos")
    negPath = os.path.join(os.path.abspath(""), "aclImdb", path, "neg")
    csvPath = os.path.join(os.path.abspath(""), "aclImdb", path +".csv")
    posFiles = os.listdir(posPath)
    negFiles = os.listdir(negPath)
    posFiles.sort()
    negFiles.sort()
    # files = posFiles + negFiles
    # files.sort()
    with open(csvPath, "a+", newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        for posFile in posFiles:
            with open(os.path.join(posPath, posFile), 'r', encoding='utf-8') as pf:
                content = pf.readline()
                line = [content, "positive"]
                writer.writerow(line)
  
    with open(csvPath, "a+", newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        for negFile in negFiles:
            with open(os.path.join(negPath, negFile), 'r', encoding='utf-8') as nf:
                content = nf.readline()
                line = [content, "negative"]
                writer.writerow(line)

txt2csv("train")
txt2csv("test")