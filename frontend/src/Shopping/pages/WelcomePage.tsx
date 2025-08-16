import { useNavigate } from "react-router-dom";
import Login from "../components/auth/Login";

export function WelcomePage() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-5xl font-bold text-green-600 mb-4">Welcome</h1>
      <div className="flex flex-col items-center">
        <Login onLoginSuccess={() => {}} />
        <span
          className="text-blue-600 underline cursor-pointer mt-1"
          onClick={() => navigate("/RegisterPage")}
        >
          Register
        </span>
      </div>
    </div>
  );
}