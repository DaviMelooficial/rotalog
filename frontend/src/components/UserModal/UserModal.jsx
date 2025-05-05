import React, { useState } from 'react';
import { userService } from '../../services/userService';
import './UserModal.css'; // Estilos do modal

export const UserModal = ({ onClose }) => {
  const [formData, setFormData] = useState({
    name: '',
    cpf: '',
    email: '',
    position: '',
    username: '',
  });

  const [queryResult, setQueryResult] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await userService.registerUser(formData);
      alert('Usuário cadastrado com sucesso!');
      onClose();
    } catch (error) {
      console.error('Erro ao cadastrar usuário:', error);
    }
  };

  const handleConsult = async () => {
    try {
      const { cpf, email, name } = formData;
      if (!cpf && !email && !name) {
        alert('Por favor, forneça pelo menos um parâmetro para consulta (CPF, E-mail ou Nome).');
        return;
      }
      const result = await userService.consultUser({ cpf, email, name });
      setQueryResult(result);
    } catch (error) {
      console.error('Erro ao consultar usuário:', error);
      alert('Usuário não encontrado ou erro no servidor.');
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="close-button" onClick={onClose}>
          &times;
        </button>
        <h2>Registrar Usuário</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="name"
            placeholder="Nome"
            value={formData.name}
            onChange={handleChange}
          />
          <input
            type="text"
            name="cpf"
            placeholder="CPF"
            value={formData.cpf}
            onChange={handleChange}
          />
          <input
            type="email"
            name="email"
            placeholder="E-mail"
            value={formData.email}
            onChange={handleChange}
          />
          <input
            type="text"
            name="position"
            placeholder="Cargo"
            value={formData.position}
            onChange={handleChange}
          />
          <input
            type="text"
            name="username"
            placeholder="Usuário"
            value={formData.username}
            onChange={handleChange}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
            <button type="submit" className="submit-button">
              Registrar
            </button>
            <button
              type="button"
              className="consult-button"
              onClick={handleConsult}
              style={{
                background: 'var(--primary)',
                color: 'var(--text)',
                padding: '10px 20px',
                borderRadius: '8px',
                border: 'none',
                cursor: 'pointer',
                fontSize: '1rem',
                fontWeight: 'bold',
                transition: 'background 0.2s',
              }}
            >
              Consultar
            </button>
          </div>
        </form>
        {queryResult && (
          <div className="query-result" style={{ marginTop: '20px', color: 'var(--text)' }}>
            <h3>Resultado da Consulta:</h3>
            <p><strong>Nome:</strong> {queryResult.name}</p>
            <p><strong>CPF:</strong> {queryResult.cpf}</p>
            <p><strong>E-mail:</strong> {queryResult.email}</p>
            <p><strong>Cargo:</strong> {queryResult.position}</p>
            <p><strong>Status:</strong> {queryResult.status}</p>
          </div>
        )}
      </div>
    </div>
  );
};