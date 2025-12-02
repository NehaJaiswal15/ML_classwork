def fetch_from_logs(filepath="experimental.txt"):
    experiments = []

    with open(filepath, "r") as file:
        for line in file:
            parts = line.strip().split()
            experiments.append({
                "date": parts[0],
                "experiment": parts[1].split(":")[1],
                "temperature": float(parts[2].split(":")[1])
            })
    return experiments

if __name__ == "__main__":
    data = fetch_from_logs()
    print("\nExperimental Logging Data")
    for entry in data:
        print(entry)
