import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { LoginForm } from './components/Login/LoginForm';
import { ForgotPassword } from './components/ForgotPassword/ForgotPassword';
import { GlobalStyles } from './styles/GlobalStyles';

function App() {
  return (
    <BrowserRouter>
      <GlobalStyles />
      <Routes>
        <Route path="/login" element={<LoginForm />} />
        <Route path="/recuperar-senha" element={<ForgotPassword />} />
        <Route path="/" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;