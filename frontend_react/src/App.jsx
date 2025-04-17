import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./Login";
import Home from "./Home";
import Cadastros from "./Cadastros"; // Importa o componente de Cadastros

function App() {
  const isAuthenticated = !!localStorage.getItem("token");

  return (
    <Router>
      <Routes>
        {/* Rota de Login */}
        <Route path="/login" element={<Login />} />

        {/* Rota da Home (protegida) */}
        <Route
          path="/home"
          element={isAuthenticated ? <Home /> : <Navigate to="/login" />}
        />

        {/* Rota de Cadastros (protegida) */}
        <Route
          path="/cadastros"
          element={isAuthenticated ? <Cadastros /> : <Navigate to="/login" />}
        />

        {/* Redireciona para /login por padrão */}
        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;