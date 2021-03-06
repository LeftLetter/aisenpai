const express = require('express')
const router = express.Router()
const loginModel = require('../models/login_model')

router.post('/login', (req, res, next) => loginModel.login(req, res, next))

module.exports = router
