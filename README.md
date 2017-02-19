##### evaluate training work
```python
def training():
  split training sample to batch size *(1000,3072)
  for each epoch in range(25):
    for each batch in batch size:
      backward(set_train_x[batch],set_train_y[batch],learning_rate,momentum,reg)
```  
    

##### forward propagation function
```python
def forward(input_value):
  hidden_layer =reLu_function(input_value * weight[0] + bias_1)
  output_layer =sigmoid_function(hidden_layer * weight[1] + bias_2)
  retrun softmax(output_layer)
```  
##### backward propagation function
```python
def backward(inputValue, target,learning_rate,momentum,reg):
  num =  number of tuple in inputValue
  probs = forward(inputValue)
  delta_3 = probs
  delta_3 = delta3[range(num),target.T ] -= 1
  delta_3 /= num
  
  current_gradient_weight_2 =  hidden_layer * delta_3
  grad_weight_2 = learning_rate * current_gradient_weight2 + momentum * previous_delta_weight[1]
  grad_bias_2 = sum(delta_3) 
  
  delta_2 = delta3 * weight[1] * ReLUforBackward(hidden_layer)
  current_gradient_weight_1 = input_value * delta_2
  grad_weight_1 = learning_rate  *current_gradient_weight_1 + momentum *previous_delta_weight[0]
  grad_bias_1 = sum(delta_2)
  
  # Add regularization for delta weights
  grad_weight_2 += reg * weight[1]
  grad_weight_1 += reg * weight[0]
  
  #update biases and weights
  bias_2 += -learning_rate * grad_bias_2
  weight[1] -=  grad_weight_2
  weight[0] -=  grad_weight_1
  bias_1 += -learning_rate * grad_bias_1
  
  # update previous delta weights 
  previous_delta_weight[0] = grad_weight_1
  previous_delta_weight[1] = grad_weight_2
```  

