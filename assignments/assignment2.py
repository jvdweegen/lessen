import json

def load_json(filepath="user_data.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def extract_provider(email):
    """Extract the domain from an email address"""
    if "@" in email:
        return email.split("@")[1]
    return "Invalid emailadress which was probably added to the dataset for this reason"

def count_providers(entries):
    """Count how many times each email provider appears (pure Python)"""
    provider_counts = {}
    for entry in entries:
        provider = extract_provider(entry["email"])
        if provider in provider_counts:
            provider_counts[provider] += 1
        else:
            provider_counts[provider] = 1
    return provider_counts

def print_provider_counts(provider_counts):
    print("Email Provider Counts:")
    for provider, count in provider_counts.items():
        print(f"{provider}: {count}")

if __name__ == "__main__":
    entries = load_json()
    provider_counts = count_providers(entries)
    print_provider_counts(provider_counts)
