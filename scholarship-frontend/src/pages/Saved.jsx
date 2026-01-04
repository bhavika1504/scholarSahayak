import { useEffect, useState } from "react";

export default function Saved() {
  const [saved, setSaved] = useState([]);
  const [loading, setLoading] = useState(true);
  const token = localStorage.getItem("token");

  useEffect(() => {
    fetch("http://localhost:5000/student/saved", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(res => res.json())
      .then(data => {
        setSaved(data || []);
      })
      .catch(() => {
        setSaved([]);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="p-10 text-gray-600">
        Loading saved scholarships...
      </div>
    );
  }

  return (
    <div className="p-10 min-h-screen w-4xl bg-[#EAF2DD]">
      <h1 className="text-3xl font-bold mb-8 text-[#1F2937]">
        💾 Saved Scholarships
      </h1>

      {saved.length === 0 ? (
        <div className="text-gray-600 bg-white p-6 rounded-xl shadow-sm">
          You haven’t saved any scholarships yet.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
          {saved.map((s) => (
            <div
              key={s.scholarship_id}
              className="bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition"
            >
              <h2 className="text-lg font-semibold text-[#1F2937] mb-2">
                {s.title}
              </h2>

              <p className="text-sm text-gray-600 mb-3">
                {s.description}
              </p>

              <div className="text-sm mb-3">
                💰 <span className="font-medium">₹{s.amount}</span>
              </div>

              <a
                href={s.official_link}
                target="_blank"
                rel="noreferrer"
                className="block text-center bg-[#6E8F75] text-white py-2 rounded-lg hover:bg-[#5d7c65]"
              >
                Apply Now
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
