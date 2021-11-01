import csv
import os

LABEL_FILE = 'labels.csv'

def save_labels_to_csv(savefolder, labels):
    with open(os.path.join(savefolder, LABEL_FILE), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(labels)