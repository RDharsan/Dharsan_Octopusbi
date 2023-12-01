import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navigation from "./components/Navigation";
import {BrowserRouter, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    < Navigation />
    <Routes>
      <Route exact path="/" element={<Home/>}>
      </Route>
    </Routes>
     
    </BrowserRouter>
   
  );
}

export default App;
