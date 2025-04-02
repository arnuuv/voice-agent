import { useState } from 'react'
import './App.css'
import Vapi from "@vapi-ai/web";

const vapi = new Vapi("9261dd01-2f22-4716-b5e6-4940e540b603");

function App() {
  const [isCallActive, setIsCallActive] = useState(false)

  const startCall = async () => {
    await vapi.start("ba32a3aa-f13b-4914-83b5-0118959c03f3")
    setIsCallActive(true)
  }

  const stopCall = async () => {
    vapi.stop()
    setIsCallActive(false)
  }

  return (
    <div className="container">
      <h1>Vapi Call Demo</h1>
      <div className="button-container">
        <button 
          onClick={startCall} 
          disabled={isCallActive}
          className="call-button"
        >
          Start Call
        </button>
        <button 
          onClick={stopCall} 
          disabled={!isCallActive}
          className="call-button"
        >
          Stop Call
        </button>
      </div>
      <p>{isCallActive ? 'Call in progress...' : 'Call ended'}</p>
    </div>
  )
}

export default App