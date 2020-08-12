const log4js = require('log4js')

class Logger {
  constructor() {
    log4js.configure(global.LOG4JS_CONFIG_FILE)
    this.logger = log4js.getLogger('app')
  }

  getLogger() {
    return this.logger
  }
}

module.exports = new Logger()
