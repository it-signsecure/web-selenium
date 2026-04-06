import { useNavigate } from "react-router-dom";

function ThumbnailCard({ item, type }) {
  const navigate = useNavigate();

  return (
    <div
      data-testid={`card-${item.id}`}
      className="card"
      onClick={() => navigate(`/${type}/${item.id}`)}
    >
      <img src={item.thumbnail} alt={item.title} />
      <h3>{item.title}</h3>
      <p>{item.summary}</p>
    </div>
  );
}

export default ThumbnailCard;
