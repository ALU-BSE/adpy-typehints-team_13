from typing import TypedDict
class UserData(TypedDict):
    id: int
    name: str

class HistoryEntry(TypedDict):
    action: str
    timestamp: str

class ProcessedUserData(TypedDict, total=False):
    display_name: str
    normalized_id: str
    history: list[HistoryEntry]

def process_user_data(user_data: UserData, include_history=False):
    user_id: int = user_data["id"]
    name: str = user_data["name"]
    
    result:ProcessedUserData = {
        "display_name": f"User {name}",
        "normalized_id": str(user_id).zfill(8)
    }
    
    if include_history:
        result["history"] = get_user_history(user_id)
    
    return result

def get_user_history(user_id: int) -> list[HistoryEntry]:
    # Simulate database call
    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]

# Sample usage
sample_user: UserData = {"id": 42, "name": "Alice"}
processed: ProcessedUserData = process_user_data(sample_user, True)
print(processed)
