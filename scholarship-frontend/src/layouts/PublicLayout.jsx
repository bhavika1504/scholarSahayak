import { Outlet } from "react-router-dom";
import Header from "../components/Header";

export default function PublicLayout() {
  return (
    <div className="min-h-screen w-full bg-[#EAF2DD]">
      <Header />
      <Outlet />
    </div>
  );
}
