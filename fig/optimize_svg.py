#!/usr/bin/env python3
"""
Optimize SVG files.
Execute `./optimize_svg.py --help` for more information.
"""

from pathlib import Path
import argparse
import re
import subprocess
import sys

def detect_optimizers():
    """
    Detect available SVG optimizers.
    Currently checks:
        - svgcleaner
        - svgo
        - scour
    """
    available_optimizers = []

    # Check if we have svgcleaner
    command = ["svgcleaner", "--version"]
    process = subprocess.run(command, capture_output=True)
    if not process.stderr:
        available_optimizers.append('svgcleaner')
        output = process.stdout.decode("ascii").split()
        if __name__ == '__main__':
            print("Found 'svgcleaner' version", output[1])

    # Check if we have svgo
    command = ["svgo", "--version"]
    process = subprocess.run(command, capture_output=True)
    if not process.stderr:
        available_optimizers.append('svgo')
        output = process.stdout.decode("ascii").split()
        if __name__ == '__main__':
            print("Found 'svgo' version", output[0])

    # Check if we have scour
    try:
        from scour import scour
    except ImportError:
        pass
    else:
        available_optimizers.append('scour')
        if __name__ == '__main__':
            print("Found 'scour' version", scour.__version__)

    return available_optimizers


def select_optimizer(choice):
    """
    Select an optimizer to use.
    Allowed choices:
        - auto
        - all
        - svgo (if available)
        - svgcleaner (if available)
        - scour (if available)
    """

    possible = ['svgcleaner', 'svgo', 'scour']
    available = detect_optimizers()
    allowed = ["auto", "all"] + available

    if choice not in allowed:
        print(f"Selected optimizer ({choice}) is not available.", file=sys.stderr)
        return []

    if choice == 'auto':
        if available:
            optimizer = [available[0]]
        else:
            optimizer = []
    elif choice == 'all':
        optimizer = available
    else:
        optimizer = [choice]

    return optimizer

### Functions

def optimize(optimizer, files):
    """Optimize (SVG) files using specified optimizer."""

    if optimizer == 'svgcleaner':
        optimize_with_svgcleaner(files)

    if optimizer == 'svgo':
        optimize_with_svgo(files)

    if optimizer == 'scour':
        optimize_with_scour(files)


def optimize_with_scour(files):
    from scour import scour
    """
    Optimize SVG files using Scour.
    """

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
    options.quiet = True

    for file in files:
        options.infilename = file
        options.outfilename = file[:-4] + "-scoured.svg"

        try:
            # .start will close the files. Weird flex but ok
            with open(file, 'rb') as infile, open(options.outfilename, 'wb') as outfile:
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
            Path(options.outfilename).rename(file)

def optimize_with_svgcleaner(files):
    """
    Optimize SVG files using SVGcleaner.
    Used options:
        - indent 2
        - ungroup-defs no
        - multipass
        - coordinates-precision 1
        - properties-precision 1
        - paths-coordinates-precision 1
    """
    basic_command = [
            "svgcleaner",
            "--indent", "2",
            "--ungroup-defs", "no",
            "--multipass",
            "--coordinates-precision", "1",
            "--properties-precision", "1",
            "--paths-coordinates-precision", "1"
            ]
    for file in files:
        output_file = file[:-4] + "-svgcleaned.svg"
        command = basic_command + [file, output_file]
        process = subprocess.run(command, capture_output=True)
        if process.returncode:
            error_stream = process.stderr.decode("ascii")
            if not re.match(r'Your image is .+? smaller now.', error_stream):
                print(f"Failed to optimize '{file}' with SVGcleaner:", file=sys.stderr)
                print(error_stream, file=sys.stderr)
                if Path(output_file).is_file():
                    Path(output_file).unlink()
        else:
            if Path(output_file).is_file():
                Path(output_file).rename(file)

def optimize_with_svgo(files):
    """
    Optimize SVG files using SVGO.
    Uses the following options:
        - multipass
        - pretty
        - indent=2
        - enables the following plugins:
            * sortAttrs
            * removeStyleElement
            * removeScriptElement
            * removeOffCanvasPaths
    """
    basic_command = [
            "svgo",
            "--multipass",
            "--pretty",
            "--indent=2",
            "--enable={sortAttrs,removeStyleElement,removeScriptElement,removeOffCanvasPaths}"
            ]
    for file in files:
        output_file = file[:-4] + "-svgo.svg"
        command = basic_command + ["-i", file, "-o", output_file]
        process = subprocess.run(command, capture_output=True)
        if process.returncode:
            print(f"Failed to optimize '{file}' with SVGO", file=sys.stderr)
            print(process.stderr.decode("ascii"), file=sys.stderr)
            if Path(output_file).is_file():
                Path(output_file).unlink()
        else:
            if Path(output_file).is_file():
                Path(output_file).rename(file)


def manual_cleanup(files):
    """
    Remove junk settings from SVG files generated with Matplotlib.
    Currently removes:
        - font-family="DejaVu Sans"
        - stroke-width=".8"
        - transform="rotate(-0 ...)"
    """
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
        output_file = file[:-4] + "-cleaned.svg"
        try:
            with open(file, "r") as infile, open(output_file, "w") as outfile:
                for line in infile:
                    if line.startswith("<!DOCTYPE"): continue
                    for txt in text_to_remove: line = line.replace(txt, "")
                    for pat in patterns_to_remove: line = re.sub(pat, "", line)
                    if line == '\n': continue
                    outfile.write(line)
        except:
            print("Failed to clean up:", file)
            if Path(output_file).is_file():
                Path(output_file).unlink()
        else:
            if Path(output_file).is_file():
                Path(output_file).rename(file)


if __name__ == '__main__':

    description = """
    Optimize SVG files using available tools.
    """

    # Specify permissible command-line arguments and parse them
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-o', metavar="optimizer",
                        help="An optimizer to use. Options: svgcleaner, svgo, scour, auto, all",
                        choices=['svgcleaner', 'svgo', 'scour', 'auto', 'all'],
                        default='auto')
    parser.add_argument('files',
                        metavar='svg_file',
                        help="SVG file(s) to optimize.", nargs='+')
    args = parser.parse_args()
    sys.argv = [''] # scour uses OptParse which processes OUR args! argh!


    for opt in select_optimizer(args.o):
        print("Optimizing using:", opt)
        optimize(opt, args.files)

    manual_cleanup(args.files)
