# tasks.py

tasks = [
    {
        "id": "easy",
        "description": "Assign priority to bug",
        "input": "App crashes when clicking login",
        "expected_output": "High"
    },
    {
        "id": "medium",
        "description": "Assign team to bug",
        "input": "Login button UI broken",
        "expected_output": "Frontend"
    },
    {
        "id": "hard",
        "description": "Suggest fix",
        "input": "Null pointer exception in auth module",
        "expected_output": "Add null check"
    }
]