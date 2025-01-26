## Simple one neuron representation
# inputs = [1.2,2.9,3.4]
# weights = [2.1,3.4,4.8]
# bias = 3

# output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

# print(output)




## Here I m testing with 3 neurons and 4 inputs
# inputs = [1.2,2.1,3.1,4.1]

# weights1 = [1,2,3,4]
# weights2 = [2.1,-4.2,3.5,-0.1]
# weights3 = [0.3,-2.2,3.1,3.6]

# bias1 = 2
# bias2 = 3
# bias3 = 4

# output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
#           inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
#           inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3,]

# print(output)


## Using dot product for calculating the output of Neuron

import numpy as np 
inputs = [1.1,2.4,2.4,5.5]

weights = [[-0.4,8.4,0.3,-0.6],
           [-2.3,-9.3,-4.5,1.2],
           [3.4,-1.2,-0.4,1.3]]

biases = [1,2,3]

output = np.dot(weights , inputs) + biases

print(output)