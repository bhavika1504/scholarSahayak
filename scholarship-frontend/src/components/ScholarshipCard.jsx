export default function ScholarshipCard({ sch, onSave }) {
  if (!sch) return null;

  const handleSaveClick = () => {
    if (!onSave) return;
    onSave(sch.scholarship_id);
  };

  return (
    <div className="bg-white rounded-2xl p-6 shadow-md hover:shadow-xl transition flex flex-col">
      <h2 className="text-lg font-semibold text-[#1F2937] mb-2">
        {sch.title}
      </h2>

      <p className="text-sm text-gray-600 mb-3">
        {sch.description}
      </p>

      <div className="text-sm mb-2">
        💰 <span className="font-medium">₹{sch.amount}</span>
      </div>

      <div className="text-xs text-gray-500 mb-3">
        ⏳ Deadline: {sch.deadline}
      </div>

      <p className="text-xs text-gray-500 mb-4">
        {sch.ai_explanation}
      </p>

      <div className="mt-auto flex gap-3">
        {/* APPLY */}
        <a
          href={sch.official_link}
          target="_blank"
          rel="noreferrer"
          className="flex-1 text-center bg-[#6E8F75] text-white py-2 rounded-lg hover:bg-[#5d7c65]"
        >
          Apply Now
        </a>

        {/* SAVE */}
        <button
          onClick={handleSaveClick}
          className="px-4 py-2 rounded-lg border border-[#6E8F75] text-[#6E8F75] hover:bg-[#6E8F75] hover:text-white transition"
        >
          Save
        </button>
      </div>
    </div>
  );
}
