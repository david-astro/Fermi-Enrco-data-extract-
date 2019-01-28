import numpy as np

Results = open("/home/david/Desktop/lightcurve/resultFinal.txt", 'a')

with open("/home/david/Desktop/lightcurve/list.txt", "r") as f:
     lines = f.read().splitlines()



num_index = 0
while num_index < 3000:
      with open(lines[num_index], 'r') as kk:
           data = np.genfromtxt(kk, dtype=None)
           FirstCol = np.array(data[:,0])
           print FirstCol
           a = FirstCol.tolist().index('tmin')
           b = FirstCol.tolist().index('tmax')
           c = FirstCol.tolist().index('Flux')
           d = FirstCol.tolist().index('dFlux')
           e = FirstCol.tolist().index('Index')
           f = FirstCol.tolist().index('dIndex')
           g = FirstCol.tolist().index('TS')
           features = [data[a,1], data[b,1], data[c,1], data[d,1], data[e,1], data[f,1],data[g,1]]
           featuresFloat = []
           for i in features:
               featuresFloat.append(float(i))
           if 'Ulvalue' in FirstCol:
               featuresFloat[3] = 0 
           else:
               featuresFloat[3] = featuresFloat[3]
           Results.write(str(data[a,1]) + "\t" + str(data[b,1]) + "\t" + str(featuresFloat[2]) + "\t"+str(featuresFloat[3])+ "\t" + str(data[e,1]) +"\t"+ str(data[f,1])+"\t" + str(data[g,1]))
           Results.write("\n")
           num_index += 1
print("Finish")
















