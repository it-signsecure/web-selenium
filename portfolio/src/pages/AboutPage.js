import { useState } from "react";
import TabBar from "../components/TabBar";
import ThumbnailGrid from "../components/ThumbnailGrid";
import projects from "../data/projects";
import blogs from "../data/blogs";
import news from "../data/news";

const tabData = {
  projects,
  blogs,
  news
};

function AboutPage() {
  const [activeTab, setActiveTab] = useState("projects");

  return (
    <div className="about-page">
      <section data-testid="about-section" className="about-section">
        <h1>About Me</h1>
        <p>
          Hi! I'm a computer science student passionate about building software,
          automating everything, and shipping products to the cloud. This
          portfolio showcases my projects, technical writing, and achievements.
        </p>
      </section>

      <TabBar activeTab={activeTab} onTabChange={setActiveTab} />
      <ThumbnailGrid items={tabData[activeTab]} type={activeTab} />
    </div>
  );
}

export default AboutPage;
