import json

def load_logs(path = "data.json"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            logs = json.load(file)
            status = "Loading correct"
            return logs, status 
        
    except FileNotFoundError:
        status = "FileNotFoundError"
        return [], status
    
    except json.decoder.JSONDecodeError:
        status = "json.decoder.JSONDecodeError"
        return None, status


def save_logs(logs, path="data.json"):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=2, ensure_ascii=False)
