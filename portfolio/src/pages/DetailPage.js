import { useParams, useNavigate } from "react-router-dom";
import projects from "../data/projects";
import blogs from "../data/blogs";
import news from "../data/news";

const allData = { projects, blogs, news };

function DetailPage({ type }) {
  const { id } = useParams();
  const navigate = useNavigate();
  const item = allData[type].find((i) => i.id === id);

  if (!item) {
    return <p>Item not found.</p>;
  }

  return (
    <div data-testid="detail-page" className="detail-page">
      <button
        data-testid="back-button"
        className="back-button"
        onClick={() => navigate(-1)}
      >
        Back
      </button>
      <h1 data-testid="detail-title">{item.title}</h1>
      <p data-testid="detail-description">{item.description}</p>
    </div>
  );
}

export default DetailPage;
