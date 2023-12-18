import WordCard from "./WordCard";
import Sentences from "./Sentences";
import "./wordCardSection.css";

function WordcardSection({ words }) {
  return (
    <section className="cards">
      {words.map((word) => (
        <div className="word-row">
          <WordCard
            key={word.word.pk}
            defaultLangWord={word.word.eng_word}
            targetLangWord={word.translated_text}
            img={word.word.image}
          />
          <Sentences key={word.word.pk} sentences={word.sentences} />
        </div>
      ))}
    </section>
  );
}

export default WordcardSection;
