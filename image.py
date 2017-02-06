
#!/usr/bin/env python

from sys import argv

print "Generating Image\n"
file = open('image.ppm', 'w+')
file.truncate()
file.write("P3 250 250 255\n")
for i in range(0, 250):
    for j in range (0, 250):
        file.write("255 " + str(i%256) + " " + str(j%256) + " ")
    file.write("\n")

print "done!"
