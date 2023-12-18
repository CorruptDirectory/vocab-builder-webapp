import Sentence from "./Sentence";

function Sentences({ sentences }) {
  return (
    <div>
      {sentences.map((sentence) => (
        <Sentence sentence={sentence} />
      ))}
    </div>
  );
}
export default Sentences;
