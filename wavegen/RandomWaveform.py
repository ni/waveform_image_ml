import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy.random as rnd

import semivariables as sv
import UniformWaveform

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

def random_color():
    return (rnd.random(), rnd.random(), rnd.random())

def gen_uniform_based_waveforms(numFamilies, waveformsPerFamily, genFamiliesOnSinglePlot):
    print(f'Total: {numFamilies*waveformsPerFamily}. Creating {numFamilies} waveform families with {waveformsPerFamily} waveforms per family.')
    generator = UniformWaveform.generator()
    for f in range(numFamilies):
        x, waveforms, errorIndexes = generator.gen_uniform_based_waveform_family(waveformsPerFamily, f)
        save_plots(x, waveforms, genFamiliesOnSinglePlot, errorIndexes)

def main():
    gen_uniform_based_waveforms(10, 5, genFamiliesOnSinglePlot=False)

if __name__ == "__main__":
    main()
