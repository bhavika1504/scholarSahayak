
export default function Landing() {
  return (
    <div className="min-h-screen w-screen flex flex-col bg-[#EAF2DD] overflow-x-hidden">


      {/* MAIN CONTENT */}
      <main className="flex-grow">

        {/* HERO SECTION */}
        <section className="px-12 py-20 grid md:grid-cols-2 gap-10 items-center">
          <div>
            <h1 className="text-4xl md:text-5xl font-bold text-[#1F2937] mb-4 leading-tight">
              Unlock Your Future. <br /> Find Scholarships
            </h1>

            <p className="text-[#4B5563] mb-6 text-lg">
              AI-powered scholarship discovery curated just for you.
            </p>

            <button className="bg-[#6E8F75] hover:bg-[#5F8066] text-white px-6 py-3 rounded-xl transition">
              Start Your Search
            </button>
          </div>

          <div className="flex justify-center">
            <img
              src="img/frontPage.jpg"
              alt="Scholarship AI"
              className="max-w-md w-full"
            />
          </div>
        </section>

        {/* HOW IT WORKS */}
        <section id="how" className="px-12 py-16 bg-[#DDE8CF]">
          <h2 className="text-2xl font-semibold text-[#1F2937] mb-10 text-center">
            How It Works
          </h2>

          <div className="grid md:grid-cols-3 gap-6">
            {[
              { title: "Smart Matching", desc: "AI finds scholarships that fit you." },
              { title: "Easy Apply", desc: "Direct links, no confusion." },
              { title: "Track Progress", desc: "Know what you’ve applied for." },
            ].map((item) => (
              <div
                key={item.title}
                className="bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition"
              >
                <h3 className="font-semibold text-[#1F2937] mb-2">
                  {item.title}
                </h3>
                <p className="text-sm text-[#6B7280]">
                  {item.desc}
                </p>
              </div>
            ))}
          </div>
        </section>

      </main>

      {/* FOOTER */}
      <footer className="bg-[#344E41] text-[#EAF2DD] py-6 text-center text-sm">
        © {new Date().getFullYear()} ScholarSahayak • AI Powered 🎓
      </footer>

    </div>
  );
}
