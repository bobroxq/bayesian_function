def bayes(A, B, prob_B, prob_AifB, prob_AifNotB):
    prob_NotB = 1.0 - prob_B
    prob_A = prob_AifB * prob_B + prob_AifNotB * prob_NotB
    prob_BifA = (prob_AifB * prob_B) / prob_A
    return f'p ({B} | {A}) = {prob_BifA : .2f}'

A = str(input("Outcome A: "))
B = str(input("Outcome B: "))
prob_B = float(input("Probablilty of Outcome B: "))
prob_AifB = float(input("Probability of Outcome A given Outcome B: "))
prob_AifNotB = float(input("Probability of Outcome A given NOT Outcome B: "))

print(bayes(A, B, prob_B, prob_AifB, prob_AifNotB))

def biomarker(p_disease, p_pos_disease, p_pos_no_disease):
    p_no_disease = 1.0 - p_disease
    p_pos = p_pos_disease * p_disease + p_pos_no_disease * p_no_disease
    return (p_pos_disease * p_disease) / p_pos