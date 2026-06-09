import React from 'react';
import whatDoesHtml from '../html-sections/what-does.html?raw';

const WhatDoes = () => {
  return <div dangerouslySetInnerHTML={{ __html: whatDoesHtml }} />;
};

export default WhatDoes;
