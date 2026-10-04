from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


DATA = [
    ("python sql pandas data analysis statistics excel", "Data Analyst"),
    ("python pandas numpy data visualization sql", "Data Analyst"),
    ("power bi sql excel dashboard data", "Data Analyst"),
    ("python machine learning pandas numpy scikit learn", "ML Engineer"),
    ("tensorflow pytorch deep learning python", "ML Engineer"),
    ("nlp machine learning python sklearn", "ML Engineer"),
    ("javascript react html css frontend", "Web Developer"),
    ("react javascript css html frontend web", "Web Developer"),
    ("typescript react javascript node web", "Web Developer"),
    ("python flask django rest api backend", "Python Developer"),
    ("python django flask api backend sql", "Python Developer"),
    ("python fastapi rest api backend mongodb", "Python Developer"),
]


def evaluate_model():
    texts = [item[0] for item in DATA]
    labels = [item[1] for item in DATA]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        labels,
        test_size=0.25,
        random_state=42,
        stratify=labels
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    return {
        "accuracy": round(accuracy_score(y_test, predictions), 2),
        "precision": round(
            precision_score(y_test, predictions, average="weighted", zero_division=0), 2
        ),
        "recall": round(
            recall_score(y_test, predictions, average="weighted", zero_division=0), 2
        ),
        "f1_score": round(
            f1_score(y_test, predictions, average="weighted", zero_division=0), 2
        )
    }


if __name__ == "__main__":
    print(evaluate_model())
