import React, { useState, useEffect } from "react";
import Sidebar from "./Sidebar";
import axios from "axios";
import "./Cadastros.css";

const Cadastros = () => {
  const [tipoCadastro, setTipoCadastro] = useState("clientes"); // clientes, motoristas, veiculos
  const [formData, setFormData] = useState({
    cnpj: "",
    razao_social: "",
    nome_fantasia: "",
    telefone: "",
    email: "",
  });
  const [mensagem, setMensagem] = useState("");
  const [clientes, setClientes] = useState([]);
  const [pesquisa, setPesquisa] = useState("");

  useEffect(() => {
    if (tipoCadastro === "clientes") {
      listarClientes();
    }
  }, [tipoCadastro]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const cadastrarCliente = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/cadastrar_cliente",
        formData
      );
      setMensagem(response.data.mensagem);
      setFormData({
        cnpj: "",
        razao_social: "",
        nome_fantasia: "",
        telefone: "",
        email: "",
      });
      listarClientes(); // Atualiza a lista após o cadastro
    } catch (error) {
      setMensagem(error.response?.data?.erro || "Erro ao cadastrar cliente.");
    }
  };

  const listarClientes = async () => {
    try {
      // Simulação de listagem de clientes
      const response = await axios.get("http://localhost:5000/listar_clientes"); // Endpoint fictício
      setClientes(response.data);
    } catch (error) {
      setMensagem("Erro ao carregar a lista de clientes.");
    }
  };

  const renderFormulario = () => {
    if (tipoCadastro === "clientes") {
      return (
        <div className="formulario">
          <h2>Cadastro de Clientes</h2>
          <input
            type="text"
            name="cnpj"
            placeholder="CNPJ"
            value={formData.cnpj}
            onChange={handleInputChange}
          />
          <input
            type="text"
            name="razao_social"
            placeholder="Razão Social"
            value={formData.razao_social}
            onChange={handleInputChange}
          />
          <input
            type="text"
            name="nome_fantasia"
            placeholder="Nome Fantasia"
            value={formData.nome_fantasia}
            onChange={handleInputChange}
          />
          <input
            type="text"
            name="telefone"
            placeholder="Telefone"
            value={formData.telefone}
            onChange={handleInputChange}
          />
          <input
            type="email"
            name="email"
            placeholder="E-mail"
            value={formData.email}
            onChange={handleInputChange}
          />
          <button onClick={cadastrarCliente}>Cadastrar Cliente</button>
        </div>
      );
    }
    return <p>Selecione uma opção para cadastro.</p>;
  };

  const renderTabela = () => {
    if (tipoCadastro === "clientes") {
      const clientesFiltrados = clientes.filter((cliente) =>
        cliente.razao_social.toLowerCase().includes(pesquisa.toLowerCase())
      );
      return (
        <div className="tabela-container">
          <h2>Clientes Cadastrados</h2>
          <div className="pesquisa-container">
            <input
              type="text"
              placeholder="Pesquisar clientes..."
              value={pesquisa}
              onChange={(e) => setPesquisa(e.target.value)}
            />
            <button>🔍</button>
          </div>
          <table className="tabela-cadastrados">
            <thead>
              <tr>
                <th>Nome</th>
                <th>CNPJ</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {clientesFiltrados.map((cliente) => (
                <tr key={cliente.cnpj}>
                  <td>{cliente.razao_social}</td>
                  <td>{cliente.cnpj}</td>
                  <td>
                    <button>Detalhes</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    }
    return <p>Selecione uma opção para visualizar os cadastrados.</p>;
  };

  return (
    <div className="cadastros-container">
      <Sidebar />
      <div className="cadastros-content">
        <header className="cadastros-header">
          <h1>Cadastros</h1>
          <div className="selecao-tipo">
            <button
              className={tipoCadastro === "clientes" ? "ativo" : ""}
              onClick={() => setTipoCadastro("clientes")}
            >
              Clientes
            </button>
            <button
              className={tipoCadastro === "motoristas" ? "ativo" : ""}
              onClick={() => setTipoCadastro("motoristas")}
            >
              Motoristas
            </button>
            <button
              className={tipoCadastro === "veiculos" ? "ativo" : ""}
              onClick={() => setTipoCadastro("veiculos")}
            >
              Veículos
            </button>
          </div>
        </header>

        {mensagem && <p className="mensagem">{mensagem}</p>}

        {renderFormulario()}

        {renderTabela()}
      </div>
    </div>
  );
};

export default Cadastros;