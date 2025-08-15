import Login from '../components/auth/Login';
import  Register  from '../components/auth/Register';

export function WelcomePage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-5xl font-bold text-green-600 mb-4">Welcome</h1>
      <div className="flex gap-8">
        <div>
          <Login onLoginSuccess={() => {}} />
        </div>
        <div>
          <Register onRegisterSucess={() => {}} />
        </div>
      </div>
    </div>
  );
}