# utils/recommender.py
from models.scholarship_model import ScholarshipModel
import math
from datetime import date

def score_and_explain(student, scholarship_row):
    score = 0
    reasons = []

    cat = student.get("category")
    income = student.get("annual_income")
    course = (student.get("course") or "").lower()
    education = (student.get("education_level") or "").lower()
    state_id = student.get("state_id")

    income_limit = scholarship_row.get("income_limit")
    category_required = scholarship_row.get("category_required")
    course_required = scholarship_row.get("course_required")
    education_required = scholarship_row.get("education_level_required")
    sch_state = scholarship_row.get("state_id")

    # ---- Income check ----
    if income_limit is not None and income is not None:
        if int(income) > int(income_limit):
            return -9999, "Income exceeds limit"
        score += min(30, int(((income_limit - income) / (income_limit + 1)) * 30))
        reasons.append("Income within limit")

    # ---- Category ----
    if category_required:
        if cat and category_required.lower() == cat.lower():
            score += 30
            reasons.append("Category matched")
    else:
        score += 5

    # ---- Course ----
    if course_required:
        if course and (course_required.lower() in course or course in course_required.lower()):
            score += 25
            reasons.append("Course matched")
    else:
        score += 5

    # ---- Education ----
    if education_required:
        if education and education_required.lower() in education:
            score += 10
            reasons.append("Education level matched")

    # ---- State ----
    if sch_state and state_id and int(sch_state) == int(state_id):
        score += 10
        reasons.append("State matched")

    # ---- Amount ----
    try:
        amount_digits = int(''.join(ch for ch in str(scholarship_row.get("amount")) if ch.isdigit()) or 0)
        score += min(10, int(amount_digits / 10000))
    except:
        pass

    return int(score), "; ".join(reasons)

def recommend_for_student(student_id, limit=10):
    from models.student_model import StudentModel

    student = StudentModel.get_student_by_id(student_id)
    if not student:
        return []

    rows = ScholarshipModel.get_all_active_scholarships()

    scored = []

    today = date.today()

    for r in rows:
        # ---------------- DEADLINE CHECK ----------------
        deadline = r.get("deadline")
        if deadline:
            try:
                if deadline < today:
                    continue  
            except Exception:
                pass
        # ------------------------------------------------

        score, explanation = score_and_explain(student, r)

        # skip disqualified
        if score == -9999:
            continue

        scored.append({
            "scholarship_id": r["scholarship_id"],
            "title": r["title"],
            "description": r["description"],
            "amount": r["amount"],
            "provider_type": r.get("provider_type"),
            "state_id": r.get("state_id"),
            "deadline": r.get("deadline"),
            "score": score,
            "explanation": explanation,
            "official_link": r.get("official_link"),
            "created_at": r.get("created_at")
        })

    # sort by score desc, then newest first
    scored.sort(key=lambda x: (x["score"], x.get("created_at")), reverse=True)

    return scored[:limit]


def ai_enrich_explanation(student, scholarship):
    # Example placeholder
    # When you add OpenAI or other API, replace this function to call API.
    prompt = f"""Student: {student['name']}, age..., course: {student['course']}, income: {student['annual_income']}, category: {student['category']}...
Scholarship: {scholarship['title']} — {scholarship['description']}. Eligibility: ...
Write a one-sentence explanation why this scholarship is a good match and list missing docs."""
    # call OpenAI here and return text
    return "AI-generated explanation (placeholder)"

