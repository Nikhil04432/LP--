'''

'''
'''
Implement any one of the following Expert System 
I. Information management
II. Hospitals and medical facilities
III. Help desks management
IV. Employee performance evaluation
V. Stock market trading
VI. Airline scheduling and cargo schedules
'''
class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.rules = {}

    def add_fact(self, fact, value):
        self.facts[fact] = value

    def add_rule(self, diagnosis, conditions):
        self.rules[diagnosis] = conditions

    def infer(self):
        for diagnosis, conditions in self.rules.items():
            if all(self.facts.get(fact) == value for fact, value in conditions.items()):
                return diagnosis
        return "No matching diagnosis found"

# Example usage
expert = ExpertSystem()

# Step 1: Add patient symptoms (facts)
expert.add_fact("fever", True)
expert.add_fact("cough", True)
expert.add_fact("body_ache", True)
expert.add_fact("rash", False)

# Step 2: Add medical rules
expert.add_rule("Flu", {"fever": True, "cough": True, "body_ache": True})
expert.add_rule("Measles", {"fever": True, "rash": True})
expert.add_rule("Common Cold", {"cough": True, "fever": False})

# Step 3: Inference (diagnosis)
diagnosis = expert.infer()
print("Diagnosis:", diagnosis)

