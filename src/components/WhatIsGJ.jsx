import React from 'react';
import whatIsHtml from '../html-sections/what-is-gj.html?raw';

const WhatIsGJ = () => {
  return <div dangerouslySetInnerHTML={{ __html: whatIsHtml }} />;
};

export default WhatIsGJ;
