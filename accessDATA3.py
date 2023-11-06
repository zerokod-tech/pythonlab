import glob
import pandas as pd

base_path = "/Users/roberta/Documents/IOSDEV/PythonLab/PythonTest//bbcsport/"
genres = ["athletics", "cricket", "football", "rugby", "tennis"]


def read_and_split_file(filename):
    with open(filename, 'r', encoding="latin-1") as f:
        lines = f.readlines()  # Get lines as a list of strings lines = list(map(str.strip, lines)) # Remove /n characters lines = list(filter(None, lines)) # Remove empty strings
        return lines


def get_df_from_genre(path, genre):
    files = glob.glob(path + genre + "/*.txt")
    titles = []
    subtitles = []
    bodies = []
    for f in files:
        lines = read_and_split_file(f)
        # First line is the title subtitles.append(lines[1]) # Second line is the subtitle bodies.append(' '.join(lines[2:])) # Combine all the rest
        titles.append(lines[0])
        subtitles.append(lines[1])
        bodies.append(' '.join(lines[2:]))

    return (pd.DataFrame({'genre': genre,
                         'title': titles, 'subtitle': subtitles, 'body': bodies
                          })
            )


final_df = pd.concat([get_df_from_genre(base_path, g) for g in genres])
final_df
