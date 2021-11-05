import mongoose from 'mongoose'

const enclosureSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    }
});

export default mongoose.model('Enclosure', enclosureSchema);