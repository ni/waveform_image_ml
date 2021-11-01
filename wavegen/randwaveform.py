import mplformat as mplf
import uniformwaveform

IMAGE_DIRECTORY = "images"


def gen_random_square_wave():
    # make this have random heights (gausian in some range)
    return 1


def gen_uniform_based_waveforms(numFamilies, waveformsPerFamily, genFamiliesOnSinglePlot, printer):
    print(f"Total: {numFamilies * waveformsPerFamily}. Creating {numFamilies} waveform families with {waveformsPerFamily} waveforms per family.")
    uniform_gen = uniformwaveform.Generator()
    for f in range(numFamilies):
        x, waveforms, errorIndexes = uniform_gen.gen_uniform_based_waveform_family(waveformsPerFamily, f)
        printer.save_plots(x, waveforms, genFamiliesOnSinglePlot, errorIndexes, IMAGE_DIRECTORY)


def main():
    gen_uniform_based_waveforms(1, 5, genFamiliesOnSinglePlot=False, printer=mplf.Printer())


if __name__ == "__main__":
    main()
