from email.mime import base
import os
from datetime import datetime
import wave

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

import semivariables as sv


class Printer: 
    def save_plot_family(self, x, waveformFamily, singlePlot, errorIndexes, directory):
        os.makedirs(directory, exist_ok=True)
        
        if singlePlot : 
            self.save_all_channels_to_one_file(waveformFamily, x, directory)
        else:
            self.save_one_file_per_channel(waveformFamily, x, directory)

    def save_one_file_per_channel(self, waveformFamily, x, directory):
        title, xTitle, yTitle = self.get_titles()
        for waveform in waveformFamily:
            df = self.make_channel_dataframe(x, waveform, title, xTitle, yTitle)
            self.save_datafame_to_waveform_parquet(df, title, directory)

    def save_all_channels_to_one_file(self, waveformFamily, x, directory):
        title, xTitle, yTitle = self.get_titles()
        frames = []
        for waveform in waveformFamily:
            _, _, yTitle = self.get_titles()
            frames.append(self.make_channel_dataframe(x, waveform, title, xTitle, yTitle))
        self.save_datafame_to_waveform_parquet(pd.concat(frames).reset_index(drop=True), title, directory)

    def save_datafame_to_waveform_parquet(self, dataframe, title, directory):
        print(dataframe.head())
        print(dataframe.tail())
        arrowWaveform = pa.Table.from_pandas(dataframe)
        arrowWaveform = arrowWaveform.cast(self.get_parquet_schema())
        filename = self.get_filename(title)
        pq.write_table(arrowWaveform,filename)
        os.replace(filename, f'{directory}/{filename}')

    def make_channel_dataframe(self, x, y, waveformName, xChannelName, yChannelName) -> pd.DataFrame:
        df = pd.DataFrame(
            {
                'WaveformName': [waveformName] * len(x),
                'x': x, 
                'xChannelName' : [xChannelName] * len(x),
                'xUnit': ['mV'] * len(x),
                'xBaseUnit': ['V'] * len(x),
                'xScale' : ['Linear'] * len(x),
                'y': y,
                'yChannelName' : [yChannelName] * len(x),
                'yUnit': ['mV'] * len(x),
                'yBaseUnit': ['V'] * len(x),
                'yScale' : ['Linear'] * len(x),
            }
        )
        return df

    def get_parquet_schema(self):
        waveformSchema = pa.schema(
                [
                    pa.field('WaveformName', 'string'),
                    pa.field('x', "double"),
                    pa.field('xChannelName', 'string'),
                    pa.field('xUnit', 'string'),
                    pa.field('xBaseUnit','string'),
                    pa.field('xScale', 'string'),
                    pa.field('y', "double"),
                    pa.field('yChannelName', 'string'),
                    pa.field('yUnit', 'string'),
                    pa.field('yBaseUnit','string'),
                    pa.field('yScale', 'string'),
                ],
                )
        return waveformSchema

    def get_filename(self, title):
        return f'{title}{str(datetime.now().strftime("%y%m%d%H%M%S%f"))}.parquet'.replace(' ','').replace('\\', '').replace('/','')

    def get_titles(self):
        xTitle = sv.get_random_xaxis()
        yTitle = sv.get_random_yaxis()
        title = f'{sv.get_random_discipline()} {yTitle}'
        return title, xTitle, yTitle