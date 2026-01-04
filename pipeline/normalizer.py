# pipeline/normalizer.py
from datetime import datetime

def normalize_scholarship(raw):
    """
    Converts raw web data into DB-ready format
    """

    return {
        "title": raw.get("title"),
        "provider_type": "Government" if "gov" in raw.get("provider", "").lower() else "Private",
        "amount": raw.get("amount"),
        "deadline": raw.get("deadline"),
        "official_link": raw.get("link"),
        "description": raw.get("description"),
        "category_required": raw.get("category"),
        "income_limit": raw.get("income_limit"),
        "course_required": raw.get("course"),
        "education_required": None,
        "created_at": datetime.now()
    }
