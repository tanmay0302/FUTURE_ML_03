import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMsg]);

    try {
      const res = await axios.post('http://localhost:5001/predict', { message: input });
      const botMsg = {
        sender: 'bot',
        text: `Ticket Type: ${res.data.predicted_ticket_type}\n${res.data.response}`
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (err) {
      setMessages(prev => [...prev, { sender: 'bot', text: 'Something went wrong.' }]);
    }

    setInput('');
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4 flex flex-col items-center">
      <div className="w-full max-w-md bg-white rounded shadow p-4 flex flex-col">
        <h1 className="text-xl font-bold mb-4">Support Chatbot</h1>
        <div className="flex-1 max-h-96 overflow-y-auto mb-4">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`p-2 my-1 rounded ${msg.sender === 'user' ? 'bg-blue-100 text-right' : 'bg-gray-200 text-left'}`}
            >
              {msg.text}
            </div>
          ))}
        </div>
        <div className="flex space-x-2">
          <input
            className="flex-1 border p-2 rounded"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && sendMessage()}
          />
          <button onClick={sendMessage} className="bg-blue-500 text-white px-4 rounded">Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
