import { useEffect, useState } from "react";

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

  return (
    <div className="min-h-screen bg-[#F6F7FB] p-8">
      
      {/* Header */}
      <div className="flex justify-between items-center mb-10">
        <h1 className="text-3xl font-bold text-[#0F172A]">
          🎓 Your Scholarships
        </h1>

        <button
          onClick={() => {
            localStorage.removeItem("token");
            window.location.href = "/";
          }}
          className="text-sm text-red-500 hover:underline"
        >
          Logout
        </button>
      </div>

      {/* Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {scholarships.map((sch) => (
          <div
            key={sch.scholarship_id}
            className="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition"
          >
            <h2 className="text-lg font-semibold text-[#5B5FEF] mb-2">
              {sch.title}
            </h2>

            <p className="text-sm text-gray-600 mb-3">
              {sch.description}
            </p>

            <div className="text-sm mb-2">
              💰 <span className="font-medium">₹{sch.amount}</span>
            </div>

            <div className="text-xs text-gray-500 mb-3">
              🕒 Deadline: {sch.deadline}
            </div>

            <div className="text-xs bg-indigo-50 text-indigo-600 px-3 py-1 rounded-full inline-block mb-3">
              Score: {sch.score}
            </div>

            <p className="text-xs text-gray-500 mb-4">
              {sch.ai_explanation}
            </p>

            <a
              href={sch.official_link}
              target="_blank"
              className="block text-center bg-[#5B5FEF] text-white py-2 rounded-lg hover:bg-[#4B4FE0] transition"
            >
              Apply Now
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}
