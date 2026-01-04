import { Link, useNavigate } from "react-router-dom";

export default function Header() {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  return (
    <header className="w-full px-10 py-4 flex justify-between items-center bg-[#EAF2DD]">
      <Link to="/" className="text-xl font-bold text-[#2F4F4F]">
        ScholarSahayak
      </Link>

      <nav className="flex gap-6 items-center">
        <Link to="/" className="text-[#2F4F4F] hover:underline">Home</Link>

        {!token ? (
          <>
            <Link to="/login" className="text-[#2F4F4F] hover:underline">
              Login
            </Link>
            <Link
              to="/login"
              className="bg-[#6E8F75] text-white px-4 py-2 rounded-lg"
            >
              Register
            </Link>
          </>
        ) : (
          <button
            onClick={() => {
              localStorage.removeItem("token");
              navigate("/");
            }}
            className="text-red-500"
          >
            Logout
          </button>
        )}
      </nav>
    </header>
  );
}
