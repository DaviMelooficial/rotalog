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
  const [cnpjConsulta, setCnpjConsulta] = useState("");
  const [clienteConsultado, setClienteConsultado] = useState(null);

  useEffect(() => {
    if (tipoCadastro === "clientes") {
      listarClientes();
    }
  }, [tipoCadastro]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Função para consultar cliente pelo CNPJ
  const consultarCliente = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/clientes/consultar_cliente/${cnpjConsulta}`);
      setClienteConsultado(response.data); // Armazena os dados do cliente consultado
      setMensagem(""); // Limpa mensagens de erro
    } catch (error) {
      setClienteConsultado(null); // Limpa os dados do cliente consultado
      setMensagem(error.response?.data?.erro || "Erro ao consultar cliente.");
    }
  };
  
  const cadastrarCliente = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/clientes/cadastrar_cliente",
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
      const response = await axios.get("http://localhost:5000/clientes/listar_clientes"); // Endpoint fictício
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

          {/* Informações Básicas */}
          <fieldset className="form-section">
            <legend>Informações Básicas</legend>
            <div className="formulario-grid">
              <input
                type="text"
                name="cnpj"
                placeholder="CNPJ *"
                value={formData.cnpj}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="razao_social"
                placeholder="Razão Social *"
                value={formData.razao_social}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="nome_fantasia"
                placeholder="Nome Fantasia"
                value={formData.nome_fantasia}
                onChange={handleInputChange}
              />
            </div>
          </fieldset>

          {/* Contato */}
          <fieldset className="form-section">
            <legend>Contato</legend>
            <div className="formulario-grid">
              <input
                type="email"
                name="email"
                placeholder="E-mail *"
                value={formData.email}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="telefone"
                placeholder="Telefone"
                value={formData.telefone}
                onChange={handleInputChange}
              />
            </div>
          </fieldset>

          {/* Endereço */}
          <fieldset className="form-section">
            <legend>Endereço</legend>
            <div className="formulario-grid">
              <input
                type="text"
                name="logradouro"
                placeholder="Logradouro"
                value={formData.logradouro}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="bairro"
                placeholder="Bairro"
                value={formData.bairro}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="cidade"
                placeholder="Cidade"
                value={formData.cidade}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="estado"
                placeholder="Estado"
                value={formData.estado}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="cep"
                placeholder="CEP"
                value={formData.cep}
                onChange={handleInputChange}
              />
            </div>
          </fieldset>

          {/* Informações Fiscais */}
          <fieldset className="form-section">
            <legend>Informações Fiscais</legend>
            <div className="formulario-grid">
              <input
                type="text"
                name="inscricao_estadual"
                placeholder="Inscrição Estadual"
                value={formData.inscricao_estadual}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="inscricao_municipal"
                placeholder="Inscrição Municipal"
                value={formData.inscricao_municipal}
                onChange={handleInputChange}
              />
            </div>
          </fieldset>

          {/* Observações */}
          <fieldset className="form-section">
            <legend>Observações</legend>
            <textarea
              name="observacoes"
              placeholder="Observações adicionais sobre o cliente"
              value={formData.observacoes}
              onChange={handleInputChange}
            />
          </fieldset>

          {/* Botões */}
          <div className="form-buttons">
            <button onClick={cadastrarCliente}>Cadastrar Cliente</button>
          </div>
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
            <button onClick={() => listarClientes()}>🔍</button> {/* Botão de consulta */}
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