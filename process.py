import csv
import pandas as pd

df = pd.DataFrame()
cols = {}


def main():
    constr_cols()
    describe_df = pd.DataFrame(cols).describe()
    means()
    medians()
    modes()
    range()
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
        print(describe_df.T.to_string())
        print(df.to_string())


def constr_cols():
    with open("data/game_scores.csv", "r", encoding="utf-8", newline="") as f:
        rows = csv.reader(f)
        next(rows, None)
        rows = list(rows)

        # home team scores
        q1_1 = [int(row[2].split("-")[0]) for row in rows]
        q1_2 = [int(row[3].split("-")[0]) for row in rows]
        q1_3 = [int(row[4].split("-")[0]) for row in rows]
        q2_1 = [int(row[5].split("-")[0]) for row in rows]
        q2_2 = [int(row[6].split("-")[0]) for row in rows]
        q2_3 = [int(row[7].split("-")[0]) for row in rows]
        q3_1 = [int(row[8].split("-")[0]) for row in rows]
        q3_2 = [int(row[9].split("-")[0]) for row in rows]
        q3_3 = [int(row[10].split("-")[0]) for row in rows]
        q4_1 = [int(row[11].split("-")[0]) for row in rows]
        q4_2 = [int(row[12].split("-")[0]) for row in rows]
        q4_3 = [int(row[13].split("-")[0]) for row in rows]

        # away team scores
        away_q1_1 = [int(row[2].split("-")[1]) for row in rows]
        away_q1_2 = [int(row[3].split("-")[1]) for row in rows]
        away_q1_3 = [int(row[4].split("-")[1]) for row in rows]
        away_q2_1 = [int(row[5].split("-")[1]) for row in rows]
        away_q2_2 = [int(row[6].split("-")[1]) for row in rows]
        away_q2_3 = [int(row[7].split("-")[1]) for row in rows]
        away_q3_1 = [int(row[8].split("-")[1]) for row in rows]
        away_q3_2 = [int(row[9].split("-")[1]) for row in rows]
        away_q3_3 = [int(row[10].split("-")[1]) for row in rows]
        away_q4_1 = [int(row[11].split("-")[1]) for row in rows]
        away_q4_2 = [int(row[12].split("-")[1]) for row in rows]
        away_q4_3 = [int(row[13].split("-")[1]) for row in rows]

        # interval deltas
        delta_q1_2_q1_1 = [int(row[14]) for row in rows]
        delta_q1_3_q1_2 = [int(row[15]) for row in rows]
        delta_q2_2_q2_1 = [int(row[16]) for row in rows]
        delta_q2_3_q2_2 = [int(row[17]) for row in rows]
        delta_q3_2_q3_1 = [int(row[18]) for row in rows]
        delta_q3_3_q3_2 = [int(row[19]) for row in rows]
        delta_q4_2_q4_1 = [int(row[20]) for row in rows]
        delta_q4_3_q4_2 = [int(row[21]) for row in rows]

        global cols
        cols = {
            "home_q1_1": q1_1,
            "home_q1_2": q1_2,
            "home_q1_3": q1_3,
            "home_q2_1": q2_1,
            "home_q2_2": q2_2,
            "home_q2_3": q2_3,
            "home_q3_1": q3_1,
            "home_q3_2": q3_2,
            "home_q3_3": q3_3,
            "home_q4_1": q4_1,
            "home_q4_2": q4_2,
            "home_q4_3": q4_3,
            "away_q1_1": away_q1_1,
            "away_q1_2": away_q1_2,
            "away_q1_3": away_q1_3,
            "away_q2_1": away_q2_1,
            "away_q2_2": away_q2_2,
            "away_q2_3": away_q2_3,
            "away_q3_1": away_q3_1,
            "away_q3_2": away_q3_2,
            "away_q3_3": away_q3_3,
            "away_q4_1": away_q4_1,
            "away_q4_2": away_q4_2,
            "away_q4_3": away_q4_3,
            "q1_2_delta_q1_1": delta_q1_2_q1_1,
            "q1_3_delta_q1_2": delta_q1_3_q1_2,
            "q2_2_delta_q2_1": delta_q2_2_q2_1,
            "q2_3_delta_q2_2": delta_q2_3_q2_2,
            "q3_2_delta_q3_1": delta_q3_2_q3_1,
            "q3_3_delta_q3_2": delta_q3_3_q3_2,
            "q4_2_delta_q4_1": delta_q4_2_q4_1,
            "q4_3_delta_q4_2": delta_q4_3_q4_2,
        }


def means():
    # home team means
    avg_q1_1 = pd.Series(cols["home_q1_1"]).mean()
    avg_q1_2 = pd.Series(cols["home_q1_2"]).mean()
    avg_q1_3 = pd.Series(cols["home_q1_3"]).mean()
    avg_q2_1 = pd.Series(cols["home_q2_1"]).mean()
    avg_q2_2 = pd.Series(cols["home_q2_2"]).mean()
    avg_q2_3 = pd.Series(cols["home_q2_3"]).mean()
    avg_q3_1 = pd.Series(cols["home_q3_1"]).mean()
    avg_q3_2 = pd.Series(cols["home_q3_2"]).mean()
    avg_q3_3 = pd.Series(cols["home_q3_3"]).mean()
    avg_q4_1 = pd.Series(cols["home_q4_1"]).mean()
    avg_q4_2 = pd.Series(cols["home_q4_2"]).mean()
    avg_q4_3 = pd.Series(cols["home_q4_3"]).mean()

    # away team means
    avg_away_q1_1 = pd.Series(cols["away_q1_1"]).mean()
    avg_away_q1_2 = pd.Series(cols["away_q1_2"]).mean()
    avg_away_q1_3 = pd.Series(cols["away_q1_3"]).mean()
    avg_away_q2_1 = pd.Series(cols["away_q2_1"]).mean()
    avg_away_q2_2 = pd.Series(cols["away_q2_2"]).mean()
    avg_away_q2_3 = pd.Series(cols["away_q2_3"]).mean()
    avg_away_q3_1 = pd.Series(cols["away_q3_1"]).mean()
    avg_away_q3_2 = pd.Series(cols["away_q3_2"]).mean()
    avg_away_q3_3 = pd.Series(cols["away_q3_3"]).mean()
    avg_away_q4_1 = pd.Series(cols["away_q4_1"]).mean()
    avg_away_q4_2 = pd.Series(cols["away_q4_2"]).mean()
    avg_away_q4_3 = pd.Series(cols["away_q4_3"]).mean()

    # interval delta means
    delta_q1_2_q1_1_mean = pd.Series(cols["q1_2_delta_q1_1"]).mean()
    delta_q1_3_q1_2_mean = pd.Series(cols["q1_3_delta_q1_2"]).mean()
    delta_q2_2_q2_1_mean = pd.Series(cols["q2_2_delta_q2_1"]).mean()
    delta_q2_3_q2_2_mean = pd.Series(cols["q2_3_delta_q2_2"]).mean()
    delta_q3_2_q3_1_mean = pd.Series(cols["q3_2_delta_q3_1"]).mean()
    delta_q3_3_q3_2_mean = pd.Series(cols["q3_3_delta_q3_2"]).mean()
    delta_q4_2_q4_1_mean = pd.Series(cols["q4_2_delta_q4_1"]).mean()
    delta_q4_3_q4_2_mean = pd.Series(cols["q4_3_delta_q4_2"]).mean()

    means = {
        "home_q1_1": avg_q1_1,
        "home_q1_2": avg_q1_2,
        "home_q1_3": avg_q1_3,
        "home_q2_1": avg_q2_1,
        "home_q2_2": avg_q2_2,
        "home_q2_3": avg_q2_3,
        "home_q3_1": avg_q3_1,
        "home_q3_2": avg_q3_2,
        "home_q3_3": avg_q3_3,
        "home_q4_1": avg_q4_1,
        "home_q4_2": avg_q4_2,
        "home_q4_3": avg_q4_3,
        "away_q1_1": avg_away_q1_1,
        "away_q1_2": avg_away_q1_2,
        "away_q1_3": avg_away_q1_3,
        "away_q2_1": avg_away_q2_1,
        "away_q2_2": avg_away_q2_2,
        "away_q2_3": avg_away_q2_3,
        "away_q3_1": avg_away_q3_1,
        "away_q3_2": avg_away_q3_2,
        "away_q3_3": avg_away_q3_3,
        "away_q4_1": avg_away_q4_1,
        "away_q4_2": avg_away_q4_2,
        "away_q4_3": avg_away_q4_3,
        "q1_2_delta_q1_1": delta_q1_2_q1_1_mean,
        "q1_3_delta_q1_2": delta_q1_3_q1_2_mean,
        "q2_2_delta_q2_1": delta_q2_2_q2_1_mean,
        "q2_3_delta_q2_2": delta_q2_3_q2_2_mean,
        "q3_2_delta_q3_1": delta_q3_2_q3_1_mean,
        "q3_3_delta_q3_2": delta_q3_3_q3_2_mean,
        "q4_2_delta_q4_1": delta_q4_2_q4_1_mean,
        "q4_3_delta_q4_2": delta_q4_3_q4_2_mean,
    }

    global df
    df = pd.DataFrame({"mean": means})


def medians():
    # home team medians
    q1_1_median = pd.Series(cols["home_q1_1"]).median()
    q1_2_median = pd.Series(cols["home_q1_2"]).median()
    q1_3_median = pd.Series(cols["home_q1_3"]).median()
    q2_1_median = pd.Series(cols["home_q2_1"]).median()
    q2_2_median = pd.Series(cols["home_q2_2"]).median()
    q2_3_median = pd.Series(cols["home_q2_3"]).median()
    q3_1_median = pd.Series(cols["home_q3_1"]).median()
    q3_2_median = pd.Series(cols["home_q3_2"]).median()
    q3_3_median = pd.Series(cols["home_q3_3"]).median()
    q4_1_median = pd.Series(cols["home_q4_1"]).median()
    q4_2_median = pd.Series(cols["home_q4_2"]).median()
    q4_3_median = pd.Series(cols["home_q4_3"]).median()

    # away team medians
    away_q1_1_median = pd.Series(cols["away_q1_1"]).median()
    away_q1_2_median = pd.Series(cols["away_q1_2"]).median()
    away_q1_3_median = pd.Series(cols["away_q1_3"]).median()
    away_q2_1_median = pd.Series(cols["away_q2_1"]).median()
    away_q2_2_median = pd.Series(cols["away_q2_2"]).median()
    away_q2_3_median = pd.Series(cols["away_q2_3"]).median()
    away_q3_1_median = pd.Series(cols["away_q3_1"]).median()
    away_q3_2_median = pd.Series(cols["away_q3_2"]).median()
    away_q3_3_median = pd.Series(cols["away_q3_3"]).median()
    away_q4_1_median = pd.Series(cols["away_q4_1"]).median()
    away_q4_2_median = pd.Series(cols["away_q4_2"]).median()
    away_q4_3_median = pd.Series(cols["away_q4_3"]).median()

    # interval delta medians
    delta_q1_2_q1_1_median = pd.Series(cols["q1_2_delta_q1_1"]).median()
    delta_q1_3_q1_2_median = pd.Series(cols["q1_3_delta_q1_2"]).median()
    delta_q2_2_q2_1_median = pd.Series(cols["q2_2_delta_q2_1"]).median()
    delta_q2_3_q2_2_median = pd.Series(cols["q2_3_delta_q2_2"]).median()
    delta_q3_2_q3_1_median = pd.Series(cols["q3_2_delta_q3_1"]).median()
    delta_q3_3_q3_2_median = pd.Series(cols["q3_3_delta_q3_2"]).median()
    delta_q4_2_q4_1_median = pd.Series(cols["q4_2_delta_q4_1"]).median()
    delta_q4_3_q4_2_median = pd.Series(cols["q4_3_delta_q4_2"]).median()

    medians = {
        "home_q1_1": q1_1_median,
        "home_q1_2": q1_2_median,
        "home_q1_3": q1_3_median,
        "home_q2_1": q2_1_median,
        "home_q2_2": q2_2_median,
        "home_q2_3": q2_3_median,
        "home_q3_1": q3_1_median,
        "home_q3_2": q3_2_median,
        "home_q3_3": q3_3_median,
        "home_q4_1": q4_1_median,
        "home_q4_2": q4_2_median,
        "home_q4_3": q4_3_median,
        "away_q1_1": away_q1_1_median,
        "away_q1_2": away_q1_2_median,
        "away_q1_3": away_q1_3_median,
        "away_q2_1": away_q2_1_median,
        "away_q2_2": away_q2_2_median,
        "away_q2_3": away_q2_3_median,
        "away_q3_1": away_q3_1_median,
        "away_q3_2": away_q3_2_median,
        "away_q3_3": away_q3_3_median,
        "away_q4_1": away_q4_1_median,
        "away_q4_2": away_q4_2_median,
        "away_q4_3": away_q4_3_median,
        "q1_2_delta_q1_1": delta_q1_2_q1_1_median,
        "q1_3_delta_q1_2": delta_q1_3_q1_2_median,
        "q2_2_delta_q2_1": delta_q2_2_q2_1_median,
        "q2_3_delta_q2_2": delta_q2_3_q2_2_median,
        "q3_2_delta_q3_1": delta_q3_2_q3_1_median,
        "q3_3_delta_q3_2": delta_q3_3_q3_2_median,
        "q4_2_delta_q4_1": delta_q4_2_q4_1_median,
        "q4_3_delta_q4_2": delta_q4_3_q4_2_median,
    }
    median_df = pd.DataFrame({"median": medians})
    global df
    df = pd.concat([df, median_df], axis=1)


def modes():
    # home team modes
    q1_1_mode = pd.Series(cols["home_q1_1"]).mode()[0]
    q1_2_mode = pd.Series(cols["home_q1_2"]).mode()[0]
    q1_3_mode = pd.Series(cols["home_q1_3"]).mode()[0]
    q2_1_mode = pd.Series(cols["home_q2_1"]).mode()[0]
    q2_2_mode = pd.Series(cols["home_q2_2"]).mode()[0]
    q2_3_mode = pd.Series(cols["home_q2_3"]).mode()[0]
    q3_1_mode = pd.Series(cols["home_q3_1"]).mode()[0]
    q3_2_mode = pd.Series(cols["home_q3_2"]).mode()[0]
    q3_3_mode = pd.Series(cols["home_q3_3"]).mode()[0]
    q4_1_mode = pd.Series(cols["home_q4_1"]).mode()[0]
    q4_2_mode = pd.Series(cols["home_q4_2"]).mode()[0]
    q4_3_mode = pd.Series(cols["home_q4_3"]).mode()[0]

    # away team modes
    away_q1_1_mode = pd.Series(cols["away_q1_1"]).mode()[0]
    away_q1_2_mode = pd.Series(cols["away_q1_2"]).mode()[0]
    away_q1_3_mode = pd.Series(cols["away_q1_3"]).mode()[0]
    away_q2_1_mode = pd.Series(cols["away_q2_1"]).mode()[0]
    away_q2_2_mode = pd.Series(cols["away_q2_2"]).mode()[0]
    away_q2_3_mode = pd.Series(cols["away_q2_3"]).mode()[0]
    away_q3_1_mode = pd.Series(cols["away_q3_1"]).mode()[0]
    away_q3_2_mode = pd.Series(cols["away_q3_2"]).mode()[0]
    away_q3_3_mode = pd.Series(cols["away_q3_3"]).mode()[0]
    away_q4_1_mode = pd.Series(cols["away_q4_1"]).mode()[0]
    away_q4_2_mode = pd.Series(cols["away_q4_2"]).mode()[0]
    away_q4_3_mode = pd.Series(cols["away_q4_3"]).mode()[0]

    # interval delta modes
    delta_q1_2_q1_1_mode = pd.Series(cols["q1_2_delta_q1_1"]).mode()[0]
    delta_q1_3_q1_2_mode = pd.Series(cols["q1_3_delta_q1_2"]).mode()[0]
    delta_q2_2_q2_1_mode = pd.Series(cols["q2_2_delta_q2_1"]).mode()[0]
    delta_q2_3_q2_2_mode = pd.Series(cols["q2_3_delta_q2_2"]).mode()[0]
    delta_q3_2_q3_1_mode = pd.Series(cols["q3_2_delta_q3_1"]).mode()[0]
    delta_q3_3_q3_2_mode = pd.Series(cols["q3_3_delta_q3_2"]).mode()[0]
    delta_q4_2_q4_1_mode = pd.Series(cols["q4_2_delta_q4_1"]).mode()[0]
    delta_q4_3_q4_2_mode = pd.Series(cols["q4_3_delta_q4_2"]).mode()[0]

    modes = {
        "home_q1_1": q1_1_mode,
        "home_q1_2": q1_2_mode,
        "home_q1_3": q1_3_mode,
        "home_q2_1": q2_1_mode,
        "home_q2_2": q2_2_mode,
        "home_q2_3": q2_3_mode,
        "home_q3_1": q3_1_mode,
        "home_q3_2": q3_2_mode,
        "home_q3_3": q3_3_mode,
        "home_q4_1": q4_1_mode,
        "home_q4_2": q4_2_mode,
        "home_q4_3": q4_3_mode,
        "away_q1_1": away_q1_1_mode,
        "away_q1_2": away_q1_2_mode,
        "away_q1_3": away_q1_3_mode,
        "away_q2_1": away_q2_1_mode,
        "away_q2_2": away_q2_2_mode,
        "away_q2_3": away_q2_3_mode,
        "away_q3_1": away_q3_1_mode,
        "away_q3_2": away_q3_2_mode,
        "away_q3_3": away_q3_3_mode,
        "away_q4_1": away_q4_1_mode,
        "away_q4_2": away_q4_2_mode,
        "away_q4_3": away_q4_3_mode,
        "q1_2_delta_q1_1": delta_q1_2_q1_1_mode,
        "q1_3_delta_q1_2": delta_q1_3_q1_2_mode,
        "q2_2_delta_q2_1": delta_q2_2_q2_1_mode,
        "q2_3_delta_q2_2": delta_q2_3_q2_2_mode,
        "q3_2_delta_q3_1": delta_q3_2_q3_1_mode,
        "q3_3_delta_q3_2": delta_q3_3_q3_2_mode,
        "q4_2_delta_q4_1": delta_q4_2_q4_1_mode,
        "q4_3_delta_q4_2": delta_q4_3_q4_2_mode,
    }
    mode_df = pd.DataFrame({"mode": modes})
    global df
    df = pd.concat([df, mode_df], axis=1)


def std():
    # home team std
    q1_1_std = pd.Series(cols["home_q1_1"]).std()
    q1_2_std = pd.Series(cols["home_q1_2"]).std()
    q1_3_std = pd.Series(cols["home_q1_3"]).std()
    q2_1_std = pd.Series(cols["home_q2_1"]).std()
    q2_2_std = pd.Series(cols["home_q2_2"]).std()
    q2_3_std = pd.Series(cols["home_q2_3"]).std()
    q3_1_std = pd.Series(cols["home_q3_1"]).std()
    q3_2_std = pd.Series(cols["home_q3_2"]).std()
    q3_3_std = pd.Series(cols["home_q3_3"]).std()
    q4_1_std = pd.Series(cols["home_q4_1"]).std()
    q4_2_std = pd.Series(cols["home_q4_2"]).std()
    q4_3_std = pd.Series(cols["home_q4_3"]).std()

    # away team std
    away_q1_1_std = pd.Series(cols["away_q1_1"]).std()
    away_q1_2_std = pd.Series(cols["away_q1_2"]).std()
    away_q1_3_std = pd.Series(cols["away_q1_3"]).std()
    away_q2_1_std = pd.Series(cols["away_q2_1"]).std()
    away_q2_2_std = pd.Series(cols["away_q2_2"]).std()
    away_q2_3_std = pd.Series(cols["away_q2_3"]).std()
    away_q3_1_std = pd.Series(cols["away_q3_1"]).std()
    away_q3_2_std = pd.Series(cols["away_q3_2"]).std()
    away_q3_3_std = pd.Series(cols["away_q3_3"]).std()
    away_q4_1_std = pd.Series(cols["away_q4_1"]).std()
    away_q4_2_std = pd.Series(cols["away_q4_2"]).std()
    away_q4_3_std = pd.Series(cols["away_q4_3"]).std()

    # interval delta std
    delta_q1_2_q1_1_std = pd.Series(cols["q1_2_delta_q1_1"]).std()
    delta_q1_3_q1_2_std = pd.Series(cols["q1_3_delta_q1_2"]).std()
    delta_q2_2_q2_1_std = pd.Series(cols["q2_2_delta_q2_1"]).std()
    delta_q2_3_q2_2_std = pd.Series(cols["q2_3_delta_q2_2"]).std()
    delta_q3_2_q3_1_std = pd.Series(cols["q3_2_delta_q3_1"]).std()
    delta_q3_3_q3_2_std = pd.Series(cols["q3_3_delta_q3_2"]).std()
    delta_q4_2_q4_1_std = pd.Series(cols["q4_2_delta_q4_1"]).std()
    delta_q4_3_q4_2_std = pd.Series(cols["q4_3_delta_q4_2"]).std()
    stds = {
        "home_q1_1": q1_1_std,
        "home_q1_2": q1_2_std,
        "home_q1_3": q1_3_std,
        "home_q2_1": q2_1_std,
        "home_q2_2": q2_2_std,
        "home_q2_3": q2_3_std,
        "home_q3_1": q3_1_std,
        "home_q3_2": q3_2_std,
        "home_q3_3": q3_3_std,
        "home_q4_1": q4_1_std,
        "home_q4_2": q4_2_std,
        "home_q4_3": q4_3_std,
        "away_q1_1": away_q1_1_std,
        "away_q1_2": away_q1_2_std,
        "away_q1_3": away_q1_3_std,
        "away_q2_1": away_q2_1_std,
        "away_q2_2": away_q2_2_std,
        "away_q2_3": away_q2_3_std,
        "away_q3_1": away_q3_1_std,
        "away_q3_2": away_q3_2_std,
        "away_q3_3": away_q3_3_std,
        "away_q4_1": away_q4_1_std,
        "away_q4_2": away_q4_2_std,
        "away_q4_3": away_q4_3_std,
        "q1_2_delta_q1_1": delta_q1_2_q1_1_std,
        "q1_3_delta_q1_2": delta_q1_3_q1_2_std,
        "q2_2_delta_q2_1": delta_q2_2_q2_1_std,
        "q2_3_delta_q2_2": delta_q2_3_q2_2_std,
        "q3_2_delta_q3_1": delta_q3_2_q3_1_std,
        "q3_3_delta_q3_2": delta_q3_3_q3_2_std,
        "q4_2_delta_q4_1": delta_q4_2_q4_1_std,
        "q4_3_delta_q4_2": delta_q4_3_q4_2_std,
    }

    std_df = pd.DataFrame({"std": stds})
    global df
    df = pd.concat([df, std_df], axis=1)


def variance():
    # home team variance
    q1_1_var = pd.Series(cols["home_q1_1"]).var()
    q1_2_var = pd.Series(cols["home_q1_2"]).var()
    q1_3_var = pd.Series(cols["home_q1_3"]).var()
    q2_1_var = pd.Series(cols["home_q2_1"]).var()
    q2_2_var = pd.Series(cols["home_q2_2"]).var()
    q2_3_var = pd.Series(cols["home_q2_3"]).var()
    q3_1_var = pd.Series(cols["home_q3_1"]).var()
    q3_2_var = pd.Series(cols["home_q3_2"]).var()
    q3_3_var = pd.Series(cols["home_q3_3"]).var()
    q4_1_var = pd.Series(cols["home_q4_1"]).var()
    q4_2_var = pd.Series(cols["home_q4_2"]).var()
    q4_3_var = pd.Series(cols["home_q4_3"]).var()

    # away team variance
    away_q1_1_var = pd.Series(cols["away_q1_1"]).var()
    away_q1_2_var = pd.Series(cols["away_q1_2"]).var()
    away_q1_3_var = pd.Series(cols["away_q1_3"]).var()
    away_q2_1_var = pd.Series(cols["away_q2_1"]).var()
    away_q2_2_var = pd.Series(cols["away_q2_2"]).var()
    away_q2_3_var = pd.Series(cols["away_q2_3"]).var()
    away_q3_1_var = pd.Series(cols["away_q3_1"]).var()
    away_q3_2_var = pd.Series(cols["away_q3_2"]).var()
    away_q3_3_var = pd.Series(cols["away_q3_3"]).var()
    away_q4_1_var = pd.Series(cols["away_q4_1"]).var()
    away_q4_2_var = pd.Series(cols["away_q4_2"]).var()
    away_q4_3_var = pd.Series(cols["away_q4_3"]).var()

    # interval delta variance
    delta_q1_2_q1_1_var = pd.Series(cols["q1_2_delta_q1_1"]).var()
    delta_q1_3_q1_2_var = pd.Series(cols["q1_3_delta_q1_2"]).var()
    delta_q2_2_q2_1_var = pd.Series(cols["q2_2_delta_q2_1"]).var()
    delta_q2_3_q2_2_var = pd.Series(cols["q2_3_delta_q2_2"]).var()
    delta_q3_2_q3_1_var = pd.Series(cols["q3_2_delta_q3_1"]).var()
    delta_q3_3_q3_2_var = pd.Series(cols["q3_3_delta_q3_2"]).var()
    delta_q4_2_q4_1_var = pd.Series(cols["q4_2_delta_q4_1"]).var()
    delta_q4_3_q4_2_var = pd.Series(cols["q4_3_delta_q4_2"]).var()

    variances = {
        "home_q1_1": q1_1_var,
        "home_q1_2": q1_2_var,
        "home_q1_3": q1_3_var,
        "home_q2_1": q2_1_var,
        "home_q2_2": q2_2_var,
        "home_q2_3": q2_3_var,
        "home_q3_1": q3_1_var,
        "home_q3_2": q3_2_var,
        "home_q3_3": q3_3_var,
        "home_q4_1": q4_1_var,
        "home_q4_2": q4_2_var,
        "home_q4_3": q4_3_var,
        "away_q1_1": away_q1_1_var,
        "away_q1_2": away_q1_2_var,
        "away_q1_3": away_q1_3_var,
        "away_q2_1": away_q2_1_var,
        "away_q2_2": away_q2_2_var,
        "away_q2_3": away_q2_3_var,
        "away_q3_1": away_q3_1_var,
        "away_q3_2": away_q3_2_var,
        "away_q3_3": away_q3_3_var,
        "away_q4_1": away_q4_1_var,
        "away_q4_2": away_q4_2_var,
        "away_q4_3": away_q4_3_var,
        "q1_2_delta_q1_1": delta_q1_2_q1_1_var,
        "q1_3_delta_q1_2": delta_q1_3_q1_2_var,
        "q2_2_delta_q2_1": delta_q2_2_q2_1_var,
        "q2_3_delta_q2_2": delta_q2_3_q2_2_var,
        "q3_2_delta_q3_1": delta_q3_2_q3_1_var,
        "q3_3_delta_q3_2": delta_q3_3_q3_2_var,
        "q4_2_delta_q4_1": delta_q4_2_q4_1_var,
        "q4_3_delta_q4_2": delta_q4_3_q4_2_var,
    }
    var_df = pd.DataFrame({"var": variances})
    global df
    df = pd.concat([df, var_df], axis=1)


def range():
    ranges = {}
    for key, values in cols.items():
        series = pd.Series(values)
        ranges[key] = series.max() - series.min()

    range_df = pd.DataFrame({"range": ranges})
    global df
    df = pd.concat([df, range_df], axis=1)


def interquartile():
    iqrs = {}
    for key, values in cols.items():
        series = pd.Series(values)
        iqrs[key] = series.quantile(0.75) - series.quantile(0.25)

    iqr_df = pd.DataFrame({"iqr": iqrs})
    global df
    df = pd.concat([df, iqr_df], axis=1)


def percentile():
    p90 = {}
    for key, values in cols.items():
        series = pd.Series(values)
        p90[key] = series.quantile(0.90)

    percentile_df = pd.DataFrame({"p90": p90})
    global df
    df = pd.concat([df, percentile_df], axis=1)


def coefficient_variation():
    cv = {}
    for key, values in cols.items():
        series = pd.Series(values)
        mean_value = series.mean()
        std_value = series.std()
        cv[key] = std_value / mean_value if mean_value != 0 else pd.NA

    cv_df = pd.DataFrame({"cv": cv})
    global df
    df = pd.concat([df, cv_df], axis=1)


def skewness():
    skews = {}
    for key, values in cols.items():
        series = pd.Series(values)
        skews[key] = series.skew()

    skew_df = pd.DataFrame({"skew": skews})
    global df
    df = pd.concat([df, skew_df], axis=1)


if __name__ == "__main__":
    main()
