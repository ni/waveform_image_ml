import os
from datetime import datetime

import numpy.random as rnd
import plotly.graph_objects as go

import semivariables as sv
import Labels


class Printer:
    def save_plot_family(self, x, waveformFamily, singlePlot, errorIndexes, directory):
        os.makedirs(directory, exist_ok=True)
        xTitle = sv.get_random_xaxis_title()
        yTitle = sv.get_random_yaxis()
        title = f'{sv.get_random_discipline()} {yTitle}'
        n = 0
        for waveform in waveformFamily:
            fig = go.Figure()
            series = go.Scatter(
                x=x, 
                y=waveform, 
                line_color=self.random_color(), 
                mode='lines',)
            fig.add_trace(series)
            fig.update_layout(
                title=title,
                xaxis_title=xTitle,
                yaxis_title = yTitle,
                width = 700,
                height = 500
            )
            
            current_time = datetime.now().strftime("%y%m%d%H%M%S%f")
            filename = f'{title}{str(current_time)}.png'.replace(' ','').replace('\\', '').replace('/','')
            path = f'{directory}/{filename}'
            fig.write_image(path)
            Labels.save_labels_to_csv(directory, path, n, errorIndexes)
            n += 1

    def random_color(self):
        return f'rgb({rnd.random()},{rnd.random()},{rnd.random()})'
