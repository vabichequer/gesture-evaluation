import csv
from os import walk
import matplotlib.pyplot as plt

FOLDER_RECORDINGS = "C:/Users/vabicheq/Documents/Repos/gesture-evaluation/recordings"

f = []
for (dirpath, dirnames, filenames) in walk(FOLDER_RECORDINGS):
    f.extend(filenames)

x, y, z = [], [], []

for filename in f:
    with open(FOLDER_RECORDINGS + '/' + filename, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader, None)
        for row in csvreader:
            x.append(float(row[6]))
            y.append(float(row[7]))
            z.append(float(row[8]))

    ax = plt.axes(projection='3d')
    ax.set_title(filename)
    ax.plot3D(x, y, z)
    ax.scatter3D(x, y, z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()