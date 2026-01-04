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
      setError("Server error. Try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-screen grid grid-cols-1 md:grid-cols-2">

      {/* LEFT BRAND PANEL */}
      <div className="hidden md:flex flex-col justify-center items-center
                      bg-[#245330de] text-white px-16 relative">

        <div className="mb-6">
          <div className="w-20 h-20 rounded-full bg-white/10 
                          flex items-center justify-center border border-white/20">
            <span className="text-3xl">🎓</span>
          </div>
        </div>

        <h1 className="text-3xl font-bold mb-2">ScholarSahayak</h1>
        <p className="text-white/80 max-w-sm text-center">
          Welcome back. Your next scholarship opportunity is waiting.
        </p>

        {/* Decorative pattern */}
        <div className="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_1px_1px,white_1px,transparent_0)] 
                        [background-size:24px_24px]" />
      </div>

      {/* RIGHT LOGIN PANEL */}
      <div className="flex items-center justify-center bg-[#F3F6F4] px-6">
        <form
          onSubmit={handleLogin}
          className="w-full max-w-md bg-white rounded-2xl 
                     shadow-xl p-10"
        >
          <h2 className="text-2xl font-semibold text-[#243B53] mb-1">
            Sign In
          </h2>

          <p className="text-sm text-gray-500 mb-6">
            Access your personalized scholarships
          </p>

          {error && (
            <div className="mb-4 text-sm text-red-600 bg-red-50 px-4 py-2 rounded-lg">
              {error}
            </div>
          )}

          {/* Email */}
          <div className="mb-4">
            <label className="text-sm text-gray-600">Email Address</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="mt-1 w-full px-4 py-3 rounded-lg border
                         border-gray-200 focus:outline-none
                         focus:ring-2 focus:ring-[#9DB8A0]"
              placeholder="you@example.com"
            />
          </div>

          {/* Password */}
          <div className="mb-6">
            <label className="text-sm text-gray-600">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="mt-1 w-full px-4 py-3 rounded-lg border
                         border-gray-200 focus:outline-none
                         focus:ring-2 focus:ring-[#9DB8A0]"
              placeholder="••••••••"
            />
          </div>

          {/* Button */}
          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 rounded-lg font-semibold text-white
                       bg-[#6E8F75] hover:bg-[#5C7D66]
                       transition disabled:opacity-60"
          >
            {loading ? "Signing in..." : "Sign In"}
          </button>

          <p className="text-xs text-gray-500 mt-6 text-center">
            Don’t have an account?{" "}
            <span className="text-[#6E8F75] font-medium cursor-pointer">
              Create free account
            </span>
          </p>
        </form>
      </div>
    </div>
  );
}
