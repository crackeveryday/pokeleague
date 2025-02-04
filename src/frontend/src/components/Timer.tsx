import React, { useEffect, useState } from 'react';

interface TimerProps {
  initialTime: number;
  onTimeout: () => void;
  isActive: boolean;
}

const Timer: React.FC<TimerProps> = ({ initialTime, onTimeout, isActive }) => {
  const [time, setTime] = useState(initialTime);

  // isActiveが変更されたときにタイマーをリセット
  useEffect(() => {
    if (isActive) {
      setTime(initialTime);  // タイマーをリセット
    }
  }, [isActive, initialTime]);

  useEffect(() => {
    if (!isActive) return;

    const timer = setInterval(() => {
      setTime(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          onTimeout();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [isActive, onTimeout]);

  return <div className="timer">残り時間: {time}秒</div>;
};

export default Timer;
