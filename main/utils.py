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


def closest(lst, K):
    lst = lst[:-1]
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]