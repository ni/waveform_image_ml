import mplformat as mplf
import plotlyformat as ptly
import uniformwaveform

IMAGE_DIRECTORY = "images"


def gen_random_square_wave():
    # make this have random heights (gausian in some range)
    return 1


def gen_uniform_based_waveforms(numFamilies, waveformsPerFamily, singlePlot, printer):
    print(f"Total: {numFamilies * waveformsPerFamily}. Creating {numFamilies} waveform families with {waveformsPerFamily} waveforms per family.")
    uniform_gen = uniformwaveform.Generator()
    for f in range(numFamilies):
        x, waveformFamily, errorIndexes = uniform_gen.gen_uniform_based_waveform_family(waveformsPerFamily, f)
        printer.save_plot_family(x, waveformFamily, singlePlot, errorIndexes, IMAGE_DIRECTORY)


def main():
    formatters = [mplf.Printer(), ptly.Printer()]
    numberOfFamilies = 2
    waveformsPerFamily = 5
    for formatter in formatters:
        gen_uniform_based_waveforms(numberOfFamilies, waveformsPerFamily, singlePlot=False, printer=formatter)


if __name__ == "__main__":
    main()