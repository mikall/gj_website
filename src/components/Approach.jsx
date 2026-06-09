import React from 'react';
import approachHtml from '../html-sections/approach.html?raw';

const Approach = () => {
  return <div dangerouslySetInnerHTML={{ __html: approachHtml }} />;
};

export default Approach;
