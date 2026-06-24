import streamlit as st
import pandas as pd
import plotly.express as px

from utils.detector import detect_subscriptions
from utils.manual_entry import add_manual_expense
from utils.reminders import get_renewal_reminders
from utils.ai_helper import get_ai_suggestions

st.set_page_config(
    page_title="Subscription Waste Detector",
    page_icon="💳",
    layout="wide"
)

st.markdown("""
<div style="
padding:25px;
border-radius:15px;
background:linear-gradient(135deg,#0f172a,#1e293b);
color:white;
text-align:center;
margin-bottom:20px;
">
<h1>💳 Subscription Waste Detector</h1>
<p>AI-Powered Subscription Tracking & Cost Optimization</p>
</div>
""", unsafe_allow_html=True)

if "expense_df" not in st.session_state:
    st.session_state.expense_df = None

if "ai_response" not in st.session_state:
    st.session_state.ai_response = ""

st.sidebar.header("➕ Manual Expense Entry")

description = st.sidebar.text_input("Description")

amount = st.sidebar.number_input(
    "Amount",
    min_value=0.0,
    step=1.0
)

category = st.sidebar.selectbox(
    "Category",
    [
        "Entertainment",
        "Software",
        "Productivity",
        "Music",
        "Video",
        "Education",
        "Gaming",
        "Other"
    ]
)

renewal_date = st.sidebar.date_input(
    "Renewal Date"
)

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        st.session_state.expense_df = pd.read_csv(
            uploaded_file
        )
    else:
        st.session_state.expense_df = pd.read_excel(
            uploaded_file
        )

if st.sidebar.button("Add Expense"):

    if (
        st.session_state.expense_df is not None
        and description
        and amount > 0
    ):

        st.session_state.expense_df = add_manual_expense(
            st.session_state.expense_df,
            description,
            amount,
            category,
            str(renewal_date)
        )

        st.sidebar.success(
            "Expense Added Successfully"
        )

if st.session_state.expense_df is not None:

    df = st.session_state.expense_df

    with st.expander(
        "📄 View Raw Expense Data",
        expanded=False
    ):
        st.dataframe(df, width="stretch")

    reminders = get_renewal_reminders(df)

    if reminders:

        st.subheader("⚠ Upcoming Renewals")

        for reminder in reminders:
            st.warning(reminder)

        st.divider()

    subscriptions = detect_subscriptions(df)

    if subscriptions.empty:

        st.warning(
            "No subscriptions detected yet."
        )

    else:

        total_spending = subscriptions[
            "Monthly Cost"
        ].sum()

        active_subscriptions = len(
            subscriptions
        )

        possible_savings = round(
            total_spending * 0.20
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "💰 Total Monthly Spending",
            f"₹{total_spending:,.0f}"
        )

        c2.metric(
            "📦 Active Subscriptions",
            active_subscriptions
        )

        c3.metric(
            "💡 Possible Savings",
            f"₹{possible_savings:,.0f}"
        )

        st.divider()

        left, right = st.columns(2)

        with left:

            st.subheader(
                "📊 Spending Distribution"
            )

            fig = px.pie(
                subscriptions,
                values="Monthly Cost",
                names="Subscription",
                hole=0.55
            )

            st.plotly_chart(fig, width="stretch")

        with right:

            st.subheader(
                "💳 Subscription Cards"
            )

            for _, row in subscriptions.iterrows():

                cost = row["Monthly Cost"]

                if cost < 500:
                    st.success(
                        f"🟢 {row['Subscription']} — ₹{cost}"
                    )

                elif cost <= 1000:
                    st.warning(
                        f"🟠 {row['Subscription']} — ₹{cost}"
                    )

                else:
                    st.error(
                        f"🔴 {row['Subscription']} — ₹{cost}"
                    )

        st.divider()

        st.subheader(
            "📋 Detected Subscriptions"
        )

        st.dataframe(
            subscriptions,
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "🤖 AI Cost-Saving Suggestions"
        )

        if st.button(
            "Get AI Suggestions"
        ):

            try:

                with st.spinner(
                    "Analyzing subscriptions..."
                ):

                    api_key = st.secrets[
                        "GROQ_API_KEY"
                    ]

                    st.session_state.ai_response = (
                        get_ai_suggestions(
                            subscriptions,
                            api_key
                        )
                    )

                st.success(
                    "Analysis Complete"
                )

            except Exception as e:

                st.error(
                    f"AI Error: {e}"
                )

        if st.session_state.ai_response:

            st.markdown(
                st.session_state.ai_response
            )

        report = f"""
Subscription Waste Detector Report

Total Monthly Spending: ₹{total_spending}

Active Subscriptions: {active_subscriptions}

Detected Subscriptions:
"""

        for _, row in subscriptions.iterrows():

            report += (
                f"\n{row['Subscription']} - ₹{row['Monthly Cost']}"
            )

        if st.session_state.ai_response:

            report += (
                f"\n\nAI Analysis:\n"
                f"{st.session_state.ai_response}"
            )

        st.download_button(
            "📥 Download Report",
            data=report,
            file_name="subscription_report.txt",
            mime="text/plain"
        )