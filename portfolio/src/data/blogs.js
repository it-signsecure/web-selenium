const blogs = [
  {
    id: "blog-1",
    title: "Getting Started with Selenium",
    thumbnail: "https://placehold.co/300x200?text=Selenium+Guide",
    summary: "A beginner's guide to writing your first Selenium test in Python.",
    description:
      "In this post I walk through setting up Selenium with Python, installing ChromeDriver via webdriver-manager, and writing your first test that opens a browser, navigates to a URL, and asserts that a page title is correct. We also cover WebDriverWait vs time.sleep and why you should always use the former."
  },
  {
    id: "blog-2",
    title: "CI/CD with GitHub Actions",
    thumbnail: "https://placehold.co/300x200?text=GitHub+Actions",
    summary: "How to set up a CI/CD pipeline for a React app from scratch.",
    description:
      "This post explains how to write a GitHub Actions workflow that lints, builds, and tests a React application on every push. A second workflow deploys the built site to AWS S3 only when changes land on the main branch. Includes tips on caching node_modules and handling secrets securely."
  },
  {
    id: "blog-3",
    title: "React Router v6 in 10 Minutes",
    thumbnail: "https://placehold.co/300x200?text=React+Router",
    summary: "The quickest way to add client-side routing to your React app.",
    description:
      "React Router v6 introduced a simpler, nested route model. This post covers BrowserRouter, Routes, Route, Link, useNavigate, and useParams with minimal working examples. By the end you'll be able to add multi-page navigation to any React app in under 10 minutes."
  }
];

export default blogs;
