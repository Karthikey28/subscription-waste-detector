from groq import Groq

def get_ai_suggestions(subscriptions, api_key):

    client = Groq(api_key=api_key)

    subscription_text = ""

    for _, row in subscriptions.iterrows():

        subscription_text += (
            f"{row['Subscription']} - ₹{row['Monthly Cost']}\n"
        )

    prompt = f"""
You are a professional fintech financial advisor.

Analyze these subscriptions:

{subscription_text}

Rules:
- Do not recommend cancelling a subscription unless it represents a significant cost and may provide low value.
- Explain reasoning.
- Focus on optimization before cancellation.
- Consider bundles, annual plans, family plans, and cheaper alternatives.
- Keep recommendations practical.

Return sections:

## Spending Analysis

## Cost Saving Opportunities

## Optimization Suggestions

## Alternative Services

## Estimated Monthly Savings
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content