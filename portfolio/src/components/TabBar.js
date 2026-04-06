function TabBar({ activeTab, onTabChange }) {
  const tabs = ["projects", "blogs", "news"];

  return (
    <nav data-testid="tab-bar" className="tab-bar">
      {tabs.map((tab) => (
        <button
          key={tab}
          data-testid={`tab-${tab}`}
          className={`tab-button ${activeTab === tab ? "active" : ""}`}
          onClick={() => onTabChange(tab)}
        >
          {tab.charAt(0).toUpperCase() + tab.slice(1)}
        </button>
      ))}
    </nav>
  );
}

export default TabBar;
