import styled, { css } from 'styled-components';
import { NavLink, useLocation } from 'react-router-dom';
import {
  FiHome, FiUser, FiMap, FiPackage, FiUsers, FiTruck, FiSettings, FiLogOut, FiChevronLeft, FiChevronRight
} from 'react-icons/fi';
import { FaCar } from 'react-icons/fa';
import { useState } from 'react';

const sidebarItems = [
  { label: 'Home', icon: <FiHome />, to: '/home' },
  { label: 'Usuário', icon: <FiUser />, to: '/usuario' },
  { label: 'Rotas', icon: <FiMap />, to: '/rotas' },
  { label: 'Entregas', icon: <FiPackage />, to: '/entregas' },
  { label: 'Clientes', icon: <FiUsers />, to: '/clientes' },
  { label: 'Motoristas', icon: <FiTruck />, to: '/motoristas' },
  { label: 'Veículos', icon: <FaCar />, to: '/veiculos' },
  { label: 'Configurações', icon: <FiSettings />, to: '/configuracoes' },
];

const SidebarContainer = styled.nav`
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: ${({ collapsed }) => (collapsed ? '64px' : '220px')};
  background: linear-gradient(135deg, var(--primary) 70%, var(--secondary) 100%);
  box-shadow: 2px 0 12px rgba(0,0,0,0.12);
  display: flex;
  flex-direction: column;
  z-index: 100;
  transition: width 0.2s;
  @media (max-width: 768px) {
    width: ${({ collapsed }) => (collapsed ? '0' : '180px')};
    min-width: 0;
    overflow-x: hidden;
  }
`;

const SidebarHeader = styled.div`
  display: flex;
  align-items: center;
  justify-content: ${({ collapsed }) => (collapsed ? 'center' : 'space-between')};
  padding: 24px 16px 16px 16px;
  font-size: 1.3rem;
  font-weight: bold;
  color: var(--text);
  letter-spacing: 1px;
`;

const CollapseButton = styled.button`
  background: none;
  border: none;
  color: var(--secondary);
  font-size: 1.3rem;
  cursor: pointer;
  transition: color 0.2s;
  &:hover {
    color: var(--warning);
  }
`;

const SidebarList = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
  flex: 1;
`;

const SidebarItem = styled.li`
  margin: 0;
`;

const activeClassName = 'sidebar-active';

const SidebarLink = styled(NavLink).attrs({ activeClassName })`
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 20px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 1.08rem;
  font-weight: 500;
  border-left: 4px solid transparent;
  transition: 
    background 0.18s,
    color 0.18s,
    border-color 0.18s,
    padding 0.18s;

  svg {
    font-size: 1.35rem;
    flex-shrink: 0;
  }

  &.${activeClassName} {
    color: var(--secondary);
    background: rgba(0,242,255,0.08);
    border-left: 4px solid var(--secondary);
    padding-left: 24px;
    position: relative;
    &::after {
      content: '';
      position: absolute;
      left: 0;
      bottom: 0;
      width: 100%;
      height: 2px;
      background: linear-gradient(90deg, var(--secondary), var(--warning));
      border-radius: 2px;
      animation: underline 0.4s;
    }
  }

  &:hover {
    color: var(--secondary);
    background: rgba(0,242,255,0.06);
    border-left: 4px solid var(--secondary);
  }

  ${({ collapsed }) =>
    collapsed &&
    css`
      justify-content: center;
      gap: 0;
      padding: 14px 0;
      span {
        display: none;
      }
    `}
`;

const LogoutButton = styled.button`
  background: none;
  border: none;
  color: var(--error);
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 1.08rem;
  font-weight: 500;
  padding: 14px 20px;
  width: 100%;
  cursor: pointer;
  border-left: 4px solid transparent;
  transition: background 0.18s, color 0.18s, border-color 0.18s, padding 0.18s;
  svg {
    font-size: 1.35rem;
    flex-shrink: 0;
  }
  &:hover {
    color: #fff;
    background: rgba(255,71,87,0.09);
    border-left: 4px solid var(--error);
  }
  ${({ collapsed }) =>
    collapsed &&
    css`
      justify-content: center;
      gap: 0;
      padding: 14px 0;
      span {
        display: none;
      }
    `}
`;

export function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);
  const location = useLocation();

  // Não renderiza a sidebar na tela de login
  if (location.pathname === '/login') {
    return null;
  }

  const handleLogout = () => {
    localStorage.clear();
    window.location.href = '/login';
  };

  return (
    <SidebarContainer collapsed={collapsed}>
      <SidebarHeader collapsed={collapsed}>
        {!collapsed && <span>RotaLog</span>}
        <CollapseButton
          aria-label={collapsed ? 'Expandir sidebar' : 'Colapsar sidebar'}
          onClick={() => setCollapsed((c) => !c)}
        >
          {collapsed ? <FiChevronRight /> : <FiChevronLeft />}
        </CollapseButton>
      </SidebarHeader>
      <SidebarList>
        {sidebarItems.map((item) => (
          <SidebarItem key={item.label}>
            <SidebarLink
              to={item.to}
              collapsed={collapsed ? 1 : 0}
              activeClassName={activeClassName}
            >
              {item.icon}
              <span>{item.label}</span>
            </SidebarLink>
          </SidebarItem>
        ))}
      </SidebarList>
      <LogoutButton onClick={handleLogout} collapsed={collapsed ? 1 : 0}>
        <FiLogOut />
        <span>Logout</span>
      </LogoutButton>
    </SidebarContainer>
  );
}