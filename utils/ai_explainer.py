def generate_ai_explanation(student, scholarship):
    """
    Rule-based AI explanation (LLM-ready)
    Safe, explainable, no external dependency
    """

    reasons = []
    docs = []

    # Matching reasons
    if scholarship.get("state_id") == student.get("state_id"):
        reasons.append("it is applicable to your state")

    if scholarship.get("category_required") == student.get("category"):
        reasons.append("your category matches the eligibility")

    if scholarship.get("course_required") and \
       scholarship["course_required"].lower() in (student.get("course") or "").lower():
        reasons.append("your course matches the requirement")

    if scholarship.get("income_limit") and \
       student.get("annual_income") <= scholarship.get("income_limit"):
        reasons.append("your family income is within the limit")

    # Documents (generic but realistic)
    docs.extend([
        "Aadhaar Card",
        "Income Certificate",
        "Caste Certificate (if applicable)",
        "Previous Year Marksheet",
        "Bank Account Details"
    ])

    explanation = "This scholarship is recommended because " + ", ".join(reasons) + "."

    return {
        "ai_explanation": explanation,
        "required_documents": docs
    }
