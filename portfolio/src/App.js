import { BrowserRouter, Routes, Route } from "react-router-dom";
import AboutPage from "./pages/AboutPage";
import DetailPage from "./pages/DetailPage";
import "./styles/main.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AboutPage />} />
        <Route path="/projects/:id" element={<DetailPage type="projects" />} />
        <Route path="/blogs/:id" element={<DetailPage type="blogs" />} />
        <Route path="/news/:id" element={<DetailPage type="news" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
