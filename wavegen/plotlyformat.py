import os
from datetime import datetime

import numpy.random as rnd
import plotly.graph_objects as go

import semivariables as sv


class Printer:
    def save_plot_family(self, x, waveformFamily, singlePlot, errorIndexes, directory):
        os.makedirs(directory, exist_ok=True)
        xTitle = sv.get_random_xaxis()
        yTitle = sv.get_random_yaxis()
        title = f'{sv.get_random_discipline()} {yTitle}'
        for waveform in waveformFamily:
            fig = go.Figure()
            series = go.Scatter(
                x=x, 
                y=waveform, 
                line_color=self.random_color(), 
                mode='lines')
            fig.add_trace(series)
            fig.update_layout(
                title=title,
                xaxis_title=xTitle,
                yaxis_title = yTitle,
            )
            current_time = datetime.now().strftime("%y%m%d%H%M%S%f")
            filename = f'{directory}/{title}{str(current_time)}.png'
            fig.write_image(filename)

    def random_color(self):
        return f'rgb({rnd.random()},{rnd.random()},{rnd.random()})'
