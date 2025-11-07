import React, { useEffect, useState } from 'react';
import '../styles/Timer.css';

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

  const percentage = (time / initialTime) * 100;
  const circumference = 2 * Math.PI * 70; // 70 is the radius
  const strokeDashoffset = circumference - (percentage / 100) * circumference;

  const getTimerColor = () => {
    if (percentage > 50) return '#10b981'; // green
    if (percentage > 25) return '#f59e0b'; // orange
    return '#ef4444'; // red
  };

  return (
    <div className="timer-container">
      <svg className="timer-svg" width="180" height="180">
        <circle
          className="timer-circle-bg"
          cx="90"
          cy="90"
          r="70"
        />
        <circle
          className="timer-circle-progress"
          cx="90"
          cy="90"
          r="70"
          style={{
            strokeDasharray: circumference,
            strokeDashoffset: strokeDashoffset,
            stroke: getTimerColor()
          }}
        />
      </svg>
      <div className="timer-text">
        <div className="timer-number">{time}</div>
        <div className="timer-label">秒</div>
      </div>
    </div>
  );
};

export default Timer;
