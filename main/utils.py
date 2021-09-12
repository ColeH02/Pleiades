import pandas as pd

def add_to_database(user, zodiac, ALQ):
    #Get current database
    df = pd.read_csv(r'../resource/pleiadesUserDatabase.csv')
    column_list = ["Name", "Phone", "Insta", "zodiac", "sex", "sexorient", "degree", "sociability", "acqmark"]
    new_df = pd.DataFrame(columns=column_list)
    new_df["Name"] = [user["contact_name"]]
    new_df["Phone"] = [user["phone_number"]]
    new_df["Insta"] = [user["instagram"]]
    new_df["zodiac"] = [zodiac]
    for x in column_list[4:]:
        new_df[x] = [user[x]]
    new_df["ALQ"] = [ALQ]
    df = pd.concat([df, new_df])
    df.to_csv('../resource/pleiadesUserDatabase.csv', index=False)
    return df


def closest(lst, K, df):
    lst = lst[:-1]
    request_sex = df["sexorient"].iloc[-1]
    if request_sex == "exclusively male":
        prefer_sex = "male"
    elif request_sex == "exclusively female":
        prefer_sex = "female"
    else:
        prefer_sex = "both"

    done = False
    if prefer_sex == "both":
        done = True
    while done:
        suggest_index = min(range(len(lst)), key=lambda i: abs(lst[i] - K))
        suggest_sex = df["sex"].iloc[suggest_index]
        if suggest_sex == prefer_sex:
            done = True
        else:
            lst.pop(suggest_sex)
    return lst[suggest_sex]