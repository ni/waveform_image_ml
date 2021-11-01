import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy.random as rnd

import Labels
import semivariables as sv

class Printer:
    def save_plot(self, xTitle, yTitle, classification, directory):
        title = f'{sv.get_random_discipline()} {yTitle}'
        current_time = datetime.now().strftime("%y%m%d%H%M%S%f")
        filename = f'{directory}/{title}{str(current_time)}.png'
        plt.title(title)
        plt.xlabel(xTitle)
        plt.ylabel(yTitle)
        plt.savefig(filename)
        plt.cla()
        Labels.save_labels_to_csv(directory, [filename, classification])
        return filename


    def save_plots(self, x, waveforms, genFamiliesOnSinglePlot, errorIndexes, directory):
        os.makedirs(directory, exist_ok=True)
        xTitle = sv.get_random_xaxis()
        yTitle = sv.get_random_yaxis()
        plt.figure(figsize=(7, 5), dpi=200)
        if genFamiliesOnSinglePlot:
            for y in waveforms:
                plt.plot(x, y, color=self.random_color())
            self.save_plot(xTitle, yTitle)
        else:
            for n in range(len(waveforms)):
                ylim = self.get_max_y_axis_plot_scale(x, waveforms)
                plt.plot(x, waveforms[n], color=self.random_color())
                plt.gca().set_ylim(ylim)
                label = 'good'
                if n in errorIndexes:
                    label = 'bad'
                self.save_plot(xTitle, yTitle, label, directory)


    def get_max_y_axis_plot_scale(self, x, waveforms):
        for w in waveforms:
            plt.plot(x, w)
        limits = plt.gca().get_ylim()
        plt.cla()
        return limits


    def random_color(self):
        return (rnd.random(), rnd.random(), rnd.random())
