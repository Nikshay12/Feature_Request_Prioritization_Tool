import matplotlib.pyplot as plt

def plot_priority(df):
    plt.figure(figsize=(8,5))
    plt.barh(df['feature_request'], df['priority_score'], color='skyblue')
    plt.xlabel('Priority Score')
    plt.title('Feature Request Prioritization')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    return plt
