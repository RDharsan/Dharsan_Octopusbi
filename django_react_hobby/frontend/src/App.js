import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navigation from "./components/Navigation";
import {BrowserRouter} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
     < Navigation />
    </BrowserRouter>
   
  );
}

export default App;
