# pipeline/pipeline_runner.py
from pipeline.collector import fetch_scholarships_from_web
from pipeline.normalizer import normalize_scholarship
from models.scholarship_model import ScholarshipModel

def run_pipeline():
    raw_scholarships = fetch_scholarships_from_web()

    for raw in raw_scholarships:
        clean = normalize_scholarship(raw)
        ScholarshipModel.create_scholarship(clean)

    return {
        "status": True,
        "inserted": len(raw_scholarships)
    }
