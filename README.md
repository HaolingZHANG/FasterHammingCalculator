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
Please see [here]() for detailed.