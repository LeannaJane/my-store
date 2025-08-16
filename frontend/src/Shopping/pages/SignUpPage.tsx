import Register from "../components/auth/Register";

export function RegisterPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-4xl font-bold text-green-600 mb-4">Register</h1>
      <Register onRegisterSucess={() => {}} />
    </div>
  );
}