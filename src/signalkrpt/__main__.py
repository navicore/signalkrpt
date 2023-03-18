#!/usr/bin/env python3
"""
gen signal k diagram and report gen
"""
import argparse
from signalkrpt.gen_dot import gen_dot
from signalkrpt.gen_scatterplot import gen_scatterplot

def main():
    """
    entry point
    """
    parser = argparse.ArgumentParser(description='Generate and move boats in Signal K format')
    parser.add_argument('--gen-scatterplot', action='store_true', help='Generate scatter-plot')
    parser.add_argument('--gen-dot', action='store_true', help='Generate dot diagram')
    args = parser.parse_args()

    if args.gen_dot:
        gen_dot(args)
    elif args.gen_scatterplot:
        gen_scatterplot(args)
    else:
        print("not implemented")

if __name__ == "__main__":
    main()
