from datetime import datetime

def get_renewal_reminders(df):

    reminders = []

    if "RenewalDate" not in df.columns:
        return reminders

    unique_subscriptions = df.drop_duplicates(
        subset=["Description"]
    )

    today = datetime.today().date()

    for _, row in unique_subscriptions.iterrows():

        renewal_date = row.get("RenewalDate")

        if not renewal_date:
            continue

        try:

            renewal_date = datetime.strptime(
                str(renewal_date),
                "%Y-%m-%d"
            ).date()

            days_left = (
                renewal_date - today
            ).days

            if 0 <= days_left <= 7:

                reminders.append(
                    f"{row['Description']} renews in {days_left} day(s) on {renewal_date}"
                )

        except Exception:
            pass

    return reminders