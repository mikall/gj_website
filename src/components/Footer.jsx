import React from 'react';
import footerHtml from '../html-sections/footer.html?raw';

const Footer = () => {
  return <div dangerouslySetInnerHTML={{ __html: footerHtml }} />;
};

export default Footer;
