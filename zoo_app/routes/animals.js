import express from 'express'
let router = express.Router();

import AnimalModel from '../models/Animals.js'

router.post('/animals', async (req, res) => {
    try {
        let { name } = req.body;

        const animal = new AnimalModel({ 
            name: name
        });
        await animal.save();

        return res.status(200).json(animal);
    } catch (error) {
        return res.status(500).json({msg: error.message});
    }
});

router.get('/animals', async (req, res) => {
    try {
        const animals = await AnimalModel.find();
        return res.status(200).json(animals);
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