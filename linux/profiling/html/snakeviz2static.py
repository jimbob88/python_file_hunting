#!/usr/bin/env python
"""
Prepare an HTML file from SnakeViz for use as a static page.
This makes it so all static files are loaded from a CDN instead
of from the local server.

To get the SnakeViz HTML file run the snakeviz CLI to load a profile
in your browser, than save that page as an HTML file to your computer.

Finally, run this script on that HTML file.
This script prints the modified HTML to stdout.

"""
from __future__ import print_function

import argparse
import re
import sys

# This regex excludes the lines in the Worker that look like
# event.data['url'] + "/static/vendor/immutable.min.js"
RESTR = r'(?<!] \+ ")/static/'
REPLACE_WITH = \
    'https://cdn.rawgit.com/jiffyclub/snakeviz/v0.4.2/snakeviz/static/'

# REPLACE_DICT = {
#     r"(\"\w+_files/)(snakeviz.css)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/snakeviz.css"',
#     r"(\"\w+_files/)(jquery.css)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/jquery.dataTables.min.css"',
#     r"(\"\w+_files/)(jquery-3.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/jquery-3.2.1.min.js"',
#     r"(\"\w+_files/)(jquery.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/jquery.dataTables.min.js"',
#     r"(\"\w+_files/)(d3.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/d3.v3.min.js"',
#     r"(\"\w+_files/)(lodash.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/lodash.min.js"',
#     r"(\"\w+_files/)(immutable.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/immutable.min.js"',
#     r"(\"\w+_files/)(snakeviz.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/snakeviz.js"',
#     r"(\"\w+_files/)(drawsvg.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/drawsvg.js"'
# }

REPLACE_DICT = {
    r"(\"\w+_files/)(snakeviz.css)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/snakeviz.css"',
    r"(\"\w+_files/)(jquery.css)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/jquery.dataTables.min.css"',
    r"(\"\w+_files/)(jquery-3.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/jquery-3.2.1.min.js"',
    r"(\"\w+_files/)(jquery.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/jquery.dataTables.min.js"',
    r"(\"\w+_files/)(d3.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/d3.v3.min.js"',
    r"(\"\w+_files/)(lodash.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/lodash.min.js"',
    r"(\"\w+_files/)(immutable.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/vendor/immutable.min.js"',
    r"(\"\w+_files/)(snakeviz.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/snakeviz.js"',
    r"(\"\w+_files/)(drawsvg.js)\"": '"https://cdn.jsdelivr.net/gh/jiffyclub/snakeviz/snakeviz/static/drawsvg.js"'
}

def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description=(
            'Prepare an HTML file from SnakeViz for use as a static page. '
            'The modified HTML is printed to stdout.'))
    parser.add_argument(
        'htmlfile', type=str,
        help='HTML to convert to a static page.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    with open(args.htmlfile, 'r') as f:
        html = f.read()
    # args.htmlfile.write(re.sub(RESTR, REPLACE_WITH, html))
    for re_str, re_with in REPLACE_DICT.items():
        html = re.sub(re_str, re_with, html)
    print(html)
    with open(args.htmlfile, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    sys.exit(main())

