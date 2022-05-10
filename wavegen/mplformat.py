import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy.random as rnd

import Labels
import semivariables as sv

class Printer:
    def save_plot(self, xTitle, yTitle, directory, waveformIndex, errorIndexes):
        title = f'{sv.get_random_discipline()} {yTitle}'
        current_time = datetime.now().strftime("%y%m%d%H%M%S%f")
        filename = f'{title}{str(current_time)}.png'.replace(' ','').replace('\\', '').replace('/','')
        path = f'{directory}/{filename}'
        plt.title(title)
        plt.xlabel(xTitle)
        plt.ylabel(yTitle)
        plt.savefig(path)
        plt.cla()
        Labels.save_labels_to_csv(directory, path, waveformIndex, errorIndexes)
        return path


    def save_plot_family(self, x, waveformFamily, singlePlot, errorIndexes, directory):
        os.makedirs(directory, exist_ok=True)
        xTitle = sv.get_random_xaxis_title()
        yTitle = sv.get_random_yaxis_title()
        plt.figure(figsize=(7, 5), dpi=200)
        if singlePlot:
            for wavecorm in waveformFamily:
                plt.plot(x, wavecorm, color=self.random_color())
            self.save_plot(xTitle, yTitle, directory, 0, errorIndexes)
        else:
            for n in range(len(waveformFamily)):
                ylim = self.get_max_y_axis_plot_scale(x, waveformFamily)
                plt.plot(x, waveformFamily[n], color=self.random_color())
                plt.gca().set_ylim(ylim)
                self.save_plot(xTitle, yTitle, directory, n, errorIndexes)


    def get_max_y_axis_plot_scale(self, x, waveforms):
        for w in waveforms:
            plt.plot(x, w)
        limits = plt.gca().get_ylim()
        plt.cla()
        return limits


    def random_color(self):
        return (rnd.random(), rnd.random(), rnd.random())
