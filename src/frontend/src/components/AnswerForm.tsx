import React, { useState } from 'react';

interface AnswerFormProps {
  onSubmit: (answer: string) => void;
  disabled: boolean;
}

const AnswerForm: React.FC<AnswerFormProps> = ({ onSubmit, disabled }) => {
  const [answer, setAnswer] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (answer.trim()) {
      onSubmit(answer.trim());
      setAnswer('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        placeholder="ポケモンの名前を入力"
        disabled={disabled}
      />
      <button type="submit" disabled={disabled}>
        回答する
      </button>
    </form>
  );
};

export default AnswerForm;
