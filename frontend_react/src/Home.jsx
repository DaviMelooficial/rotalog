import React from "react";
import Sidebar from "./Sidebar";
import "./Home.css";

const Home = () => {
  return (
    <div className="home-container">
      <Sidebar />
      <div className="home-content">
      <header className="home-header-card">
          <div className="home-header">
            <h1>Painel de Logística</h1>
            <div className="user-info">
              <span>Bem-vindo, Admin</span>
              <span className="user-icon">👤</span>
            </div>
          </div>
        </header>

        <section className="status-section">
          <h2>Status das Entregas</h2>
          <div className="status-cards">
            <div className="status-card success">
              <div className="status-icon">✅</div>
              <div>
                <h3>185</h3>
                <p>(+12.8%) Comparado ao mês anterior</p>
                <p>Entregas no Prazo</p>
              </div>
            </div>
            <div className="status-card danger">
              <div className="status-icon">⚠️</div>
              <div>
                <h3>23</h3>
                <p>Necessitam atenção imediata</p>
                <p>Entregas Atrasadas</p>
              </div>
            </div>
          </div>
        </section>

        <section className="deliveries-section">
          <h2>Entregas do Dia</h2>
          <table className="deliveries-table">
            <thead>
              <tr>
                <th>ID do Pedido</th>
                <th>Cidade</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>#ORD-2350</td>
                <td>Curitiba, PR</td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
              <tr>
                <td>#ORD-2351</td>
                <td>Porto Alegre, RS</td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
              <tr>
                <td>#ORD-2352</td>
                <td>Goiânia, GO</td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
              <tr>
                <td>#ORD-2353</td>
                <td>Manaus, AM</td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
            </tbody>
          </table>
        </section>

        <section className="pending-deliveries-section">
          <h2>Entregas Pendentes</h2>
          <table className="deliveries-table">
            <thead>
              <tr>
                <th>ID do Pedido</th>
                <th>Cidade</th>
                <th>Data Prevista</th>
                <th>Status</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>#ORD-2345</td>
                <td>São Paulo, SP</td>
                <td>16/07/2024</td>
                <td>
                  <span className="status-label atrasada">Atrasada</span>
                </td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
              <tr>
                <td>#ORD-2346</td>
                <td>Rio de Janeiro, RJ</td>
                <td>17/07/2024</td>
                <td>
                  <span className="status-label atrasada">Atrasada</span>
                </td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
              <tr>
                <td>#ORD-2347</td>
                <td>Belo Horizonte, MG</td>
                <td>15/07/2024</td>
                <td>
                  <span className="status-label no-prazo">No prazo</span>
                </td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
              <tr>
                <td>#ORD-2348</td>
                <td>Salvador, BA</td>
                <td>16/07/2024</td>
                <td>
                  <span className="status-label no-prazo">No prazo</span>
                </td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
              <tr>
                <td>#ORD-2349</td>
                <td>Fortaleza, CE</td>
                <td>16/07/2024</td>
                <td>
                  <span className="status-label no-prazo">No prazo</span>
                </td>
                <td>
                  <button>Detalhes</button>
                </td>
              </tr>
            </tbody>
          </table>
          <div className="pagination">
            <button className="page-button">1</button>
            <button className="page-button">2</button>
            <button className="page-button">3</button>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Home;