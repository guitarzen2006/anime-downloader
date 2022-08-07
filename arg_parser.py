import argparse
import bcolors

def arguments():
    """
    Command line arguments module.


    """
    parser = argparse.ArgumentParser( prog="anipy-cli-script.py", description="An application for automated anime series downloads.")
    parser.add_argument("series_name", nargs="*", help="Name of the Series in Romanji or English version. Must be accurate.")
    parser.add_argument("-e", "--episode_num", nargs=1, type=int, help="Epsidoe number of a series.")
    parser.add_argument("-L", "--Latest", "--latest", help="Download the latest episode.", action="store_true")
    parser.add_argument("-f", "--file", metavar="filename.csv", help="Process list of anime series from file")
    args = parser.parse_args()

    if args.Latest:
        pass
    elif args.episode_num != None:
        pass
    else:
        print(f"{bcolors.FAIL}Missing episode number (-e | --episode_num) paramenter or choose latest episode with (-L | --Latest | --latest) argument.{bcolors.ENDC}")

    return args
