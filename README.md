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
The results shown that the runtime comparison is **our proposed** << **numpy.sum**.
Detailed design is shown in [here](https://github.com/HaolingZHANG/FasterHammingCalculator/blob/main/README.ipynb).


### Comparison of Hamming distance between one sample and all other samples
This function is often used in the task of investigating 
whether an individual belongs to a population.
The comparison with the above conventional method is as follows:

<p align="center">
<img src="./experiments/result.1.svg" alt="result1" title="result1", width=50%/>
</p>

### Comparison of Hamming distance between a group of samples
This function is often used to investigate 
the differences between individuals within a population.

The comparison with the above conventional method is as follows:

<p align="center">
<img src="./experiments/result.2.svg" alt="result1" title="result1", width=50%/>
</p>

### Comparison of Hamming distance between two groups of samples.
This function is usually used to investigate 
the individual differences between two populations.

The comparison with the above two conventional methods of inter population operation 
is similar as that of intra population operation.