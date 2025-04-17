import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await axios.post("http://localhost:5000/auth/login", {
        username,
        password,
      });

      const { access_token, user } = response.data;

      // Salva o token no localStorage
      localStorage.setItem("token", access_token);

      // Redireciona para a página inicial
      navigate("/home");
    } catch (err) {
      if (err.response && err.response.data && err.response.data.error) {
        setError(err.response.data.error);
      } else {
        setError("Erro ao conectar ao servidor.");
      }
    }
  };

  return (
    <div className="login-container">
      <div className="login-content">
        <h2 className="login-title">Login</h2>
        <form onSubmit={handleSubmit}>
          {error && <p className="login-error">{error}</p>}
          <div className="form-group">
            <label htmlFor="username">E-mail ou usuário</label>
            <input
              type="text"
              id="username"
              placeholder="Seu e-mail ou nome de usuário"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Senha</label>
            <input
              type="password"
              id="password"
              placeholder="Sua senha"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="login-button">
            Entrar
          </button>
        </form>
        <a href="/forgot-password" className="forgot-password-link">
          Esqueci minha senha
        </a>
      </div>
    </div>
  );
};

export default Login;