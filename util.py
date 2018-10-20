from sklearn.feature_extraction.text import TfidfVectorizer


def convertToDocument(inputFileName, featureFileName):
    '''
    Converts the matrix format into a document format
    :param file:
    :return:
    '''

    inputFile = open(inputFileName, 'r')
    featureFile = open(featureFileName, 'r')
    outputFile = open("output.txt", 'w')

    features = featureFile.readlines()
    input = inputFile.readlines()


    for line in input:
        items = line.split()
        outline = ""
        for i in range(0, len(items),2):
            index = int(items[i])
            frequency = int(items[i+1])

            word = features[index-1].strip()
            outline += (word + " ") * frequency


        outline = outline.rstrip()
        outline += "\n"
        outputFile.writelines(outline)




if __name__ == "__main__":
    #convertToDocument("../1538577415_6724253_new_input.dat", "../1538577415_670582_features.dat")

    file = open("output.txt", 'r')
    vectorizer = TfidfVectorizer(stop_words='english', input=file)
