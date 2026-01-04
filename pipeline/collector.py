# pipeline/collector.py

def fetch_scholarships_from_web():
    """
    Simulates scholarships fetched from web sources.
    Later this will be replaced by real scraping or APIs.
    """

    return [
        {
            "title": "AI Excellence Scholarship",
            "provider": "Government of India",
            "amount": "75000",
            "deadline": "2026-04-30",
            "link": "https://gov.in/ai-scholarship",
            "description": "For IT students interested in AI and ML",
            "category": "General",
            "income_limit": 800000,
            "course": "IT"
        },
        {
            "title": "Women in Tech Scholarship",
            "provider": "Private Foundation",
            "amount": "50000",
            "deadline": "2026-03-15",
            "link": "https://example.org/women-tech",
            "description": "Scholarship for women pursuing CS/IT",
            "category": "Female",
            "income_limit": 600000,
            "course": "Computer Science"
        }
    ]
