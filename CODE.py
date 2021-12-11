# Import uuid library for generate Random ID:
# Make uuid with number format <= uuid.uuid1()
import uuid

# Import pickle:
import pickle
# 1.1 Load data with pickle:
def storeData(inputData, inputFileName):
    # 1. Load old data:
    dbfile1 = open(inputFileName, 'rb')
    dataLoad = pickle.load(dbfile1)
    dbfile1.close()
    # Append new data into old data:
    dataLoad.append(inputData)

    dbfile2 = open(inputFileName, 'ab')

    # source, destination
    pickle.dump(dataLoad, dbfile2)
    dbfile2.close()
    return inputData

def loadData(inputFileName):
    # for reading also binary mode is important
    dbfile = open(inputFileName, 'rb')
    dataLoad = pickle.load(dbfile)
    print('dataLoad:\n', dataLoad)
    dbfile.close()
    return dataLoad

# storeData({
#     "id_post": uuid.uuid1().hex,
#     "title_post": "Bài viết 1"
# },'./databases/posts.json')

loadData('./databases/posts.json')

# def storeData1(inputData, inputFileName):
#     # 1. Load old data:
#     dbfile1 = open(inputFileName, 'rb')
#     dataLoad = pickle.load(dbfile1)
#     dbfile1.close()
#     # Append new data into old data:
#     dataLoad.append(inputData)
#
#     dbfile2 = open(inputFileName, 'ab')
#
#     # source, destination
#     pickle.dump(dataLoad, dbfile2)
#     dbfile2.close()
#     return dataLoad
