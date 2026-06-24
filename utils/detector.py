import pandas as pd

def detect_subscriptions(df):

    subscriptions = []

    grouped = df.groupby("Description")

    for name, group in grouped:

        if len(group) >= 3:

            amounts = group["Amount"].unique()

            if len(amounts) == 1:

                subscriptions.append({
                    "Subscription": name,
                    "Monthly Cost": amounts[0],
                    "Occurrences": len(group)
                })

    return pd.DataFrame(subscriptions)