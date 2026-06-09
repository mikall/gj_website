import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import WhatIsGJ from './components/WhatIsGJ';
import WhatDoes from './components/WhatDoes';
import Approach from './components/Approach';
import Contact from './components/Contact';
import Footer from './components/Footer';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Hero />
        <WhatIsGJ />
        <WhatDoes />
        <Approach />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}

export default App;
