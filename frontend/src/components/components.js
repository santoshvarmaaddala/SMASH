// frontend/src/components/MyComponent.js
import React, { useEffect, useState } from 'react';
import api from '../api';  // Adjust path as per your project structure

const MyComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    api.get('mymodel/')  // Adjust endpoint as per your Django URLs
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Data from Django Backend</h1>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default MyComponent;
