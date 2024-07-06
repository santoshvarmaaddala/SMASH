// frontend/src/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',  // Adjust URL as per your Django backend
  timeout: 10000,
});

export default api;
