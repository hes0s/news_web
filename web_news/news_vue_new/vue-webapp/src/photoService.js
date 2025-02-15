import axios from 'axios';

API_URL = 'http://localhost:5000/photos';

export const getPhotos = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};

export const addPhoto = async (photo) => {
    const response = await axios.post(API_URL, photo);
    return response.data;
  };