"""
The command-line interface for the repometrics
"""
import argparse
from .repometrics import repometrics


def main():
    parser = argparse.ArgumentParser(
        description="An language repo metrics for Project folders."
    )
    parser.add_argument(
        "url", type=str,
        help="The path for which language metrics is required."
    )
   
    args = parser.parse_args()
    lang_metrics = repometrics(args.url)
    print("Language Metrics {}".format(lang_metrics))

if __name__ == "__main__":
    main()