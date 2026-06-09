import React, { useState, useEffect } from 'react';
import headerHtml from '../html-sections/header.html?raw';

const Header = () => {
  return <div dangerouslySetInnerHTML={{ __html: headerHtml }} />;
};

export default Header;
