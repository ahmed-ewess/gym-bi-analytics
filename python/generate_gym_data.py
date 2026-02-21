import random
from datetime import datetime, timedelta
import csv

random.seed(42)

N = 2500

membership_types = [
    ("Basic", 19.99),
    ("Premium", 34.99),
    ("Elite", 49.99),
]

payment_methods = ["SEPA", "Credit Card", "PayPal"]
genders = ["M", "F", "D"]

start_date = datetime(2023, 1, 1)
end_date = datetime(2026, 2, 1)

def rand_date(a: datetime, b: datetime) -> datetime:
    delta = b - a
    return a + timedelta(days=random.randint(0, delta.days))

rows = []
for i in range(1, N + 1):
    join = rand_date(start_date, end_date - timedelta(days=30))
    last_visit = rand_date(join, end_date)

    age = random.randint(16, 55)
    gender = random.choice(genders)

    mtype, fee = random.choice(membership_types)

    visits_30d = max(0, int(random.gauss(8 if mtype != "Basic" else 6, 4)))
    pt_sessions_90d = max(0, int(random.gauss(3 if mtype == "Elite" else 1, 2)))

    inactivity_days = (end_date - last_visit).days
    cancel_prob = min(0.85, max(0.05, inactivity_days / 180))
    cancelled = 1 if random.random() < cancel_prob else 0

    if cancelled and inactivity_days < 30:
        last_visit = end_date - timedelta(days=random.randint(30, 180))
        inactivity_days = (end_date - last_visit).days

    rows.append({
        "MemberID": i,
        "Age": age,
        "Gender": gender,
        "MembershipType": mtype,
        "MonthlyFee": fee,
        "JoinDate": join.date().isoformat(),
        "LastVisitDate": last_visit.date().isoformat(),
        "VisitsLast30Days": visits_30d,
        "PersonalTrainingSessionsLast90Days": pt_sessions_90d,
        "PaymentMethod": random.choice(payment_methods),
        "InactivityDays": inactivity_days,
        "Cancelled": cancelled
    })

with open("data/gym_membership_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print("Created data/gym_membership_data.csv with", len(rows), "rows")