import React from 'react';
import { FiEye, FiEdit, FiTrash2 } from 'react-icons/fi';
import './UserList.css';
import { userService } from '../../services/userService'; // Certifique-se de importar o serviço

export const UserList = ({ users, setUsers }) => {
  const handleDeactivate = async (userId) => {
    const confirm = window.confirm('Tem certeza que deseja desativar este usuário?');
    if (!confirm) return;

    try {
      await userService.disableUser(userId); // Chama o serviço para desativar o usuário
      alert('Usuário desativado com sucesso!');
      setUsers((prevUsers) => prevUsers.filter((user) => user.id !== userId)); // Remove o usuário da lista
    } catch (error) {
      console.error('Erro ao desativar usuário:', error);
      alert('Erro ao desativar o usuário. Tente novamente.');
    }
  };

  return (
    <div className="user-list-container">
      <table className="user-list-table">
        <thead>
          <tr>
            <th>Nome</th>
            <th>E-mail</th>
            <th>Perfil</th>
            <th>Status</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>
                <div className="user-info">
                  <div className="user-avatar">{user.name[0]}</div>
                  <div className="user-details">
                    <div className="user-name">{user.name}</div>
                    <div className="user-role">{user.position}</div>
                  </div>
                </div>
              </td>
              <td>{user.email}</td>
              <td>
                <span className={`user-role-badge ${user.position.toLowerCase()}`}>
                  {user.position}
                </span>
              </td>
              <td>
                <span
                  className={`status-badge ${
                    user.status === 'Ativo' ? 'active' : 'inactive'
                  }`}
                >
                  {user.status}
                </span>
              </td>
              <td>
                <div className="actions">
                  <button
                    className="action-button"
                    title="Detalhes"
                    onClick={() => alert(`Exibindo detalhes do usuário com ID: ${user.id}`)}
                  >
                    <FiEye />
                  </button>
                  <button
                    className="action-button"
                    title="Editar"
                    onClick={() => alert(`Editando usuário com ID: ${user.id}`)}
                  >
                    <FiEdit />
                  </button>
                  <button
                    className="action-button"
                    title="Desativar"
                    onClick={() => handleDeactivate(user.id)} // Chama a função de desativar
                  >
                    <FiTrash2 />
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};