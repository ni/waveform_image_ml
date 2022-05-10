import math

import numpy as np
import numpy.random as rnd
from tqdm import tqdm


class Generator:

    def gen_uniform_based_waveform_family(self, waveformsPerFamily, familyNumber):
        factorOfWaveformsWithError = 0.3
        numberWithErrors = math.floor(
            waveformsPerFamily * factorOfWaveformsWithError * rnd.random())
        errorIndexes = rnd.randint(0, waveformsPerFamily-1, numberWithErrors)
        segments = rnd.randint(4, 8)
        xBounds = rnd.rand(2)
        xMin, xMax = np.min(xBounds), np.max(xBounds)
        xPointCount = 1000
        x = np.linspace(xMin, xMax, num=xPointCount)
        y = self.__gen_random_uniform_based_waveform(x, segments)
        waveforms = []
        for n in tqdm(range(waveformsPerFamily), desc=f'Generating Waveforms for family {familyNumber}'):
            lineBounds = rnd.random(2)
            line = np.linspace(
                lineBounds.min(), lineBounds.max(), num=xPointCount)
            ys = y * line
            if n in errorIndexes:
                ys = self.__introduce_error(ys)
            waveforms.append(ys)
        waveforms = self.__add_noise(waveforms)
        return x, waveforms, errorIndexes

    def __gen_random_uniform_based_waveform(self, x, segments):
        y = (x - rnd.uniform(-1, 1))
        for s in range(segments):
            y = y * (x - rnd.uniform(-1, 1))
        return y

    def __introduce_error(self, y):
        errorType = rnd.randint(0, 3)
        if errorType == 0:
            return self.__introduce_narrow_spike(y)
        elif errorType == 1:
            return self.__introduce_step(y)
        elif errorType == 2:
            return self.__introduce_constant_error(y)
        return y

    def __introduce_narrow_spike(self, y):
        y_error = y
        min, max = np.min(y), np.max(y)
        spike_height = np.abs(max-min) * rnd.random()
        errorPoint = rnd.randint(0, len(y))
        y_error[errorPoint] = y_error[errorPoint] + spike_height
        return y_error

    def __introduce_step(self, y):
        y_error = y
        errorPointMin, errorPointMax = self.__get_error_range(y)
        delta = self.__get_random_value_in_y_range_with_factor(y)
        y[errorPointMin:errorPointMax] = y[errorPointMin: errorPointMax] + delta
        return y_error

    def __introduce_constant_error(self, y):
        y_error = y
        min, max = self.__get_error_range(y)
        error_value = self.__get_random_value_in_y_range_with_factor(y)
        y[min:max] = error_value
        return y_error

    def __get_error_range(self, y):
        bounds = rnd.rand(2)
        maxErrorLength = len(y) / 2
        return math.floor(np.min(bounds) * maxErrorLength), math.ceil(np.max(bounds) * maxErrorLength)

    def __get_random_value_in_y_range_with_factor(self, y):
        errorScale = rnd.uniform(-1, 1)
        percentRangeForError = 1.5
        return (np.max(y) - np.min(y)) * errorScale * percentRangeForError

    def __add_noise(self, waveforms):
        scale = (np.max(waveforms) - np.min(waveforms)) * \
            np.abs(rnd.normal(0, .005))
        withNoise = []
        for w in waveforms:
            noise = np.random.normal(0, scale, w.shape)
            withNoise.append(w+noise)
        return withNoise
