import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sla_report import load_tickets, add_sla_columns, SLA_HOURS

# 1. Data: only resolved tickets have a known outcome
df = add_sla_columns(load_tickets("data/tickets.csv"), SLA_HOURS)
df = df[df["status"] == "Resolved"].copy()

# 2. Features (known when the ticket is created) and target (what we predict)
X = pd.get_dummies(df[["priority", "issue_type", "agent"]])
y = df["breached"]

# 3. Split: 75% to learn, 25% for the "certification test"
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 4. Train
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

# 5. Test on unseen tickets
pred = model.predict(X_test)
print("Baseline - always guess 'no breach':", round((y_test == False).mean() * 100, 1), "%")
print("Model accuracy:", round(accuracy_score(y_test, pred) * 100, 1), "%")
print("\nConfusion matrix:")
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, target_names=["No breach", "Breach"]))

# 6. What did the model learn?
weights = pd.Series(model.coef_[0], index=X.columns).sort_values(ascending=False)
print("Features that push towards BREACH:")
print(weights.head(5).round(2))