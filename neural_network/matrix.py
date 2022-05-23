import math
import random
from random import random


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

        i = 0
        j = 0
        while i < self.rows:
            i += 1
            self.data[i] = []
            while j < self.cols:
                j += 1
                self.data[i][j] = 0

    def randomize(self):
        i = 0
        j= 0
        while i < self.rows:
            i += 1
            while j < self.cols:
                j += 1
                self.data[i][j] = random.randint(0, 500) * 2 - 1


    @staticmethod
    def multiply(a, b):

        i = 0
        j = 0
        k = 0
        if a.cols != b.rows:
            print("Columns must be the same lenght")
            return None

        result = Matrix(a.rows, b.cols)

        while i < result.rows:
            i += 1
            while j < result.cols:
                j += 1
                sum = 0
                while k < a.cols:
                    k += 1
                    sum += a.data[i][k] * b.data[k][j]
                result.data[i][j] = sum

        return result

    @staticmethod
    def from_array(arr):
        i = 0
        m = Matrix(len(arr), 1)
        while i < len(arr):
            i += 1
            m.data[i][0] = arr[i]

        return m

    def to_array(self):
        arr = []
        i = 0
        j= 0
        while i < self.rows:
            i += 1
            while j < self.cols:
                j += 1
                arr.append(self.data[i][j])
        return arr

    def map(self, func):
        i = 0
        j = 0

        while i < self.rows:
            i += 1
            while j < self.cols:
                j += 1
                val = self.data[i][j]
                self.data[i][j] = func(val)