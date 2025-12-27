import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.error || "Invalid credentials");
        return;
      }

      localStorage.setItem("token", data.token);
      navigate("/dashboard");
    } catch {
      setError("Server error. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#F7F9FC] px-4">
      <div className="w-full max-w-5xl bg-white rounded-3xl shadow-xl flex overflow-hidden">

        {/* LEFT – LOGIN CARD */}
        <div className="w-full md:w-1/2 p-10">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">
            Welcome Back 👋
          </h1>
          <p className="text-gray-500 mb-6">
            Login to explore scholarships curated for you
          </p>

          {error && (
            <div className="mb-4 text-sm text-red-600 bg-red-50 px-4 py-2 rounded-lg">
              {error}
            </div>
          )}

          <form onSubmit={handleLogin} className="space-y-5">

            {/* Email */}
            <div>
              <label className="text-sm text-gray-600">Email</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@example.com"
                required
                className="mt-1 w-full px-4 py-3 rounded-lg border border-gray-200
                           focus:outline-none focus:ring-2 focus:ring-indigo-300
                           transition"
              />
            </div>

            {/* Password */}
            <div>
              <label className="text-sm text-gray-600">Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                required
                className="mt-1 w-full px-4 py-3 rounded-lg border border-gray-200
                           focus:outline-none focus:ring-2 focus:ring-indigo-300
                           transition"
              />
            </div>

            {/* Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 rounded-lg font-semibold text-white
                         bg-linear-to-r from-indigo-400 to-purple-400
                         hover:from-indigo-500 hover:to-purple-500
                         transition-all duration-300 disabled:opacity-60"
            >
              {loading ? "Logging in..." : "Login"}
            </button>
          </form>

          <p className="text-xs text-gray-500 mt-6 text-center">
            Scholarship Sahayak • AI Powered 🎓
          </p>
        </div>

        {/* RIGHT – ILLUSTRATION */}
        <div className="hidden md:flex w-1/2 bg-[#EEF2FF] items-center justify-center">
          <img
            src="/login-illustration.png"
            alt="Scholarship Illustration"
            className="max-w-sm"
          />
        </div>
      </div>
    </div>
  );
}
