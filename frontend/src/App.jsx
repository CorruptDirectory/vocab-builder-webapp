import { useState, useEffect } from "react";

import WordCardSection from "./components/WordCardSection";

import "./app.css";

function App() {
  const [words, setWords] = useState([]);
  const [selectableLanguages, setSelectableLanguages] = useState([]);
  const [selectedLanguage, setSelectedLanguage] = useState("");

  async function fetchWords() {
    try {
      const response = await fetch(
        `${
          import.meta.env.VITE_API_URL
        }words/languange?code=${selectedLanguage}`
      );
      if (!response.ok) {
        throw new Error("Network response not ok");
      }
      const result = await response.json();
      setWords(result);
    } catch (error) {
      console.log("Error fetching data:", error);
    }
  }

  // Get list of languages awailable for learning.
  async function fetchLanguages() {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}language`);
      if (!response.ok) {
        throw new Error("Network response not ok");
      }
      const result = await response.json();
      setSelectableLanguages(result);
    } catch (error) {
      console.log("Error fetching languages: ", error);
    }
  }

  // Runs only on initial render
  useEffect(() => {
    fetchLanguages();
  }, []);

  // Runs every time selectedLanguage is changed
  useEffect(() => {
    fetchWords();
  }, [selectedLanguage]);

  return (
    <div className="container">
      <form className="">
        <label>Please select language:</label>
        <select
          value={selectedLanguage}
          onChange={(e) => setSelectedLanguage(e.target.value)}
        >
          {selectableLanguages.map((language) => (
            <option key={language.code} value={language.code}>
              {language.name}
            </option>
          ))}
        </select>
      </form>
      <WordCardSection words={words} />
    </div>
  );
}

export default App;
