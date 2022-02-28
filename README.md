# Faster Hamming Calculator

## Motivation
For calculating Hamming distance, an apparent strategy could be:
```python
from numpy import random, sum

variable_number = 20
sample_1 = random.randint(0, 2, size=(int(variable_number),))
sample_2 = random.randint(0, 2, size=(int(variable_number),))
distance = sum(sample_1 != sample_2)
```

However, in large-scale operations, such as 1,000,000 times, its runtime is difficult to be accepted by users.
Hence, this work is specifically designed for large-scale Hamming distance calculation.
The results shown that the runtime comparison is **our proposed** << **numpy.sum** (above one-tenth).
Detailed design is shown in [here](https://github.com/HaolingZHANG/FasterHammingCalculator/blob/main/README.ipynb).


### Comparison of Hamming distance between one sample and all other samples
This function is often used in the task of investigating 
whether an individual belongs to a population.

You can complete this task by:
```python
from numpy import array
from calculator import hamming_group
sample = array([0, 1, 0])
sample_group = array([[1, 1, 0], [0, 1, 1], [0, 1, 0]])
hamming_group(observed_sample=sample, sample_group=sample_group, threshold=None)
# array([1, 1, 0])
```

The comparison with the 'numpy.sum' method is as follows:

<p align="center">
<img src="./experiments/result.1.svg" alt="result1" title="result1", width=50%/>
</p>

Here, "x" implies that observation and statistics cannot be carried out in the unit of seconds. 

### Comparison of Hamming distance between a group of samples
This function is often used to investigate 
the differences between individuals within a population.

You can do this task through:
```python
from numpy import array
from calculator import hamming_matrix
samples = array([[1, 1, 0], [0, 1, 1], [0, 1, 0]])
hamming_matrix(samples=samples)
# array([[0, 2, 1],
#        [2, 0, 1],
#        [1, 1, 0]])
```

The comparison with the 'numpy.sum' method is as follows:

<p align="center">
<img src="./experiments/result.2.svg" alt="result1" title="result1", width=50%/>
</p>

### Comparison of Hamming distance between two groups of samples.
This function is usually used to investigate 
the individual differences between two populations.

You can finish this task using:
```python
from numpy import array
from calculator import hamming_matrix
samples_1 = array([[1, 1, 0], [0, 1, 1], [0, 1, 0]])
samples_2 = array([[0, 0, 1], [1, 0, 1]])
hamming_matrix(samples=samples_1, other_samples=samples_2)
# array([[3, 2],
#        [1, 2],
#        [2, 3]])
```

The comparison with the 'numpy.sum' method of inter population operation 
is similar as that of intra population operation.