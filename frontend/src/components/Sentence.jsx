import { useState } from "react";

import "./sentence.css";

function Sentence({ sentence }) {
  const [showTranslation, setShowTranslation] = useState(false);
  return (
    <p
      className="sentence"
      onClick={() => setShowTranslation(!showTranslation)}
    >
      {showTranslation ? sentence.text : sentence.sentence_eng.text}
    </p>
  );
}

export default Sentence;
