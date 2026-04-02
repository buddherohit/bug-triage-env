# reward.py

def calculate_reward(expected, predicted):

    if predicted.lower() == expected.lower():
        return 1.0

    elif expected.lower() in predicted.lower():
        return 0.5

    elif len(predicted) > 0:
        return 0.2

    else:
        return -0.2