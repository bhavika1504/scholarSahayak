import { useEffect, useState } from "react";

export default function Applied() {
  const [data, setData] = useState([]);
  const token = localStorage.getItem("token");

  useEffect(() => {
    fetch("http://localhost:5000/student/applied", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">📨 Applied Scholarships</h1>

      {data.map(s => (
        <div key={s.scholarship_id}
          className="bg-white rounded-xl p-5 mb-4 shadow-sm">
          <h2 className="font-semibold">{s.title}</h2>
          <p className="text-sm text-gray-600">{s.description}</p>
        </div>
      ))}
    </div>
  );
}
