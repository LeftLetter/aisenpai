const express = require('express')
const path = require('path')
const cookieParser = require('cookie-parser')
const logger = require('morgan')
const helmet = require('helmet')

require('./common/common_settings')
require('./common/common_texts')

const Logger = require('./common/logger')
Logger.getLogger().info('Server Start')

const app = express()

const httpRouter = require('./routes/http')

app.use(logger('dev'))
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
app.use(cookieParser())
app.use(express.static(path.join(__dirname, 'public')))
app.use(helmet())

// app.use('/', indexRouter)
app.use('/api', httpRouter)

module.exports = app
