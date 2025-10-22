import pandas as pd

def calculate_priority(df):
    weights = {'impact': 0.3, 'feasibility': 0.2, 'value': 0.3, 'urgency': 0.2}
    df['priority_score'] = (
        df['impact']*weights['impact'] +
        df['feasibility']*weights['feasibility'] +
        df['value']*weights['value'] +
        df['urgency']*weights['urgency']
    )
    return df.sort_values(by='priority_score', ascending=False)
