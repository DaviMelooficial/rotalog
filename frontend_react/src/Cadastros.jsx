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
  const [motoristas, setMotoristas] = useState([]);
  const [cnpjConsulta, setCnpjConsulta] = useState("");
  const [clienteConsultado, setClienteConsultado] = useState(null);
  const [veiculos, setVeiculos] = useState([]);
  useEffect(() => {
    if (tipoCadastro === "clientes") {
      listarClientes();
    } else if (tipoCadastro === "motoristas") {
      listarMotoristas();
    } else if (tipoCadastro === "veiculos") {
      listarVeiculos();
    }
  }, [tipoCadastro]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };
  // Função para cadastrar motorista
  const cadastrarMotorista = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/motoristas/cadastrar_motorista",
        formData
      );
      setMensagem(response.data.mensagem);
      setFormData({
        nome_motorista: "",
        cpf: "",
        cnh: "",
        telefone: "",
        classificacao: "",
      });
    } catch (error) {
      setMensagem(error.response?.data?.erro || "Erro ao cadastrar motorista.");
    }
  };
  const listarMotoristas = async () => {
    try {
      // Faz a requisição ao endpoint para listar motoristas
      const response = await axios.get("http://localhost:5000/motoristas/listar_motoristas");
      setMotoristas(response.data); // Atualiza o estado com os motoristas retornados
    } catch (error) {
      setMensagem("Erro ao carregar a lista de motoristas.");
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

  const cadastrarVeiculo = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/veiculos/cadastrar",
        formData
      );
      setMensagem(response.data.mensagem || "Veículo cadastrado com sucesso!");
      setFormData({
        placa: "",
        marca: "",
        modelo: "",
        cor: "",
        ano_fabricacao: "",
        renavam: "",
        chassi: "",
        tipo_carroceria: "",
        capacidade_carga: "",
        status: "",
      });
      listarVeiculos(); // Atualiza a lista após o cadastro
    } catch (error) {
      setMensagem(error.response?.data?.erro || "Erro ao cadastrar veículo.");
    }
  };
  
  const listarVeiculos = async () => {
    try {
      const response = await axios.get("http://localhost:5000/veiculos/listar");
      console.log("Dados retornados do backend:", response.data); // Verifique os dados aqui
      setVeiculos(response.data); // Atualiza o estado com os veículos retornados
    } catch (error) {
      setMensagem("Erro ao carregar a lista de veículos.");
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
    else if (tipoCadastro === "motoristas") {
      return (
        <div className="formulario">
          <h2>Cadastro de Motoristas</h2>
  
          {/* Informações Básicas */}
          <fieldset className="form-section">
            <legend>Informações Básicas</legend>
            <div className="formulario-grid">
              <input
                type="text"
                name="nome_motorista"
                placeholder="Nome do Motorista *"
                value={formData.nome_motorista || ""}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="cpf"
                placeholder="CPF *"
                value={formData.cpf || ""}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="cnh"
                placeholder="CNH *"
                value={formData.cnh || ""}
                onChange={handleInputChange}
                required
              />
            </div>
          </fieldset>
  
          {/* Contato */}
          <fieldset className="form-section">
            <legend>Contato</legend>
            <div className="formulario-grid">
              <input
                type="text"
                name="telefone"
                placeholder="Telefone"
                value={formData.telefone || ""}
                onChange={handleInputChange}
              />
            </div>
          </fieldset>
  
          {/* Classificação */}
          <fieldset className="form-section">
            <legend>Classificação</legend>
            <div className="formulario-grid">
              <input
                type="text"
                name="classificacao"
                placeholder="Classificação"
                value={formData.classificacao || ""}
                onChange={handleInputChange}
              />
            </div>
          </fieldset>
  
          {/* Botões */}
          <div className="form-buttons">
            <button onClick={cadastrarMotorista}>Cadastrar Motorista</button>
          </div>
        </div>
      );
    }
    else if (tipoCadastro === "veiculos") {
      return (
        <div className="formulario">
          <h2>Cadastro de Veículos</h2>
    
          {/* Informações do Veículo */}
          <fieldset className="form-section">
            <legend>Informações do Veículo</legend>
            <div className="formulario-grid">
              <input
                type="text"
                name="placa"
                placeholder="Placa *"
                value={formData.placa || ""}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="marca"
                placeholder="Marca *"
                value={formData.marca || ""}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="modelo"
                placeholder="Modelo *"
                value={formData.modelo || ""}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                name="cor"
                placeholder="Cor"
                value={formData.cor || ""}
                onChange={handleInputChange}
              />
              <input
                type="number"
                name="ano_fabricacao"
                placeholder="Ano de Fabricação"
                value={formData.ano_fabricacao || ""}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="renavam"
                placeholder="Renavam"
                value={formData.renavam || ""}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="chassi"
                placeholder="Chassi"
                value={formData.chassi || ""}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="tipo_carroceria"
                placeholder="Tipo de Carroceria"
                value={formData.tipo_carroceria || ""}
                onChange={handleInputChange}
              />
              <input
                type="number"
                name="capacidade_carga"
                placeholder="Capacidade de Carga (kg)"
                value={formData.capacidade_carga || ""}
                onChange={handleInputChange}
              />
              <input
                type="text"
                name="status"
                placeholder="Status"
                value={formData.status || ""}
                onChange={handleInputChange}
              />
            </div>
          </fieldset>
    
          {/* Botões */}
          <div className="form-buttons">
            <button onClick={cadastrarVeiculo}>Cadastrar Veículo</button>
          </div>
        </div>
      );
    }
    return <p>Selecione uma opção para cadastro.</p>;
  };

  const renderTabela = () => {
    if (tipoCadastro === "clientes") {
      const clientesFiltrados = clientes.filter((cliente) =>
        cliente.razao_social?.toLowerCase().includes(pesquisa.toLowerCase())
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
    else if (tipoCadastro === "motoristas") {
      const motoristasFiltrados = motoristas.filter((motorista) =>
        motorista.nome_motorista?.toLowerCase().includes(pesquisa.toLowerCase())
      );
      return (
        <div className="tabela-container">
          <h2>Motoristas Cadastrados</h2>
          <div className="pesquisa-container">
            <input
              type="text"
              placeholder="Pesquisar motoristas..."
              value={pesquisa}
              onChange={(e) => setPesquisa(e.target.value)}
            />
            <button onClick={() => listarMotoristas()}>🔍</button>
          </div>
          <table className="tabela-cadastrados">
            <thead>
              <tr>
                <th>Nome</th>
                <th>CPF</th>
                <th>CNH</th>
                <th>Classificação</th>
                <th>Telefone</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {motoristasFiltrados.map((motorista) => (
                <tr key={motorista.id_motorista}>
                  <td>{motorista.nome_motorista}</td>
                  <td>{motorista.cpf}</td>
                  <td>{motorista.cnh}</td>
                  <td>{motorista.classificacao}</td>
                  <td>{motorista.telefone}</td>
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
    else if (tipoCadastro === "veiculos") {
      const veiculosFiltrados = veiculos.filter((veiculo) =>
        veiculo.PLACA?.toLowerCase().includes(pesquisa.toLowerCase())
      );
      console.log("Veículos filtrados:", veiculosFiltrados); // Verifique os dados filtrados
      return (
        <div className="tabela-container">
          <h2>Veículos Cadastrados</h2>
          <div className="pesquisa-container">
            <input
              type="text"
              placeholder="Pesquisar veículos..."
              value={pesquisa}
              onChange={(e) => setPesquisa(e.target.value)}
            />
            <button onClick={() => listarVeiculos()}>🔍</button>
          </div>
          <table className="tabela-cadastrados">
            <thead>
              <tr>
                <th>Placa</th>
                <th>Marca</th>
                <th>Modelo</th>
                <th>Cor</th>
                <th>Ano</th>
                <th>Capacidade</th>
                <th>Status</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {veiculosFiltrados.map((veiculo) => (
                <tr key={veiculo.ID_VEICULO}>
                  <td>{veiculo.PLACA}</td>
                  <td>{veiculo.MARCA}</td>
                  <td>{veiculo.MODELO}</td>
                  <td>{veiculo.COR}</td>
                  <td>{veiculo.ANO_FABRICACAO}</td>
                  <td>{veiculo.CAPACIDADE_CARGA} kg</td>
                  <td>{veiculo.STATUS}</td>
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