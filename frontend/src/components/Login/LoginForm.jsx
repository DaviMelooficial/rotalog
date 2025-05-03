import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { Envelope, Lock } from '@phosphor-icons/react';
import authService from '../../services/authService';

const LoginContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  background: linear-gradient(135deg, var(--primary) 0%, var(--background) 100%);
`;

const LoginBox = styled(motion.div)`
  background: var(--surface);
  backdrop-filter: blur(10px);
  padding: 2.5rem;
  border-radius: 20px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
`;

const Logo = styled.div`
  text-align: center;
  margin-bottom: 2rem;

  h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: 1px;
    
    span {
      background: linear-gradient(90deg, var(--secondary) 0%, #00b8d4 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  }
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
`;

const InputGroup = styled.div`
  position: relative;

  svg {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    transition: color 0.3s;
  }

  input:focus + svg {
    color: var(--secondary);
  }
`;

const Input = styled.input`
  width: 100%;
  padding: 1rem 1rem 1rem 3rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  color: var(--text);
  font-size: 1rem;
  transition: all 0.3s;

  &:focus {
    outline: none;
    border-color: var(--secondary);
    background: rgba(255, 255, 255, 0.1);
  }

  &::placeholder {
    color: var(--text-secondary);
  }
`;

const LoginButton = styled(motion.button)`
  width: 100%;
  padding: 1rem;
  border: none;
  border-radius: 12px;
  background: linear-gradient(90deg, var(--secondary) 0%, #00b8d4 100%);
  color: var(--text);
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.3s;

  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
`;

const ForgotPassword = styled.a`
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.875rem;
  text-align: center;
  margin-top: 1rem;
  display: block;
  transition: color 0.3s;

  &:hover {
    color: var(--secondary);
  }
`;

const ErrorMessage = styled.div`
  color: #ff4757;
  background: rgba(255, 71, 87, 0.1);
  padding: 0.75rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  text-align: center;
  font-size: 0.875rem;
`;

export function LoginForm() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const response = await authService.login(formData.username, formData.password);
      if (response.access_token) {
        console.log('Login realizado com sucesso!');
        window.location.href = '/dashboard';
      }
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleForgotPassword = (e) => {
    e.preventDefault();
    navigate('/recuperar-senha');
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    setError('');
  };

  return (
    <LoginContainer>
      <LoginBox
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Logo>
          <h1>Rota<span>log</span></h1>
        </Logo>
        
        {error && <ErrorMessage>{error}</ErrorMessage>}

        <Form onSubmit={handleSubmit}>
          <InputGroup>
            <Input
              type="text"
              name="username"
              placeholder="Usuário"
              value={formData.username}
              onChange={handleChange}
              required
            />
            <Envelope size={20} />
          </InputGroup>

          <InputGroup>
            <Input
              type="password"
              name="password"
              placeholder="Senha"
              value={formData.password}
              onChange={handleChange}
              required
            />
            <Lock size={20} />
          </InputGroup>

          <LoginButton
            type="submit"
            disabled={loading}
            whileTap={{ scale: 0.98 }}
          >
            {loading ? 'Entrando...' : 'Entrar'}
          </LoginButton>
        </Form>

        <ForgotPassword onClick={handleForgotPassword}>
          Esqueceu sua senha?
        </ForgotPassword>
      </LoginBox>
    </LoginContainer>
  );
}