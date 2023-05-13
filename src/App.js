import './App.css';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { blueGrey, blue } from '@mui/material/colors';

import Header from './pages/header';
import Body from './pages/body';

let theme = createTheme({
  palette: {
    primary: {light: '#87ADCC', 'main': '#478CC3', 'dark': '#2C3842'},
    secondary: blueGrey,
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Box sx={{ display: 'flex' }}>
        <CssBaseline />
        <Header/>
        <Body/>
      </Box>
    </ThemeProvider>
  );
}

export default App;
