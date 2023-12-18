import { useState } from "react";
import "./wordCard.css";

function WordCard({ defaultLangWord, targetLangWord, img }) {
  const [cardIsTurned, setCardIsTurned] = useState(false);

  return (
    <div className="card" onClick={() => setCardIsTurned(!cardIsTurned)}>
      <img src={import.meta.env.VITE_MEDIA_URL + img} />
      {!cardIsTurned && <p className="word">{defaultLangWord}</p>}
      {cardIsTurned && <p className="word">{targetLangWord}</p>}
    </div>
  );
}

export default WordCard;
