import csv 
import math
import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
from numpy.core.function_base import linspace
import semivariables as sv
from tqdm import tqdm

IMAGE_DIRECTORY = 'images'
LABEL_FILE = 'labels.csv'

def save_labels_to_csv(savefolder, labels):
    with open(os.path.join(savefolder, LABEL_FILE), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(labels)

def save_plot(xTitle, yTitle, classification):
    plt.figure(figsize=(7,5), dpi=200)
    title = f'{sv.get_random_discipline()} {yTitle}'
    current_time = datetime.now().strftime("%y%m%d%H%M%S")
    filename = f'{IMAGE_DIRECTORY}/{title}{str(current_time)}.png'
    plt.title(title)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.savefig(filename)
    plt.cla()
    save_labels_to_csv(IMAGE_DIRECTORY, [filename, classification])
    return filename

def save_plots(x, waveforms, genFamiliesOnSinglePlot, errorIndexes):
    os.makedirs(IMAGE_DIRECTORY,exist_ok=True)
    xTitle = sv.get_random_xaxis()
    yTitle = sv.get_random_yaxis()
    if genFamiliesOnSinglePlot:
        for y in waveforms:
            plt.plot(x, y, color=random_color())
        save_plot(xTitle, yTitle)
    else:
        for n in range(len(waveforms)):
            ylim = get_max_y_axis_plot_scale(x, waveforms)
            plt.plot(x, waveforms[n], color=random_color())
            plt.gca().set_ylim(ylim)
            label = 'good'
            if n in errorIndexes:
                label='bad'
            save_plot(xTitle, yTitle, label)

def get_max_y_axis_plot_scale(x, waveforms):
    for w in waveforms:
        plt.plot(x, w)
    limits = plt.gca().get_ylim()
    plt.cla()
    return limits

def gen_random_square_wave():
    # make this have random heights (gausian in some range)
    return 1

def add_noise(waveforms):
    scale = (np.max(waveforms) - np.min(waveforms)) * np.abs(rnd.normal(0,.005))
    withNoise = []
    for w in waveforms:
        noise = np.random.normal(0, scale, w.shape)
        withNoise.append(w+noise)
    return withNoise

def random_color():
    return (rnd.random(), rnd.random(), rnd.random())

def gen_random_uniform_based_waveform(x, segments):
    y = (x - rnd.uniform(-1, 1))
    for s in range(segments):
        y = y * (x - rnd.uniform(-1, 1))
    return y

def get_error_range(y):
    bounds = rnd.rand(2)
    maxErrorLength = len(y) / 2
    return math.floor(np.min(bounds) * maxErrorLength), math.ceil(np.max(bounds) * maxErrorLength)

def get_random_value_in_y_range_with_factor(y):
    errorScale = rnd.uniform(-1,1)
    percentRangeForError = 1.5
    return (np.max(y) - np.min(y)) * errorScale * percentRangeForError

def introduce_narrow_spike(y):
    y_error = y
    min, max = np.min(y), np.max(y)
    spike_height = np.abs(max-min) * rnd.random()
    errorPoint = rnd.randint(0,len(y))
    y_error[errorPoint] = y_error[errorPoint] + spike_height
    return y_error

def introduce_step(y):
    y_error = y
    errorPointMin, errorPointMax = get_error_range(y)
    delta = get_random_value_in_y_range_with_factor(y)
    y[errorPointMin:errorPointMax] = y[errorPointMin : errorPointMax] + delta
    return y_error

def inroduce_constant_error(y):
    y_error = y
    min, max = get_error_range(y)
    error_value = get_random_value_in_y_range_with_factor(y)
    y[min:max] = error_value
    return y_error

def introduce_error(y):
    errorType = rnd.randint(0,3)
    if errorType == 0:
        return introduce_narrow_spike(y)
    elif errorType == 1:
        return introduce_step(y)
    elif errorType ==2:
        return inroduce_constant_error(y)
    return y

def gen_uniform_based_waveform_family(waveformsPerFamily):
    factorOfWaveformsWithError = 0.3
    numberWithErrors = math.floor(waveformsPerFamily * factorOfWaveformsWithError * rnd.random())
    errorIndexes = rnd.randint(0, waveformsPerFamily-1,numberWithErrors)
    segments = rnd.randint(4,8)
    xBounds = rnd.rand(2)
    xMin,xMax = np.min(xBounds), np.max(xBounds)
    xPointCount = 1000
    x = np.linspace(xMin, xMax, num=xPointCount)
    y = gen_random_uniform_based_waveform(x, segments)
    waveforms = []
    for n in tqdm(range(waveformsPerFamily), desc=f'Generating Waveforms for family {f}'):
        lineBounds = rnd.random(2)
        line = np.linspace(lineBounds.min(), lineBounds.max(), num=xPointCount)
        ys = y * line
        if n in errorIndexes:
            ys = introduce_error(ys)
        waveforms.append(ys)
    waveforms = add_noise(waveforms)
    return x, waveforms, errorIndexes

def gen_uniform_based_waveforms(numFamilies, waveformsPerFamily, genFamiliesOnSinglePlot):
    print(f'Total: {numFamilies*waveformsPerFamily}. Creating {numFamilies} waveform families with {waveformsPerFamily} waveforms per family.')
    for f in range(numFamilies):
        x, waveforms, errorIndexes = gen_uniform_based_waveform_family(waveformsPerFamily)
        save_plots(x, waveforms, genFamiliesOnSinglePlot, errorIndexes)

def main():
    gen_uniform_based_waveforms(10, 5, genFamiliesOnSinglePlot=False)

if __name__ == "__main__":
    main()
