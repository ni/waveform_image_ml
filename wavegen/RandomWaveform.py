import UniformWaveform
import MatplotlibFormat as mplf

IMAGE_DIRECTORY = 'images'


def gen_random_square_wave():
    # make this have random heights (gausian in some range)
    return 1


def gen_uniform_based_waveforms(numFamilies, waveformsPerFamily, genFamiliesOnSinglePlot):
    print(f'Total: {numFamilies*waveformsPerFamily}. Creating {numFamilies} waveform families with {waveformsPerFamily} waveforms per family.')
    generator = UniformWaveform.generator()
    for f in range(numFamilies):
        x, waveforms, errorIndexes = generator.gen_uniform_based_waveform_family(
            waveformsPerFamily, f)
        mplf.save_plots(x, waveforms, genFamiliesOnSinglePlot,
                        errorIndexes, IMAGE_DIRECTORY)


def main():
    gen_uniform_based_waveforms(10, 5, genFamiliesOnSinglePlot=False)


if __name__ == "__main__":
    main()
