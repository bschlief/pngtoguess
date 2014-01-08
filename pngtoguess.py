from sys import argv
import png
from pybrain.tools.xml.networkreader import NetworkReader

filename = argv[1]

png_file = png.Reader(filename).read()

arr = []
for row in png_file[2]:
    for i in row:
        arr.append((255-i)/255)

net = NetworkReader.readFrom('network.xml')

result = net.activate(arr)
guess = result.argmax()

print "Best guess is {0}".format(guess)

for idx,item in enumerate(result):
    print "Probability of {0} is {1:.3f}%".format(idx, item*100)


