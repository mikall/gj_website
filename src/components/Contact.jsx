import React from 'react';
import contactHtml from '../html-sections/contact.html?raw';

const Contact = () => {
  return <div dangerouslySetInnerHTML={{ __html: contactHtml }} />;
};

export default Contact;
