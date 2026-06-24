import pandas as pd

def add_manual_expense(
    df,
    description,
    amount,
    category,
    renewal_date
):

    new_row = pd.DataFrame([
        {
            "Date": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "Description": description,
            "Amount": amount,
            "Category": category,
            "RenewalDate": renewal_date
        }
    ])

    return pd.concat(
        [df, new_row],
        ignore_index=True
    )