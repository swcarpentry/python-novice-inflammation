#!/usr/bin/env python3
"""
Generate figures used in the lesson episodes.
Usage: ./generate_figures.py
"""

import glob
from pathlib import Path
import re
import sys

try:
    import numpy
    import matplotlib.pyplot
except ImportError:
    print("Failed to load NumPy and/or Matplotlib", file=sys.stderr)
    exit(1)

try:
    from scour import scour
    has_scour = True
except ImportError:
    print("Scour is not installed. Can't optimize produced SVG files",
            file=sys.stderr)
    has_scour = False

# Configure Matplotlib to not convert text to outlines
# All settings: matplotlib.rcParams or matplotlib.pyplot.rcParams
matplotlib.pyplot.rcParams['svg.fonttype'] = 'none'

# Load data
data = numpy.loadtxt(fname="../data/inflammation-01.csv", delimiter=",")


# Episode 1
## Visualizing data

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.savefig("inflammation-01-imshow.svg")
matplotlib.pyplot.close()

matplotlib.pyplot.plot(numpy.mean(data, axis=0))
matplotlib.pyplot.savefig("inflammation-01-average.svg")
matplotlib.pyplot.close()

matplotlib.pyplot.plot(numpy.max(data, axis=0))
matplotlib.pyplot.savefig("inflammation-01-maximum.svg")
matplotlib.pyplot.close()

matplotlib.pyplot.plot(numpy.min(data, axis=0))
matplotlib.pyplot.savefig("inflammation-01-minimum.svg")
matplotlib.pyplot.close()

## Grouping plots
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()
matplotlib.pyplot.savefig("inflammation-01-group-plot.svg")
matplotlib.pyplot.close(fig)


## Exercise: Drawing Straight Lines
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0), drawstyle='steps-mid')

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0), drawstyle='steps-mid')

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0), drawstyle='steps-mid')

fig.tight_layout()
matplotlib.pyplot.savefig("inflammation-01-line-styles.svg")
matplotlib.pyplot.close(fig)

files = [
        "inflammation-01-imshow.svg",
        "inflammation-01-maximum.svg",
        "inflammation-01-minimum.svg",
        "inflammation-01-average.svg",
        "inflammation-01-group-plot.svg",
        "inflammation-01-line-styles.svg"
        ]

if has_scour:

    # Configure scour
    options = scour.parse_args()

    options.digits = 4
    # values lower than 4 for '.digits' led to visilble differences between
    # the original and 'optimized' file
    options.indent_depth = 2
    options.simple_colors = False
    options.enable_viewboxing = True
    options.embed_rasters = True
    options.group_create = True
    options.group_collapse = True
    options.shorten_ids = True
    options.strip_comments = True
    options.strip_ids = True
    options.strip_xml_prolog = True
    options.strip_xml_space_attribute = True
    options.remove_titles = True
    options.remove_descriptions = True
    options.remove_metadata = True
    options.remove_descriptive_elements = True

    for file in files:
        options.infilename = file
        options.outfilename = file[:-4] + "-scoured.svg"

        try:
            # .start will close the files. Weird flex but ok
            infile = open(options.infilename, 'rb')
            outfile = open(options.outfilename, 'wb')
            scour.start(options, infile, outfile)
        except FileNotFoundError:
            # Doing this because we have a list of
            # hard-coded file names
            print(f"File {file} not found")
        except:
            print("Failed to optimize:", file)
            if not infile.closed: infile.close()
            if not outfile.closed: outfile.close()
            if Path(options.outfilename).is_file():
                Path(options.outfilename).unlink()
        else:
            Path(file).unlink()
            Path(options.outfilename).rename(file)


text_to_remove = [
        # Matplotlib's default font
        'font-family="DejaVu Sans"',
        # Default stroke width of 1.0 is good enough
        'stroke-width=".8"'
        ]

patterns_to_remove = [
        # useless rotations (by 0 degrees)
        r'\s*transform="rotate\(-?0 .+?\)"',
        ]

for file in files:
    output_filename = file[:-4] + "-cleaned.svg"
    try:
        with open(file, "r") as infile, open(output_filename, "w") as outfile:
            for line in infile:
                if line.startswith("<!DOCTYPE"): continue
                for txt in text_to_remove: line = line.replace(txt, "")
                for pat in patterns_to_remove: line = re.sub(pat, "", line)
                if line == '\n': continue
                outfile.write(line)
    except:
        print("Failed to clean up:", file)
        if Path(output_filename).is_file():
            Path(output_filename).unlink()
    else:
        Path(file).unlink()
        Path(output_filename).rename(file)
