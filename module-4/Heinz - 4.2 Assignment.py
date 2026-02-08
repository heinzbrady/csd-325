"""
Brady Heinz 4.2 Assignment 2/8/2026

Changes made from the original sitka_highs.py:
1) Added a simple text menu (Highs / Lows / Exit) and loop so the user can view multiple graphs.
2) Parsed BOTH TMAX (highs) and TMIN (lows) from the CSV so we can graph either series.
3) Added a lows graph in blue (highs remain red).
4) Added a clean exit option with an exit message (uses sys.exit()).
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

FILENAME = "sitka_weather_2018_simple.csv"

def load_weather_data(filename: str):
    """Load dates, highs (TMAX), and lows (TMIN) from the given CSV."""
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # skip header

        for row in reader:
            # DATE is column index 2, TMAX index 5, TMIN index 6 in this dataset.
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[5])
            low = int(row[6])

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

def plot_series(dates, temps, color, title):
    """Plot a temperature series against dates."""
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()

def main():
    print("Sitka Weather Viewer")
    print("--------------------")
    print("Type one of the following options and press Enter:")
    print("  highs - view daily high temperatures (red)")
    print("  lows  - view daily low temperatures (blue)")
    print("  exit  - quit the program")

    try:
        dates, highs, lows = load_weather_data(FILENAME)
    except FileNotFoundError:
        print(f"ERROR: Could not find '{FILENAME}' in the current folder.")
        print("Make sure the CSV file is in the same directory as this program.")
        sys.exit(1)

    while True:
        choice = input("\nMenu (highs/lows/exit): ").strip().lower()

        if choice == "highs":
            plot_series(dates, highs, "red", "Daily high temperatures - 2018")
        elif choice == "lows":
            plot_series(dates, lows, "blue", "Daily low temperatures - 2018")
        elif choice == "exit":
            print("Thanks for using Sitka Weather Viewer. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please type: highs, lows, or exit.")

if __name__ == "__main__":
    main()
