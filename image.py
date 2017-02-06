
#!/usr/bin/env python

from sys import argv

print "Generating Image\n"
file = open('image.ppm', 'w+')
file.truncate()
file.write("P3 500 500 255\n")

for i in range(0, 500):
    for j in range (0, 500):
        file.write("" + str((i*i-j)%256) + " " + str((i+j)%256) + " " + str((j*j-i)%256) + " ")
    file.write("\n")

print "done!"
