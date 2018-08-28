'''
Author:      Jackson Cole
Affiliation: Middle Tennessee State University, United States
Date:        August 2018
'''

from sys import argv
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import random


def main(argv):
    if len(argv) > 1:
        if argv[1] == "-1":
            filename = argv[2]
            data = read_data(filename)

            plt.figure()
            plot_one(data)
            plt.show()

        elif argv[1] == "-m":
            filename_list = argv[2]

            lines = []
            with open(filename_list, 'r') as f:
                for line in f:
                    lines.append(line.rsplit()[0])

            num_plots = int(16)
            rows = int(num_plots**(1/2))
            cols = int(num_plots**(1/2))

            pp = PdfPages('multipage.pdf')
            num_plotted = 0
            while num_plotted < len(lines):
                fig, ax = plt.subplots(rows, cols)
                for i, line in zip(range(num_plots),
                        lines[num_plotted:num_plotted + num_plots]):
                    data = read_data("data/" + str(line))
                    ax = plt.subplot(rows, cols, i+1)
                    plt.plot(
                        data['Dates'],
                        data['Flux'],
                        lw=0.2,
                        )

                    ax.axes.get_xaxis().set_visible(False)
                    ax.axes.get_yaxis().set_visible(False)

                pp.savefig()
                num_plotted += num_plots
            pp.close()


    else:
        print("ERROR: No file specified.")


def read_data(filename):
    return pd.read_table(
            filename,
            delim_whitespace=True,
            header=0,
            names=(
                'Dates',
                'Cadences',
                'Flux',
                'Uncert',
                'Xpos',
                'Ypos',
                'Quality',
                ),
            )


def plot_one(data):
        plt.plot(
                data['Dates'],
                data['Flux'],
                lw=0.5,
                )


if __name__ == "__main__":
    main(argv)
