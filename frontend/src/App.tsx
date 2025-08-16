import { Route, Routes } from "react-router-dom";
import { RegisterPage } from "./Shopping/pages/SignUpPage";
import { WelcomePage } from "./Shopping/pages/WelcomePage";


const App = () => {
   return (
    <Routes>
      <Route path="/" element={<WelcomePage />} />
      <Route path="/RegisterPage" element={<RegisterPage />} />
    </Routes>
  );
};

export default App;
