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
        yTitle = sv.get_random_yaxis_title()
        title = f"{sv.get_random_discipline()} {yTitle}"
        n = 0
        fig = go.Figure()
        for waveform in waveformFamily:
            series = go.Scatter(
                x=x,
                y=waveform,
                line_color=self.random_color(),
                mode="lines",
            )
            fig.add_trace(series)

            n += 1
        fig.update_layout(
            title=title,
            xaxis_title=xTitle,
            yaxis_title=yTitle,
            width=1024,
            height=768,
        )
        current_time = datetime.now().strftime("%y%m%d%H%M%S%f")
        filename = (
            f"{title}{str(current_time)}.html".replace(" ", "")
            .replace("\\", "")
            .replace("/", "")
        )
        path = f"{directory}/{filename}"
        fig.write_html(path)
        Labels.save_labels_to_csv(directory, path, n, errorIndexes)

    def random_color(self):
        return f"rgb({rnd.random()},{rnd.random()},{rnd.random()})"
