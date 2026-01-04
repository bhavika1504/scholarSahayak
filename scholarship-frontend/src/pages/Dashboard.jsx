import { useEffect, useState } from "react";
import ScholarshipCard from "../components/ScholarshipCard";

export default function Dashboard() {
  const [scholarships, setScholarships] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("token");

    fetch("http://localhost:5000/student/recommendations", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(res => res.json())
      .then(data => setScholarships(data.recommendations || []));
  }, []);

  // 🔥 SAVE HANDLER (THIS WAS MISSING)
  const handleSave = async (scholarshipId) => {
  const token = localStorage.getItem("token");

  const res = await fetch(
    `http://localhost:5000/student/scholarships/${scholarshipId}/save-scholarship`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  const data = await res.json();

  if (data.status) {
    alert("✅ Scholarship saved!");
  } else {
    alert(data.message || "Already saved");
  }
};


  return (
    <div className="flex min-h-screen w-full bg-[#EAF2DD]">
      

      <main className="flex-1 p-10 overflow-y-auto">
        <div className="flex justify-between items-center mb-10">
          <h1 className="text-4xl font-bold text-[#1F2937]">
            🎓 Smart Matches
          </h1>

          <button
            onClick={() => {
              localStorage.removeItem("token");
              window.location.href = "/";
            }}
            className="text-red-500"
          >
            Logout
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
          {scholarships.map((sch) => (
  <ScholarshipCard
    key={sch.scholarship_id}
    sch={sch}
    onSave={handleSave}
  />
))}

        </div>
      </main>
    </div>
  );
}
