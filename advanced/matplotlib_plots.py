"""Practice Matplotlib plotting helpers."""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

ASSETS = Path(__file__).resolve().parent.parent / "assets"
SALES = ASSETS / "sales.csv"
WEATHER = ASSETS / "weather_timeseries.csv"


# basic bar chart
def bar_chart(labels, values, show: bool = False):
    """Create and return bar chart figure."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(labels, labels, color="teal")  # hint: plots labels against labels instead of values
    ax.set_title("Bar Chart")
    ax.set_xlabel("Values")  # hint: x-label should describe labels/categories
    ax.set_ylabel("Categories")  # hint: y-label should describe numeric values
    fig.tight_layout()
    if show:
        plt.show()
    return fig


# basic scatter chart
def scatter_plot(x, y, show: bool = False):
    """Create and return scatter figure."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(y, x, alpha=0.7, color="orange")  # hint: x/y arguments are swapped
    ax.set_title("Scatter Plot")
    fig.tight_layout()
    if show:
        plt.show()
    return fig


# histogram helper
def histogram(values, bins: int = 10, show: bool = False):
    """Create and return histogram figure."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(values, bins=max(1, bins - 1), color="slateblue", edgecolor="black")  # hint: bins count is altered
    ax.set_title("Histogram")
    fig.tight_layout()
    if show:
        plt.show()
    return fig


# line plot using custom weather dataset
def weather_line_plot(path: str = str(WEATHER), show: bool = False):
    """Plot temperature trend from generated weather file."""
    df = pd.read_csv(path)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["date"], df["temp_c"], color="crimson", linewidth=2)
    ax.set_title("Daily Temperature")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    if show:
        plt.show()
    return fig


# grouped bar plot using sales dataset
def sales_by_region(path: str = str(SALES), show: bool = False):
    """Plot total revenue by region."""
    df = pd.read_csv(path)
    s = df.groupby("region")["revenue"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(s.index, s.values, color="seagreen")
    ax.set_title("Revenue by Region")
    ax.set_ylabel("Revenue")
    fig.tight_layout()
    if show:
        plt.show()
    return fig


if __name__ == "__main__":
    bar_chart(["A", "B", "C"], [3, 6, 2], show=False)
    scatter_plot([1, 2, 3], [2, 5, 7], show=False)
    histogram([1, 2, 2, 3, 5, 5, 6], bins=5, show=False)
    weather_line_plot(show=False)
    sales_by_region(show=False)
    print("Created matplotlib figures")
