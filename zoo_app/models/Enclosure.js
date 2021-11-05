import mongoose from 'mongoose'

const enclosureSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    animals: [{
        ref: 'Animal',
        type: mongoose.Types.ObjectId
    }]
});

export default mongoose.model('Enclosure', enclosureSchema);