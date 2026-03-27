import csv
import pandas as pd

# TODO: Descriptive Analysis of the data, including visualizations and insights.
df = pd.DataFrame()


def main():
    means()


def means():
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

        row_len = len(q1_1)
        avg_q1_1 = sum(q1_1) / row_len
        avg_q1_2 = sum(q1_2) / row_len
        avg_q1_3 = sum(q1_3) / row_len
        avg_q2_1 = sum(q2_1) / row_len
        avg_q2_2 = sum(q2_2) / row_len
        avg_q2_3 = sum(q2_3) / row_len
        avg_q3_1 = sum(q3_1) / row_len
        avg_q3_2 = sum(q3_2) / row_len
        avg_q3_3 = sum(q3_3) / row_len
        avg_q4_1 = sum(q4_1) / row_len
        avg_q4_2 = sum(q4_2) / row_len
        avg_q4_3 = sum(q4_3) / row_len

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

        avg_away_q1_1 = sum(away_q1_1) / row_len
        avg_away_q1_2 = sum(away_q1_2) / row_len
        avg_away_q1_3 = sum(away_q1_3) / row_len
        avg_away_q2_1 = sum(away_q2_1) / row_len
        avg_away_q2_2 = sum(away_q2_2) / row_len
        avg_away_q2_3 = sum(away_q2_3) / row_len
        avg_away_q3_1 = sum(away_q3_1) / row_len
        avg_away_q3_2 = sum(away_q3_2) / row_len
        avg_away_q3_3 = sum(away_q3_3) / row_len
        avg_away_q4_1 = sum(away_q4_1) / row_len
        avg_away_q4_2 = sum(away_q4_2) / row_len
        avg_away_q4_3 = sum(away_q4_3) / row_len

        # differences between home and away team scores
        diff_q1_1 = avg_q1_1 - avg_away_q1_1
        diff_q1_2 = avg_q1_2 - avg_away_q1_2
        diff_q1_3 = avg_q1_3 - avg_away_q1_3
        diff_q2_1 = avg_q2_1 - avg_away_q2_1
        diff_q2_2 = avg_q2_2 - avg_away_q2_2
        diff_q2_3 = avg_q2_3 - avg_away_q2_3
        diff_q3_1 = avg_q3_1 - avg_away_q3_1
        diff_q3_2 = avg_q3_2 - avg_away_q3_2
        diff_q3_3 = avg_q3_3 - avg_away_q3_3
        diff_q4_1 = avg_q4_1 - avg_away_q4_1
        diff_q4_2 = avg_q4_2 - avg_away_q4_2
        diff_q4_3 = avg_q4_3 - avg_away_q4_3

        # interval-delta means from dataset columns (home-away deltas)
        delta_q1_2_q1_1_mean = sum(int(row[14]) for row in rows) / row_len
        delta_q1_3_q1_2_mean = sum(int(row[15]) for row in rows) / row_len
        delta_q2_2_q2_1_mean = sum(int(row[16]) for row in rows) / row_len
        delta_q2_3_q2_2_mean = sum(int(row[17]) for row in rows) / row_len
        delta_q3_2_q3_1_mean = sum(int(row[18]) for row in rows) / row_len
        delta_q3_3_q3_2_mean = sum(int(row[19]) for row in rows) / row_len
        delta_q4_2_q4_1_mean = sum(int(row[20]) for row in rows) / row_len
        delta_q4_3_q4_2_mean = sum(int(row[21]) for row in rows) / row_len

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
            "diff_q1_1": diff_q1_1,
            "diff_q1_2": diff_q1_2,
            "diff_q1_3": diff_q1_3,
            "diff_q2_1": diff_q2_1,
            "diff_q2_2": diff_q2_2,
            "diff_q2_3": diff_q2_3,
            "diff_q3_1": diff_q3_1,
            "diff_q3_2": diff_q3_2,
            "diff_q3_3": diff_q3_3,
            "diff_q4_1": diff_q4_1,
            "diff_q4_2": diff_q4_2,
            "diff_q4_3": diff_q4_3,
            "q1_2_delta_q1_1": delta_q1_2_q1_1_mean,
            "q1_3_delta_q1_2": delta_q1_3_q1_2_mean,
            "q2_2_delta_q2_1": delta_q2_2_q2_1_mean,
            "q2_3_delta_q2_2": delta_q2_3_q2_2_mean,
            "q3_2_delta_q3_1": delta_q3_2_q3_1_mean,
            "q3_3_delta_q3_2": delta_q3_3_q3_2_mean,
            "q4_2_delta_q4_1": delta_q4_2_q4_1_mean,
            "q4_3_delta_q4_2": delta_q4_3_q4_2_mean,
        }
        df = pd.DataFrame({"means": means})

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


def medians():
    with open("data/game_scores.csv", "r", encoding="utf-8", newline="") as f:
        rows = csv.reader(f)
        next(rows, None)
        rows = list(rows)


if __name__ == "__main__":
    main()
