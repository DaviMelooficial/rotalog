import React from "react";
import { NavLink } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHome,
  faTruck,
  faRoute,
  faUser,
  faChartLine,
  faCogs,
  faSignOutAlt,
  faUsers, // Ícone para Cadastros
} from "@fortawesome/free-solid-svg-icons";
import "./Sidebar.css";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2 className="sidebar-title">Menu</h2>
      <nav className="sidebar-nav">
        <NavLink
          to="/home"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <FontAwesomeIcon icon={faHome} className="sidebar-icon" />
          Painel geral
        </NavLink>
        <NavLink
          to="/deliveries"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <FontAwesomeIcon icon={faTruck} className="sidebar-icon" />
          Entregas
        </NavLink>
        <NavLink
          to="/routes"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <FontAwesomeIcon icon={faRoute} className="sidebar-icon" />
          Criar rotas
        </NavLink>
        <NavLink
          to="/cadastros" // Adiciona a rota para Cadastros
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <FontAwesomeIcon icon={faUsers} className="sidebar-icon" />
          Cadastros
        </NavLink>
        <NavLink
          to="/reports"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <FontAwesomeIcon icon={faChartLine} className="sidebar-icon" />
          Relatórios
        </NavLink>
        <NavLink
          to="/profile"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <FontAwesomeIcon icon={faUser} className="sidebar-icon" />
          Perfil
        </NavLink>
        <NavLink
          to="/settings"
          className={({ isActive }) =>
            isActive ? "sidebar-link active" : "sidebar-link"
          }
        >
          <FontAwesomeIcon icon={faCogs} className="sidebar-icon" />
          Configurações
        </NavLink>
        <NavLink
          to="/logout"
          className="sidebar-link"
          onClick={() => {
            localStorage.removeItem("token");
            window.location.href = "/login";
          }}
        >
          <FontAwesomeIcon icon={faSignOutAlt} className="sidebar-icon" />
          Sair
        </NavLink>
      </nav>
    </div>
  );
};

export default Sidebar;