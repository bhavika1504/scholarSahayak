# utils/recommender.py
from models.scholarship_model import ScholarshipModel
import math

def score_and_explain(student, scholarship_row):
    """
    student: dict from student_model.get_student_by_id
    scholarship_row: dict from ScholarshipModel.get_all_with_eligibility()
    returns: (score:int, explanation:str)
    """
    score = 0
    reasons = []

    # quick convenience
    cat = student.get("category")
    income = student.get("annual_income")
    course = (student.get("course") or "").lower()
    education = (student.get("education_level") or "").lower()
    state_id = student.get("state_id")

    # eligibility fields (may be None)
    income_limit = scholarship_row.get("income_limit")
    category_required = scholarship_row.get("category_required")
    course_required = scholarship_row.get("course_required")
    education_required = scholarship_row.get("education_required")
    min_marks = scholarship_row.get("min_marks")
    sch_state = scholarship_row.get("state_id")

    # Disqualify if explicit income_limit and student's income > limit
    if income_limit is not None:
        try:
            if income is not None and int(income) > int(income_limit):
                return -9999, f"Not eligible: income {income} exceeds limit {income_limit}"
            else:
                # lower income means stronger eligibility
                if income is not None:
                    # closer to 0 income => higher score; normalized
                    inv = max(0, int(income_limit) - int(income)) if income_limit else 0
                    score += min(30, int((inv / (int(income_limit) + 1)) * 30))
                    reasons.append("Income within limit")
        except Exception:
            pass

    # Category match
    if category_required:
        if cat and category_required.strip().lower() == cat.strip().lower():
            score += 30
            reasons.append(f"Category matches ({cat})")
        else:
            # if scholarship allows all categories (NULL) it's better than mismatch
            pass
    else:
        # no category restriction -> small bonus
        score += 5

    # Course match
    if course_required:
        if course and course_required.strip().lower() in course:
            score += 25
            reasons.append(f"Course requirement matched ({course_required})")
    else:
        score += 5

    # Education level match
    if education_required:
        if education and education_required.strip().lower() in education:
            score += 10
            reasons.append(f"Education level matches ({education_required})")

    # State match (local scholarships get bonus)
    try:
        if sch_state and state_id and int(sch_state) == int(state_id):
            score += 10
            reasons.append("State match (local scholarship)")
    except Exception:
        pass

    # amount weight: larger amounts get a small boost
    try:
        amount_raw = scholarship_row.get("amount") or ""
        # parse digits from amount if formatted like '50,000' or '₹50000'
        amount_digits = int(''.join(ch for ch in str(amount_raw) if ch.isdigit()) or 0)
        if amount_digits > 0:
            score += min(10, amount_digits / 10000)  # scale
    except Exception:
        pass

    # final normalization
    score = int(math.floor(score))

    explanation = "; ".join(reasons) if reasons else "No explicit eligibility fields matched, check detailed criteria."
    return score, explanation


def recommend_for_student(student_id, limit=10):
    student = None
    # lazy import to avoid circulars
    from models.student_model import StudentModel
    student = StudentModel.get_student_by_id(student_id)
    if not student:
        return []

    rows = ScholarshipModel.get_all_with_eligibility()
    scored = []
    for r in rows:
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
            "score": score,
            "explanation": explanation,
            "official_link": r.get("official_link"),
            "created_at": r.get("created_at")
        })

    # sort by score desc then created_at
    scored.sort(key=lambda x: (x["score"], x.get("created_at")), reverse=True)
    return scored[:limit]
