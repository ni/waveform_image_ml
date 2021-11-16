import csv
import os

LABEL_FILE = 'labels.csv'

def get_waveform_label(waveformIndex, errorIndexes):
    label = 'good'
    if waveformIndex in errorIndexes:
        label = 'bad'
    return label

def save_labels_to_csv(savefolder, waveformFileName, waveformIndex, errorIndexes):
    with open(os.path.join(savefolder, LABEL_FILE), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([waveformFileName, get_waveform_label(waveformIndex, errorIndexes)])