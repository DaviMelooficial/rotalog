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
  }

  body {
    background: var(--background);
    color: var(--text);
    min-height: 100vh;
  }
`;