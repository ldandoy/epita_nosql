import mongoose from "mongoose"

export const db = () => {
    mongoose.connect('mongodb://localhost:27017/epita')
    .then(() => {
        console.log('Connected...');
    })
    .catch(err => console.log(err));
}