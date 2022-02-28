from numpy import random, zeros, sum, abs, all
from unittest import TestCase

from calculator import hamming_group, hamming_matrix


class TestBinaryGroup(TestCase):

    def setUp(self):
        self.repeat_time = 100

    # noinspection PyTypeChecker
    def test(self):
        for _ in range(self.repeat_time):
            sample = random.randint(0, 2, size=(100,))
            # 200 samples, each sample contains 100 bool variables.
            sample_group = random.randint(0, 2, size=(200, 100))
            requested_distances = zeros(shape=(len(sample_group),), dtype=int)
            for position in range(len(sample_group)):
                value = sum(sample != sample_group[position])
                requested_distances[position] = value

            predicted_distances = hamming_group(observed_sample=sample, sample_group=sample_group, threshold=None)

            self.assertEqual(all(requested_distances == predicted_distances), True)


class TestIntegerGroup(TestCase):

    def setUp(self):
        self.repeat_time = 100

    # noinspection PyTypeChecker
    def test(self):
        for _ in range(self.repeat_time):
            sample = random.randint(0, 50, size=(100,))
            # 200 samples, each sample contains 100 integer variables (value belongs to 0 ~ 49).
            sample_group = random.randint(0, 50, size=(200, 100))
            requested_distances = zeros(shape=(len(sample_group),), dtype=int)
            for position in range(len(sample_group)):
                value = sum(sample != sample_group[position])
                requested_distances[position] = value

            predicted_distances = hamming_group(observed_sample=sample, sample_group=sample_group, threshold=None)

            self.assertEqual(all(requested_distances == predicted_distances), True)


class TestRealGroup(TestCase):

    def setUp(self):
        self.repeat_time = 100
        self.threshold = 0.5

    # noinspection PyTypeChecker, PyArgumentList
    def test(self):
        for _ in range(self.repeat_time):
            sample = random.random(size=(100,))
            # 200 samples, each sample contains 100 integer variables (value belongs to 0 ~ 1).
            sample_group = random.random(size=(200, 100))
            requested_distances = zeros(shape=(len(sample_group),), dtype=int)
            for position in range(len(sample_group)):
                values = abs(sample - sample_group[position])
                value = len(values[values > self.threshold])
                requested_distances[position] = value

            predicted_distances = hamming_group(observed_sample=sample, sample_group=sample_group,
                                                threshold=self.threshold)

            self.assertEqual(all(requested_distances == predicted_distances), True)


class TestBinaryMatrix(TestCase):

    def setUp(self):
        self.repeat_time = 100

    # noinspection PyTypeChecker
    def test(self):
        for _ in range(self.repeat_time):
            # 200 samples, each sample contains 100 bool variables.
            samples = random.randint(0, 2, size=(200, 100))
            requested_matrix = zeros(shape=(len(samples), len(samples)), dtype=int)
            for position_1 in range(len(samples) - 1):
                for position_2 in range(position_1 + 1, len(samples)):
                    value = sum(samples[position_1] != samples[position_2])
                    requested_matrix[position_1, position_2] = value
                    requested_matrix[position_2, position_1] = value

            predicted_matrix = hamming_matrix(samples=samples, threshold=None)

            self.assertEqual(all(requested_matrix == predicted_matrix), True)


class TestIntegerMatrix(TestCase):

    def setUp(self):
        self.repeat_time = 100

    # noinspection PyTypeChecker
    def test(self):
        for _ in range(self.repeat_time):
            # 200 samples, each sample contains 100 integer variables (value belongs to 0 ~ 49).
            samples = random.randint(0, 50, size=(200, 100))
            requested_matrix = zeros(shape=(len(samples), len(samples)), dtype=int)
            for position_1 in range(len(samples) - 1):
                for position_2 in range(position_1 + 1, len(samples)):
                    value = sum(samples[position_1] != samples[position_2])
                    requested_matrix[position_1, position_2] = value
                    requested_matrix[position_2, position_1] = value

            predicted_matrix = hamming_matrix(samples=samples, threshold=None)

            self.assertEqual(all(requested_matrix == predicted_matrix), True)


class TestRealMatrix(TestCase):

    def setUp(self):
        self.repeat_time = 10
        self.threshold = 0.5

    # noinspection PyTypeChecker, PyArgumentList
    def test(self):
        for _ in range(self.repeat_time):
            # 200 samples, each sample contains 100 real number variables (value belongs to 0 ~ 1).
            samples = random.random(size=(200, 100))
            requested_matrix = zeros(shape=(len(samples), len(samples)), dtype=int)
            for position_1 in range(len(samples) - 1):
                for position_2 in range(position_1 + 1, len(samples)):
                    values = abs(samples[position_1] - samples[position_2])
                    value = len(values[values > self.threshold])
                    requested_matrix[position_1, position_2] = value
                    requested_matrix[position_2, position_1] = value

            predicted_matrix = hamming_matrix(samples=samples, threshold=self.threshold)

            self.assertEqual(all(requested_matrix == predicted_matrix), True)


class TestWithMatrix(TestCase):

    def setUp(self):
        self.repeat_time = 10

    # noinspection PyTypeChecker
    def test(self):
        for _ in range(self.repeat_time):
            # 200 samples, each sample contains 100 bool variables.
            samples_1 = random.randint(0, 2, size=(200, 100))
            # 300 samples, each sample contains 100 bool variables.
            samples_2 = random.randint(0, 2, size=(300, 100))
            requested_matrix = zeros(shape=(len(samples_1), len(samples_2)), dtype=int)
            for position_1 in range(len(samples_1)):
                for position_2 in range(len(samples_2)):
                    value = sum(samples_1[position_1] != samples_2[position_2])
                    requested_matrix[position_1, position_2] = value

            predicted_matrix = hamming_matrix(samples=samples_1, other_samples=samples_2, threshold=None)

            self.assertEqual(all(requested_matrix == predicted_matrix), True)
