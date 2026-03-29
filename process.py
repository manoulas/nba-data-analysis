import re

import pandas as pd

df = pd.DataFrame()
cols = {}

SCORE_COLUMN_PATTERN = re.compile(r"^q[1-4]_[1-5]$")
DELTA_COLUMN_PATTERN = re.compile(r"^q[1-4]_[2-5]-q[1-4]_[1-4]$")


def main():
    global df, cols
    df = pd.DataFrame()
    cols = {}

    constr_cols()
    means()
    medians()
    modes()
    stat_range()
    interquartile()
    percentile()
    variance()
    std()
    coefficient_variation()
    skewness()

    with pd.option_context(
        "display.max_rows",
        None,
        "display.max_columns",
        None,
        "display.width",
        None,
        "display.max_colwidth",
        None,
    ):
        print(df.to_string())


def parse_score_pair(score_text):
    if not isinstance(score_text, str) or "-" not in score_text:
        return 0, 0
    left, right = score_text.split("-", 1)
    if left.isdigit() and right.isdigit():
        return int(left), int(right)
    return 0, 0


def constr_cols():
    source_df = pd.read_csv("data/game_scores.csv", encoding="utf-8")

    score_columns = [
        column for column in source_df.columns if SCORE_COLUMN_PATTERN.match(column)
    ]
    delta_columns = [
        column for column in source_df.columns if DELTA_COLUMN_PATTERN.match(column)
    ]

    home_cols = {}
    away_cols = {}

    for column in score_columns:
        home_scores = []
        away_scores = []
        for score_text in source_df[column].fillna("0-0").astype(str):
            home_score, away_score = parse_score_pair(score_text)
            home_scores.append(home_score)
            away_scores.append(away_score)
        home_cols[f"home_{column}"] = home_scores
        away_cols[f"away_{column}"] = away_scores

    ordered_cols = {}
    ordered_cols.update(home_cols)
    ordered_cols.update(away_cols)

    for column in delta_columns:
        delta_key = column.replace("-", "_delta_")
        ordered_cols[delta_key] = (
            pd.to_numeric(source_df[column], errors="coerce")
            .fillna(0)
            .astype(int)
            .tolist()
        )

    global cols
    cols = ordered_cols


def append_stat_column(column_name, stat_func):
    stat_values = {key: stat_func(pd.Series(values)) for key, values in cols.items()}
    stat_df = pd.DataFrame({column_name: stat_values})

    global df
    if df.empty:
        df = stat_df
    else:
        df = pd.concat([df, stat_df], axis=1)


def first_mode(series):
    modes = series.mode()
    if modes.empty:
        return pd.NA
    return modes.iloc[0]


def means():
    append_stat_column("mean", pd.Series.mean)


def medians():
    append_stat_column("median", pd.Series.median)


def modes():
    append_stat_column("mode", first_mode)


def std():
    append_stat_column("std", pd.Series.std)


def variance():
    append_stat_column("var", pd.Series.var)


def stat_range():
    append_stat_column("range", lambda series: series.max() - series.min())


def interquartile():
    append_stat_column(
        "iqr", lambda series: series.quantile(0.75) - series.quantile(0.25)
    )


def percentile():
    append_stat_column("p90", lambda series: series.quantile(0.90))


def coefficient_variation():
    def cv_stat(series):
        mean_value = series.mean()
        std_value = series.std()
        return std_value / mean_value if mean_value != 0 else pd.NA

    append_stat_column("cv", cv_stat)


def skewness():
    append_stat_column("skew", pd.Series.skew)


if __name__ == "__main__":
    main()
