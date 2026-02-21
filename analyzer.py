def add_log(logs, date, category, amount):
    logs.append({
        "date": date, 
        "category": category, 
        "amount": amount, 
        "user_data": True
        })
    
    while logs and logs[0]["user_data"] is False:
        logs.pop(0)


def filter_by_category(logs, category):
    try:
        result = list(
            filter(lambda log: log["category"] == category, logs)
        )
        if result == []:
            return False
        else:
            return result
    except KeyError:
        return False

    


def total_spent(logs):
    amounts = 0
    total = 0
    amounts = map(lambda log: log["amount"], logs)

    for amount in amounts:
        total += amount
        return total


def summary_by_category(logs):
    categories = []
    totals = []

    for log in logs:    
        category = log["category"]
        amount = log["amount"]

        if category in categories:
            idx = categories.index(category)
            totals[idx] += amount
        else:
            categories.append(category)
            totals.append(amount)

    return categories, totals



def top_categories(logs):
    categories, totals = summary_by_category(logs)
    top_3 = []
    top_in_tuples = []
    for category, total in zip(categories,totals):
        top_in_tuples.append((category, total))
    
    sorted_categories = sorted(top_in_tuples, key = lambda total: total[1], reverse= True)
    top_3 = sorted_categories[:3]
    
    return top_3