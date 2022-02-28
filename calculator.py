from numpy import expand_dims, repeat, swapaxes, abs, sum, where


def hamming_group(observed_sample, sample_group, threshold=None):
    """
    Calculate the Hamming distances between the observed sample and all the samples in sample group.

    :param observed_sample: one-dimensional variable array, the shape of which could be (variable number,).
    :type observed_sample: numpy.ndarray

    :param sample_group: two-dimensional variable array, the shape of which could be (sample number, variable number).
    :type sample_group: numpy.ndarray

    :param threshold: threshold for real number system.
    :type threshold: float or None

    :return: hamming distance array between the observed sample and sample group.
    :rtype: numpy.ndarray

    Example
        >>> from numpy import array
        >>> from calculator import hamming_group
        >>> sample = array([0, 1, 0])
        >>> sample_group = array([[1, 1, 0], [0, 1, 1], [0, 1, 0]])
        >>> hamming_group(observed_sample=sample, sample_group=sample_group, threshold=None)
        array([1, 1, 0])
        >>> sample = array([0.2, 0.5, 0.8])
        >>> sample_group = array([[0.7, 0.1, 0.2], [0.3, 0.4, 0.7], [0.9, 0.2, 0.4]])
        >>> hamming_group(observed_sample=sample, sample_group=sample_group, threshold=0.4)
        array([2, 0, 1])

    .. note:
        The variable number of parameter 'observed_sample' and 'sample_group' should be equal.
    """

    sample = expand_dims(observed_sample, axis=0)

    matrix = abs(sample_group - sample)

    if threshold is None:
        matrix = matrix.astype(bool)  # set bool for illustrating the difference flag rapidly.
    else:
        matrix = where(matrix > threshold, 1, 0)   # use 'where' function for real number system with threshold.

    distances = sum(matrix, axis=1)

    return distances


def hamming_matrix(samples, other_samples=None, threshold=None):
    """
    Calculate hamming matrix between samples.

    :param samples: two-dimensional sample array, the shape of which could be (sample number, variable number).
    :type samples: numpy.ndarray

    :param other_samples: another two-dimensional sample array with above-mentioned shape.
    :type other_samples: numpy.ndarray

    :param threshold: threshold for real number system.
    :type threshold: float or None

    :return: hamming distance matrix of samples.
    :rtype: numpy.ndarray

    Example
        >>> from numpy import array
        >>> from calculator import hamming_matrix
        >>> samples_1 = array([[1, 1, 0], [0, 1, 1], [0, 1, 0]])
        >>> hamming_matrix(samples=samples_1)
        array([[0, 2, 1],
               [2, 0, 1],
               [1, 1, 0]])
        >>> samples_2 = array([[0, 0, 1], [1, 0, 1]])
        >>> hamming_matrix(samples=samples_1, other_samples=samples_2)
        array([[3, 2],
               [1, 2],
               [2, 3]])
        >>> samples_1 = array([[0.7, 0.1, 0.2], [0.3, 0.4, 0.7], [0.9, 0.2, 0.4]])
        >>> hamming_matrix(samples=samples_1, threshold=0.4)
        array([[0, 1, 0],
               [1, 0, 1],
               [0, 1, 0]])
        >>> samples_2 = array([[0.6, 0.7, 0.8], [0.5, 0.9, 0.1]])
        >>> hamming_matrix(samples=samples_1, other_samples=samples_2, threshold=0.4)
        array([[2, 1],
               [0, 2],
               [1, 1]])

    .. note::
        The variable number of parameter 'samples' and 'other_samples' should be equal.

        If 'other_samples' is None, the shape of outputted matrix is (sample number, sample number).
        Otherwise, that of outputted matrix is (sample number, other sample number).
    """

    # prepare for the cross subtraction for samples or two sample groups.
    if other_samples is None:
        former = repeat(expand_dims(samples, 0), len(samples), 0)
        latter = swapaxes(former.copy(), 0, 1)
    else:
        former = repeat(expand_dims(other_samples, 0), len(samples), 0)
        latter = swapaxes(repeat(expand_dims(samples, 0), len(other_samples), 0), 0, 1)

    # do cross subtraction to define the actual difference between any two samples in the same position.
    matrix = abs(former - latter)

    if threshold is None:
        matrix = matrix.astype(bool)  # set bool for illustrating the difference flag rapidly.
    else:
        matrix = where(matrix > threshold, 1, 0)   # use 'where' function for real number system with threshold.

    matrix = sum(matrix, axis=2, dtype=int)  # calculate hamming distances.

    return matrix
