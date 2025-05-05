import React, { useState } from 'react';
import { userService } from '../../services/userService';

export const UserForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    cpf: '',
    email: '',
    position: '',
    username: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await userService.registerUser(formData);
      alert('Usuário cadastrado com sucesso!');
    } catch (error) {
      console.error('Erro ao cadastrar usuário:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Registrar Usuário</h2>
      <input
        type="text"
        name="name"
        placeholder="Nome"
        value={formData.name}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="cpf"
        placeholder="CPF"
        value={formData.cpf}
        onChange={handleChange}
        required
      />
      <input
        type="email"
        name="email"
        placeholder="E-mail"
        value={formData.email}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="position"
        placeholder="Cargo"
        value={formData.position}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="username"
        placeholder="Usuário"
        value={formData.username}
        onChange={handleChange}
        required
      />
      <button type="submit">Registrar</button>
    </form>
  );
};