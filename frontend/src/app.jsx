import { BrowserRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import { LoginForm } from './components/Login/LoginForm';
import { ForgotPassword } from './components/ForgotPassword/ForgotPassword';
import { GlobalStyles } from './styles/GlobalStyles';
import { Sidebar } from './components/Sidebar/Sidebar';
import { UserManagement } from './pages/UserManagement'; // Importação da nova página

function MainContent({ children }) {
  const location = useLocation();
  const isLogin = location.pathname === '/login';

  return (
    <div
      style={{
        marginLeft: isLogin ? 0 : '220px', // Remove margem na tela de login
        transition: 'margin-left 0.2s',
        minHeight: '100vh',
        background: 'var(--background)',
      }}
    >
      {children}
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <GlobalStyles />
      <Sidebar />
      <MainContent>
        <Routes>
          <Route path="/login" element={<LoginForm />} />
          <Route path="/recuperar-senha" element={<ForgotPassword />} />
          <Route path="/usuarios" element={<UserManagement />} /> {/* Nova rota */}
          <Route path="/" element={<Navigate to="/login" replace />} />
          {/* Outras rotas */}
        </Routes>
      </MainContent>
    </BrowserRouter>
  );
}

export default App;