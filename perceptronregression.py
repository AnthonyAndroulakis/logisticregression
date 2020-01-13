print('Running...')
#get data
csv_file = 'spamham.csv'

x=[]
with open(csv_file, 'r') as f:
    for row in f:
        x.append(row.split(',')[0])
x = [float(i) for i in x]

y=[]
with open(csv_file, 'r') as f:
    for row in f:
        y.append(row.split(',')[1])
y = [float(i) for i in y]

##########################################################################################

xcoeff = 1 #a
ycoeff = 1 #b
constant = -1 #c #ax+by+c=0
learningrate = 0.05
epochs = 1000000
#algorithm to split the data: #buy + #mistakes = 4
# #buy = x, #mistakes = y
for i in range(epochs):
    #index = random.randrange(0,len(x)) #pick random index
    for index in range(len(x)):
        xpt = x[index]
        ypt = y[index]
        linevalue = xcoeff*xpt + ycoeff*ypt + constant
        if xpt+ypt > 4 and linevalue < 0: #point is spam but incorrectly classified
            xcoeff = xcoeff + learningrate*abs(xpt)
            ycoeff = ycoeff + learningrate*abs(ypt)
            constant = constant + learningrate
        elif xpt+ypt < 4 and linevalue > 0: #point is ham but incorrectly classified
            xcoeff = xcoeff - learningrate*abs(xpt)
            ycoeff = ycoeff - learningrate*abs(ypt)
            constant = constant - learningrate
        #else do nothing

##########################################################################################
#graph points and line of best fit
import matplotlib.pyplot as plt
import numpy as np
print('y = '+str(-(xcoeff/ycoeff))+'*x-'+str(constant/ycoeff))
xline = np.linspace(len(x),int(min(x)),int(max(x)))
yline = -(xcoeff/ycoeff)*xline-(constant/ycoeff)
plt.scatter(x, y) #plot the original points
plt.plot(xline,yline,'-r', label='y = '+str(-(xcoeff/ycoeff))+'*x-'+str(constant/ycoeff))
plt.show()