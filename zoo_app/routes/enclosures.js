import express from 'express'
let router = express.Router();

import EnclosureModel from '../models/Enclosure.js';

router.post('/', async (req, res) => {
    try {
        let { name, animals } = req.body;

        const enclosure = new EnclosureModel({ 
            name: name,
            animals: animals
        });
        await enclosure.save();

        return res.status(200).json(enclosure);
    } catch (error) {
        return res.status(500).json({msg: error.message});
    }
});

router.get('/', async (req, res) => {
    try {
        let enclosures = await EnclosureModel.find();
        res.status(200).json(enclosures);
    } catch (error) {
        return res.status(500).json({msg: error.message});
    }
});

router.get('/animals/:animalId', async (req, res) => {
    try {
        let { animalId } = req.params;

        const animal = await AnimalModel.findOne({_id: animalId});
        
        if (animal === null) {
            return res.status(500).json({msg: "Animal not found !"});
        }
        
        return res.status(200).json(animal);
    } catch (error) {
        return res.status(500).json({msg: error.message});
    }
});

router.delete('/animals/:animalId', async (req, res) => {
    try {
        let { animalId } = req.params;

        await AnimalModel.findOneByIdAndDelete(animalId);
        res.status(200).json({msg: "Animal well deleted !"});
    } catch (error) {
        return res.status(500).json({msg: error.message});
    }
});

router.put('/animals/:animalId', async (req, res) => {
    try {
        const { animalId } = req.params;
        let animal = req.body;

        animal = await AnimalModel.findOneAndUpdate({ _id: animalId}, animal, {new: true});
        // animal = await AnimalModel.findOne({_id: animalId});

        res.status(200).json(animal);
    } catch (error) {
        return res.status(500).json({msg: error.message});
    }
});

export default router;