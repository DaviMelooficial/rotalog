import React, { useState } from 'react';
import { UserList } from '../components/UserList/UserList';
import { Sidebar } from '../components/Sidebar/Sidebar';
import { UserModal } from '../components/UserModal/UserModal';
import { userService } from '../services/userService';

export const UserManagement = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [users, setUsers] = useState([]); // Estado para armazenar os usuários

  const handleOpenModal = () => setIsModalOpen(true);
  const handleCloseModal = () => setIsModalOpen(false);

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleConsult = async () => {
    if (!searchTerm) {
      alert('Por favor, insira um termo de busca para consulta.');
      return;
    }
    try {
      const result = await userService.consultUser({ name: searchTerm });
      setUsers([result]); // Atualiza a lista com o usuário consultado
    } catch (error) {
      console.error('Erro ao consultar usuário:', error);
      alert(error);
    }
  };

  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <Sidebar />
      <div style={{ flex: 1, padding: '40px', overflowY: 'auto' }}>
        <div style={{ marginBottom: '30px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h1 style={{ color: 'var(--text)', fontSize: '2rem' }}>Gerenciamento de Usuários</h1>
            <button
              onClick={handleOpenModal}
              style={{
                background: 'var(--secondary)',
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
              + Criar Usuário
            </button>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', marginTop: '20px', gap: '10px' }}>
            <input
              type="text"
              placeholder="Buscar usuários..."
              value={searchTerm}
              onChange={handleSearchChange}
              style={{
                flex: 1,
                padding: '10px',
                borderRadius: '8px',
                border: '1px solid rgba(255, 255, 255, 0.1)',
                background: 'var(--background)',
                color: 'var(--text-secondary)',
                fontSize: '1rem',
              }}
            />
            <button
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
        </div>
        <UserList users={users} /> {/* Passa os usuários para o componente UserList */}
        {isModalOpen && <UserModal onClose={handleCloseModal} />}
      </div>
    </div>
  );
};