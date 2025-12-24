def ai_scholarship_suggestions(student):
    suggestions = []
    reasons = []

    category = (student.get("category") or "").lower()
    course = (student.get("course") or "").lower()
    education = (student.get("education_level") or "").lower()
    income = student.get("annual_income")
    state_id = student.get("state_id")

    # National portals (for all)
    suggestions.append("National Scholarship Portal (NSP)")
    reasons.append("All verified central and state scholarships")

    # Category-based
    if category in ["obc", "sc", "st", "minority"]:
        suggestions.append(f"{category.upper()} Welfare Department Scholarships")
        reasons.append(f"Reserved category benefits available for {category.upper()} students")

    # Course-based
    if "it" in course or "engineering" in course:
        suggestions.append("AICTE & Technical Education Scholarships")
        reasons.append("Technical / engineering background detected")

    if "science" in course:
        suggestions.append("DST & Science Fellowship Programs")
        reasons.append("Science stream scholarships available")

    # Education level
    if "post" in education or "pg" in education:
        suggestions.append("UGC / Postgraduate Merit Scholarships")
        reasons.append("Postgraduate-level funding opportunities")

    # Income-based
    if income and income < 250000:
        suggestions.append("Income-based Merit-cum-Means Scholarships")
        reasons.append("Low income increases eligibility")

    # State-based
    if state_id:
        suggestions.append("State Government Scholarship Portal")
        reasons.append("State-specific benefits available")

    # Build keyword queries
    search_queries = [
        f"{education} {course} scholarship",
        f"{category} scholarship {course}",
        f"low income student scholarship"
    ]

    return {
        "portals": list(set(suggestions)),
        "search_keywords": list(set(search_queries)),
        "why_recommended": list(set(reasons))
    }
