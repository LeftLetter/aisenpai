const socketio = require('socket.io')
const io = socketio()
const axios = require('axios')
const Logger = require('../common/logger')
// const MessageController = require('../controllers/messageController')

const socketApi = {}
socketApi.io = io

io.of('/socket.io').on('connection', socket => {
  Logger.getLogger().info('connected')

  // 新規接続時にウェルカムメッセージを送信
  socket.on('welcome', msg => {
    socket.emit('message', global.WELCOME_MESSAGE)
    Logger.getLogger().info(msg)
  })

  // メッセージ受信
  socket.on('message', async msg => {
    try {
      // 時間がかかった時用のクッションメッセージ
      socket.emit('message', global.WAIT_MESSAGE)

      // // 検索クエリを投げかけて関連記事を得る
      // const title = await axios.get(
      //   `http://api-server:${process.env.APISERVER_PORT}/sentence`,
      //   { params: { sentence: msg } }
      // )
      // console.log(title.data.title)

      // // 記事本文を得る
      // const body = await axios.get(
      //   `http://api-server:${process.env.APISERVER_PORT}/qiita`,
      //   { params: { sentence: title.data.title } }
      // )
      // console.log(body.data.body)

      // // 記事要約
      // const summary = axios.get(
      //   `http://api-server:${process.env.APISERVER_PORT}/summary`,
      //   { params: { sentence: body.data.body } }
      // )
      // console.log(summary)

      // 関連単語取得
      const words = axios.get(
        `http://api-server:${process.env.APISERVER_PORT}/api/v1/synonym`,
        // { params: { sentence: msg, useDictionary: true } }
        { params: { sentence: msg } }
      )
      console.log(words)

      const p = await Promise.all([words])
      // const p = await Promise.all([summary, words])

      const result = {
        // summary: p[0].data.body,
        words: p[0].data.words,
        title: 'mock title',
        url: '',
      }

      socket.emit('message', result)
    } catch (error) {
      Logger.getLogger().error(JSON.stringify(error, null, 2))
      // エラー時のメッセージ
      socket.emit('message', global.FAIL_MESSAGE)
    }

    Logger.getLogger().info(msg)
  })
})

module.exports = socketApi
