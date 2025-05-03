import { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { Envelope, ArrowLeft } from '@phosphor-icons/react';
import authService from '../../services/authService';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  background: linear-gradient(135deg, var(--primary) 0%, var(--background) 100%);
`;

const Card = styled(motion.div)`
  background: rgba(255, 255, 255, 0.1);
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

const SubmitButton = styled(motion.button)`
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

const InfoText = styled.p`
  color: var(--text-secondary);
  text-align: center;
  font-size: 0.875rem;
  margin: 1.5rem 0;
  line-height: 1.5;
`;

const BackToLogin = styled.a`
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.875rem;
  margin-top: 1rem;
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

export function ForgotPassword() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [email, setEmail] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await authService.resetPassword(email);
      setSuccess(true);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Card
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Logo>
          <h1>Rota<span>log</span></h1>
        </Logo>

        {error && <ErrorMessage>{error}</ErrorMessage>}

        {success ? (
          <>
            <InfoText>
              Se o e-mail estiver cadastrado em nossa base, você receberá um link para redefinir sua senha.
            </InfoText>
            <BackToLogin href="/login">
              <ArrowLeft size={20} />
              Voltar para o login
            </BackToLogin>
          </>
        ) : (
          <>
            <InfoText>
              Digite seu e-mail cadastrado para receber as instruções de recuperação de senha.
            </InfoText>

            <Form onSubmit={handleSubmit}>
              <InputGroup>
                <Input
                  type="email"
                  placeholder="Digite seu e-mail"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
                <Envelope size={20} />
              </InputGroup>

              <SubmitButton
                type="submit"
                disabled={loading}
                whileTap={{ scale: 0.98 }}
              >
                {loading ? 'Enviando...' : 'Enviar link de recuperação'}
              </SubmitButton>
            </Form>

            <BackToLogin href="/login">
              <ArrowLeft size={20} />
              Voltar para o login
            </BackToLogin>
          </>
        )}
      </Card>
    </Container>
  );
}