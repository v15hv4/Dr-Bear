# taking
# positive as 1,
# negative as -1,
# neutral is 0

def remove_non_utf():
    """
    removes non utf-8 characters that can cause issues!
    """
    lines = []
    with open('dataset.csv', 'r', encoding='latin-1') as f:
        # print(f.readlines())
        for line in f:
            lines.append(line.encode("utf-8").decode('utf-8'))

    with open('cleaned_dataset.csv', 'w') as f:
        f.writelines(lines)

    return


def clean_csv():
    """
    taking:
        positive as 1,
        negative as -1,
        neutral as 0
    """
    import pandas as pd

    mapper = {
        'positive': 1,
        'neutral': 0,
        'negative': -1,
    }

    df = pd.read_csv('cleaned_dataset.csv', names=[
                     'sentiment', 'text'], header=None)
    df['sentiment'].replace(to_replace=mapper, inplace=True)
    df.to_csv('final_dataset.csv')


# remove_non_utf()
clean_csv()
