# Write a function that takes a list of dictionaries, where each dictionary represents a person with their name and a list of their test scores. The function should:
# Return the average score for each person.
# Create and return a new list of dictionaries with each dictionary containing the person's name and their highest test score.

def process_scores(people_scores: list) -> tuple:
    average_scores = []
    highest_scores = []
    
    for person in people_scores:
        name = person["name"]
        scores = person["scores"]
        avg_score = sum(scores) / len(scores)
        average_scores.append({"name": name, "average_score": avg_score})
        highest_score = max(scores)
        highest_scores.append({"name": name, "highest_score": highest_score,})
    
    return (average_scores, highest_scores)

people_list = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [88, 92, 95]},
    {"name": "Charlie", "scores": [78, 80, 72]}
]

average_scores, highest_scores = process_scores(people_list)
print(average_scores)
print(highest_scores)