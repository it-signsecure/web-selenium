import ThumbnailCard from "./ThumbnailCard";

function ThumbnailGrid({ items, type }) {
  return (
    <div data-testid="thumbnail-grid" className="grid">
      {items.map((item) => (
        <ThumbnailCard key={item.id} item={item} type={type} />
      ))}
    </div>
  );
}

export default ThumbnailGrid;
