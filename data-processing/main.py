import pickle

# Open the file in read-binary mode
with open('poems.pkl', 'rb') as file:
    data = pickle.load(file)

# Print the data line by line
for line in data:
    print(line)