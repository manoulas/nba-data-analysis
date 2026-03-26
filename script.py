import pandas as pd
import csv

data = {
    "game_id": [],
    "vs": [],
    "q1_1": [],
    "q1_2": [],
    "q2_1": [],
    "q2_2": [],
    "q3_1": [],
    "q3_2": [],
    "q4_1": [],
    "q4_2": [],
    "q1_2-q1_1": [],
    "q2_1-q1_2": [],
    "q2_2-q2_1": [],
    "q3_1-q3_2": [],
    "q3_2-q3_1": [],
    "q4_2-q4_1": [],
}


def main():
    def score_diff(score_text):
        if not score_text or "-" not in score_text:
            return 0
        parts = score_text.split("-")
        if len(parts) != 2 or (not parts[0].isdigit()) or (not parts[1].isdigit()):
            return 0
        return int(parts[0]) - int(parts[1])

    games = {}
    with open("data/data.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            game_id = row.get("game_id", "")
            team = row.get("team", "")
            if game_id not in games:
                games[game_id] = {
                    "home": game_id[-3:],
                    "away": "",
                    "last_score": None,
                    "q1_1": None,
                    "q1_2": None,
                    "q2_1": None,
                    "q2_2": None,
                    "q3_1": None,
                    "q3_2": None,
                    "q4_1": None,
                    "q4_2": None,
                }

            # adjust teams
            if team != games[game_id]["home"]:
                games[game_id]["away"] = team

            score = row.get("Score", "")
            time = row.get("Time", "")
            event = row.get("event", "").lower()

            # end of quarters
            if games[game_id]["q1_2"] is None and "end of 1st quarter" in event:
                if games[game_id]["last_score"] is not None:
                    games[game_id]["q1_2"] = games[game_id]["last_score"]
            if games[game_id]["q2_2"] is None and "end of 2nd quarter" in event:
                if games[game_id]["last_score"] is not None:
                    games[game_id]["q2_2"] = games[game_id]["last_score"]
            if games[game_id]["q3_2"] is None and "end of 3rd quarter" in event:
                if games[game_id]["last_score"] is not None:
                    games[game_id]["q3_2"] = games[game_id]["last_score"]
            if games[game_id]["q4_2"] is None and "end of 4th quarter" in event:
                if games[game_id]["last_score"] is not None:
                    games[game_id]["q4_2"] = games[game_id]["last_score"]

            if "-" in score:
                parts = score.split("-")
                if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    left = int(parts[0])
                    right = int(parts[1])
                    cur_score = f"{left}-{right}"

                    games[game_id]["last_score"] = cur_score

                    is_mid_time = (
                        time.startswith("6:0")
                        or time.startswith("6:1")
                        or time.startswith("6:2")
                        or time.startswith("6:3")
                        or time.startswith("6:4")
                        or time.startswith("5:")
                    )

                    # mid times
                    if games[game_id]["q1_1"] is None and is_mid_time:
                        games[game_id]["q1_1"] = cur_score
                    elif (
                        games[game_id]["q1_2"] is not None
                        and games[game_id]["q2_1"] is None
                        and is_mid_time
                    ):
                        games[game_id]["q2_1"] = cur_score
                    elif (
                        games[game_id]["q2_2"] is not None
                        and games[game_id]["q3_1"] is None
                        and is_mid_time
                    ):
                        games[game_id]["q3_1"] = cur_score
                    elif (
                        games[game_id]["q3_2"] is not None
                        and games[game_id]["q4_1"] is None
                        and is_mid_time
                    ):
                        games[game_id]["q4_1"] = cur_score

    for game_id in games:
        data["game_id"].append(game_id)
        home_team = games[game_id]["home"]
        away_team = games[game_id]["away"]
        data["vs"].append(f"{home_team}-{away_team}")

        for q in ["q1_1", "q1_2", "q2_1", "q2_2", "q3_1", "q3_2", "q4_1", "q4_2"]:
            if games[game_id][q] is None:
                data[q].append("0-0")
            else:
                data[q].append(games[game_id][q])

        dif_q1_2 = score_diff(games[game_id]["q1_2"])
        dif_q2_2 = score_diff(games[game_id]["q2_2"])
        dif_q3_2 = score_diff(games[game_id]["q3_2"])
        dif_q4_2 = score_diff(games[game_id]["q4_2"])
        dif_q1_1 = score_diff(games[game_id]["q1_1"])
        dif_q2_1 = score_diff(games[game_id]["q2_1"])
        dif_q3_1 = score_diff(games[game_id]["q3_1"])
        dif_q4_1 = score_diff(games[game_id]["q4_1"])
        dif_q1_2_q1_1 = dif_q1_2 - dif_q1_1
        dif_q2_1_q1_2 = dif_q2_1 - dif_q1_2
        dif_q2_2_q2_1 = dif_q2_2 - dif_q2_1
        dif_q3_1_q3_2 = dif_q3_1 - dif_q3_2
        dif_q3_2_q3_1 = dif_q3_2 - dif_q3_1
        dif_q4_2_q4_1 = dif_q4_2 - dif_q4_1

        data["q1_2-q1_1"].append(dif_q1_2_q1_1)
        data["q2_1-q1_2"].append(dif_q2_1_q1_2)
        data["q2_2-q2_1"].append(dif_q2_2_q2_1)
        data["q3_1-q3_2"].append(dif_q3_1_q3_2)
        data["q3_2-q3_1"].append(dif_q3_2_q3_1)
        data["q4_2-q4_1"].append(dif_q4_2_q4_1)

    df = pd.DataFrame(data)
    df.to_csv("output.csv", index=False, encoding="utf-8")


if __name__ == "__main__":
    main()
