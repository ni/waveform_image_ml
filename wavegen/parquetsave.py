import os
from datetime import datetime

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

import semivariables as sv


class Printer: 
    def save_plot_family(self, x, waveformFamily, singlePlot, errorIndexes, directory):
        os.makedirs(directory, exist_ok=True)
        xTitle = sv.get_random_xaxis()
        yTitle = sv.get_random_yaxis()
        title = f'{sv.get_random_discipline()} {yTitle}'
        now = datetime.now()
        waveformSchema = pa.schema(
                [
                pa.field('x', "double", metadata={'name': xTitle, 'units': 'XUNITS', 'scale':'linear'}),
                pa.field('y0', "double", metadata={'name': yTitle, 'units': 'YUNITS', 'scale':'linear'}),
                ],
                metadata={'name' : title, 'time':str(now)}
            )
        for waveform in waveformFamily:
            df = pd.DataFrame({'x': x, 'y0': waveform})
            arrowWaveform = pa.Table.from_pandas(df)
            arrowWaveform = arrowWaveform.cast(waveformSchema)
            filename = f'{title}{str(datetime.now().strftime("%y%m%d%H%M%S%f"))}.parquet'.replace(' ','').replace('\\', '').replace('/','')
            pq.write_table(arrowWaveform,filename)
            os.replace(filename, f'{directory}/{filename}')