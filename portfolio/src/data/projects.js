const projects = [
  {
    id: "proj-1",
    title: "Weather App",
    thumbnail: "https://placehold.co/300x200?text=Weather+App",
    summary: "A React app that fetches and displays live weather data.",
    description:
      "Built with React and the OpenWeatherMap API. Users can search for any city and see current temperature, humidity, and wind speed. The app uses React hooks for state management and async/await for API calls."
  },
  {
    id: "proj-2",
    title: "Portfolio Website",
    thumbnail: "https://placehold.co/300x200?text=Portfolio",
    summary: "This very website — built with React and deployed on AWS S3.",
    description:
      "A static portfolio site built with Create React App and React Router. CI/CD is handled by GitHub Actions: ESLint + Selenium tests run on every push, and the production build deploys to AWS S3 on merge to main."
  },
  {
    id: "proj-3",
    title: "Chat Bot",
    thumbnail: "https://placehold.co/300x200?text=Chat+Bot",
    summary: "A rule-based chat bot written in Python.",
    description:
      "A Python CLI chatbot that uses pattern matching and a knowledge base of intents to respond to user messages. Built to demonstrate NLP basics and state machines without any ML framework."
  }
];

export default projects;
