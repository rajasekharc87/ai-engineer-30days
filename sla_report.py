import pandas as pd

SLA_HOURS = {"P1": 4, "P2": 8, "P3": 24, "P4": 48}


def load_tickets(path):
    """Read the tickets file and convert date columns to real dates."""
    df = pd.read_csv(path)
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["resolved_at"] = pd.to_datetime(df["resolved_at"])
    df["agent"] = df["agent"].fillna("Unassigned")
    return df


def add_sla_columns(df, sla_hours):
    """Add hours taken, SLA target and a breached flag."""
    df["hours_taken"] = (df["resolved_at"] - df["created_at"]).dt.total_seconds() / 3600
    df["sla_target"] = df["priority"].map(sla_hours)
    df["breached"] = df["hours_taken"] > df["sla_target"]
    return df


def breach_rate(df, group_by=None):
    """Breach rate % for resolved tickets, overall or per group."""
    resolved = df[df["status"] == "Resolved"]
    if group_by is None:
        return round(resolved["breached"].mean() * 100, 1)
    return resolved.groupby(group_by)["breached"].mean().mul(100).round(1).sort_values(ascending=False)


if __name__ == "__main__":
    tickets = load_tickets("data/tickets.csv")
    tickets = add_sla_columns(tickets, SLA_HOURS)

    print("Overall breach rate:", breach_rate(tickets), "%")
    print("\nBy priority:")
    print(breach_rate(tickets, "priority"))
    print("\nBy agent:")
    print(breach_rate(tickets, "agent"))