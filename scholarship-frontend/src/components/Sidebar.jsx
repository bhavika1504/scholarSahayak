import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-[#1F2F45] text-white p-6">
      <h2 className="text-xl font-bold mb-10">ScholarSahayak</h2>

      <nav className="flex flex-col gap-4">
        <Link to="/" className="hover:text-[#B7D3B0]">🏠 Home</Link>
        <Link to="/dashboard" className="hover:text-[#B7D3B0]">🤖 AI Matcher</Link>
        <Link to="/applications" className="hover:text-[#B7D3B0]">📄 My Applications</Link>
        <Link to="/saved" className="hover:text-[#B7D3B0]">💾 Saved</Link>
      </nav>
    </aside>
  );
}
