import pandas as pd

df = pd.read_csv("data/tickets.csv")

# 1. Convert text to real dates
df["created_at"] = pd.to_datetime(df["created_at"])
df["resolved_at"] = pd.to_datetime(df["resolved_at"])

# 2. How many hours each ticket took
df["hours_taken"] = (df["resolved_at"] - df["created_at"]).dt.total_seconds() / 3600

# 3. SLA target for each priority
sla_hours = {"P1": 4, "P2": 8, "P3": 24, "P4": 48}
df["sla_target"] = df["priority"].map(sla_hours)

# 4. Did it breach?
df["breached"] = df["hours_taken"] > df["sla_target"]

# 5. Data quality: label tickets with no agent
df["agent"] = df["agent"].fillna("Unassigned")

# 6. Only resolved tickets have a final result
resolved = df[df["status"] == "Resolved"]

print("Overall breach rate:", round(resolved["breached"].mean() * 100, 1), "%")
print("\nBreach rate % by priority:")
print(resolved.groupby("priority")["breached"].mean().mul(100).round(1))
print("\nBreach rate % by agent:")
print(resolved.groupby("agent")["breached"].mean().mul(100).round(1).sort_values(ascending=False))