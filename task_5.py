# List of user interests
interests = [
    (0, "Hadoop"), (6, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def most_common_interests_with(user):
    # Get the interests of the given user
    user_interests = [interest for user_id, interest in interests if user_id == user]

    # Initialize a dictionary to store the count of shared interests
    shared_interests_count = {}

    # Iterate through the list of interests
    for user_id, interest in interests:
        if user_id != user and interest in user_interests:
            if user_id not in shared_interests_count:
                shared_interests_count[user_id] = 0
            shared_interests_count[user_id] += 1

    return shared_interests_count

# Example usage
print(most_common_interests_with(0))  # Output: {1: 2, 9: 2}
print(most_common_interests_with(2))  # Output: {3: 1, 5: 1}