import React from 'react';
import heroHtml from '../html-sections/hero.html?raw';

const Hero = () => {
  return <div dangerouslySetInnerHTML={{ __html: heroHtml }} />;
};

export default Hero;
