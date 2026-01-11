import axios from 'axios';

const api = axios.create({
    baseURL: '/api', // Proxied by Vite or Nginx in prod
    headers: {
        'Content-Type': 'application/json',
    },
});

export const loginWithGoogle = () => {
    // Redirects to backend auth endpoint
    window.location.href = '/api/auth/login';
};

export default api;
