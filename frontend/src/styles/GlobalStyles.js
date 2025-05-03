import { createGlobalStyle } from 'styled-components';

export const GlobalStyles = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
  }

  :root {
    --primary: #1a1c46;
    --secondary: #00f2ff;
    --success: #00b371;
    --warning: #ff8a00;
    --error: #ff4757;
    --background: #13141f;
    --surface: rgba(255, 255, 255, 0.1);
    --text: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --sidebar-width: 220px;
    --sidebar-width-collapsed: 64px;
    --sidebar-blur: blur(6px);
    --sidebar-shadow: 2px 0 12px rgba(0,0,0,0.12);
    --sidebar-gradient: linear-gradient(135deg, var(--primary) 70%, var(--secondary) 100%);
    --sidebar-active-underline: linear-gradient(90deg, var(--secondary), var(--warning));
  }

  body {
    background: var(--background);
    color: var(--text);
    min-height: 100vh;
    transition: background 0.2s;
  }

  #root {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  ::selection {
    background: var(--secondary);
    color: var(--primary);
  }

  /* Scrollbar estilizada */
  ::-webkit-scrollbar {
    width: 8px;
    background: var(--surface);
  }
  ::-webkit-scrollbar-thumb {
    background: var(--secondary);
    border-radius: 4px;
  }
`;