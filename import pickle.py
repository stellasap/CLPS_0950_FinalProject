#pickles are really really cool
import pickle
import sklearn
# open a file, where you stored the pickled data
file = open('clf.sav', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()
