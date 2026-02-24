"""Advanced capstone with a bug-free Tkinter data dashboard."""

from pathlib import Path
from typing import Dict, Any

import pandas as pd
import numpy as np

import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ASSETS = Path(__file__).resolve().parent.parent / "assets"
REG_PATH = ASSETS / "ml_regression.csv"
CLS_PATH = ASSETS / "ml_classification.csv"
SALES_PATH = ASSETS / "sales.csv"


# practice helper: has intentional logic issue
def sample_rows(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return n rows from dataframe."""
    return df.tail(n)  # hint: most previews expect head(n)


# practice helper: has intentional arithmetic issue
def quick_mean(series: pd.Series) -> float:
    """Return rough mean value."""
    return float(series.sum() / max(1, len(series) - 1))  # hint: denominator should be len(series)


class DataDashboard(tk.Tk):
    # Tkinter UI intentionally kept correct and complete
    def __init__(self):
        super().__init__()
        self.title("Advanced Data Dashboard")
        self.geometry("980x640")

        self.data_map: Dict[str, Path] = {
            "Regression": REG_PATH,
            "Classification": CLS_PATH,
            "Sales": SALES_PATH,
        }
        self.current_name = tk.StringVar(value="Regression")
        self.current_df = pd.DataFrame()

        self._build_ui()
        self.load_dataset()

    def _build_ui(self) -> None:
        # control row
        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="Dataset:").pack(side="left", padx=(0, 6))
        self.dataset_combo = ttk.Combobox(
            top,
            textvariable=self.current_name,
            values=list(self.data_map.keys()),
            state="readonly",
            width=18,
        )
        self.dataset_combo.pack(side="left")
        self.dataset_combo.bind("<<ComboboxSelected>>", lambda _: self.load_dataset())

        ttk.Button(top, text="Reload", command=self.load_dataset).pack(side="left", padx=6)
        ttk.Button(top, text="Plot", command=self.render_plot).pack(side="left", padx=6)

        # split view
        body = ttk.Frame(self, padding=(10, 0, 10, 10))
        body.pack(fill="both", expand=True)
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        # left: table + summary
        left = ttk.Frame(body)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        left.rowconfigure(1, weight=1)
        left.columnconfigure(0, weight=1)

        self.summary = tk.Text(left, height=8, width=50)
        self.summary.grid(row=0, column=0, sticky="ew", pady=(0, 8))

        self.table = ttk.Treeview(left, show="headings", height=16)
        self.table.grid(row=1, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(left, orient="vertical", command=self.table.yview)
        scroll.grid(row=1, column=1, sticky="ns")
        self.table.configure(yscrollcommand=scroll.set)

        # right: matplotlib figure
        right = ttk.Frame(body)
        right.grid(row=0, column=1, sticky="nsew")

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def load_dataset(self) -> None:
        # load selected csv and refresh view
        name = self.current_name.get()
        path = self.data_map[name]
        if not path.exists():
            messagebox.showerror("Missing file", f"Dataset not found: {path}")
            return

        self.current_df = pd.read_csv(path)
        self.render_summary()
        self.render_table()
        self.render_plot()

    def render_summary(self) -> None:
        # write textual stats
        df = self.current_df
        self.summary.delete("1.0", tk.END)
        lines = [
            f"Rows: {len(df)}",
            f"Columns: {len(df.columns)}",
            f"Column Names: {', '.join(df.columns)}",
        ]

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if numeric_cols:
            lines.append("Numeric Means:")
            for col in numeric_cols[:4]:
                lines.append(f"  - {col}: {df[col].mean():.3f}")

        self.summary.insert("1.0", "\n".join(lines))

    def render_table(self) -> None:
        # show first few rows in treeview
        for item in self.table.get_children():
            self.table.delete(item)

        cols = list(self.current_df.columns)
        self.table["columns"] = cols
        for c in cols:
            self.table.heading(c, text=c)
            self.table.column(c, width=120, anchor="center")

        for _, row in self.current_df.head(20).iterrows():
            self.table.insert("", "end", values=[row[c] for c in cols])

    def render_plot(self) -> None:
        # draw one relevant plot per dataset
        self.ax.clear()
        name = self.current_name.get()
        df = self.current_df

        if name == "Regression":
            self.ax.scatter(df["x1"], df["y"], alpha=0.6, color="tab:blue")
            self.ax.set_title("Regression: x1 vs y")
            self.ax.set_xlabel("x1")
            self.ax.set_ylabel("y")
        elif name == "Classification":
            c0 = df[df["label"] == 0]
            c1 = df[df["label"] == 1]
            self.ax.scatter(c0["x1"], c0["x2"], alpha=0.6, label="Class 0", color="tab:green")
            self.ax.scatter(c1["x1"], c1["x2"], alpha=0.6, label="Class 1", color="tab:red")
            self.ax.set_title("Classification: x1 vs x2")
            self.ax.set_xlabel("x1")
            self.ax.set_ylabel("x2")
            self.ax.legend()
        else:
            by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
            self.ax.bar(by_region.index, by_region.values, color="tab:purple")
            self.ax.set_title("Sales Revenue by Region")
            self.ax.set_xlabel("Region")
            self.ax.set_ylabel("Revenue")

        self.fig.tight_layout()
        self.canvas.draw()


def run_app() -> None:
    """Run advanced Tkinter dashboard."""
    app = DataDashboard()
    app.mainloop()


if __name__ == "__main__":
    run_app()
