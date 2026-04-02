# grader.py

def grade(expected, predicted):
    
    if expected.lower() == predicted.lower():
        return 1.0
    
    elif expected.lower() in predicted.lower():
        return 0.5
    
    else:
        return 0.0