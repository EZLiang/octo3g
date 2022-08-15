import path
fingerprintfile = path.path + "/build/fingerprints.txt"
base = path.path + "/octohashes/octohashes3g"

count = 0
ptr = 0
with open(fingerprintfile) as f:
  f2 = open(base + "_0.txt", "w")
  for line in f:
    f2.write(line)
    count +=1
    if count == 23238:
      count = 0
      f2.close()
      ptr += 1
      f2 = open(base + "_" + str(ptr) + ".txt", "w")
f2.close()