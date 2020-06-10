<template>
  <v-app>
    <div class="chatarea">
      <transition-group tag="div" name="list">
        <div v-for="message in chat" :key="message.num">
          <div v-if="message.isUser">
            <UserMessage :message="message"></UserMessage>
          </div>
          <div v-else>
            <BotMessage :message="message"></BotMessage>
          </div>
        </div>
      </transition-group>
    </div>
    <v-footer fixed height="80px">
      <v-text-field
        label="入力してください..."
        required
        v-model="input"
        :disabled="sending"
        @keyup.enter="send"
        @keypress="setCanMessageSubmit"
        ref="msgArea"
      ></v-text-field>
      <v-btn color="primary" class="ml-5" @click="send" :disabled="sending"
        >送信</v-btn
      >
    </v-footer>
  </v-app>
</template>

<script>
import UserMessage from '@/components/UserMessage.vue'
import BotMessage from '@/components/BotMessage.vue'
import io from 'socket.io-client'
// import axios from 'axios'
import { v4 as uuidv4 } from 'uuid'

export default {
  name: 'App',
  components: {
    UserMessage,
    BotMessage,
  },
  created() {
    // ウェルカムメッセージの送信
    this.socket.emit('welcome', { user: uuidv4() })

    // メッセージ受信
    this.socket.on('message', data => {
      this.showBotInput(data)
      console.log(data)
      this.sending = false
    })
  },
  data: () => ({
    chat: [],
    input: '',
    num: 0,
    socket: io('/socket.io'),
    canMessageSubmit: false,
    sending: false,
  }),
  methods: {
    setCanMessageSubmit: function () {
      this.canMessageSubmit = true
    },
    send: async function () {
      if (!this.canMessageSubmit) {
        return
      }
      this.showUserInput()
      // send message to server
      this.socket.emit('message', this.input)
      this.sending = true
      this.input = ''
    },
    showUserInput: function () {
      this.chat.push({
        message: this.input,
        isUser: true,
        num: this.num++,
      })
      this.$nextTick(() => {
        window.scrollTo(0, document.body.clientHeight)
      })
    },
    showBotInput: function (data) {
      this.chat.push({
        message: data.summary || data,
        title: data.title || null,
        words: data.words || null,
        isUser: false,
        num: this.num++,
      })
      this.$nextTick(() => {
        window.scrollTo(0, document.body.clientHeight)
        this.$refs.msgArea.focus()
      })
    },
  },
}
</script>

<style scoped>
.chatarea {
  margin-bottom: 120px;
  margin-top: 20px;
}
.list-enter-active,
.list-leave-active {
  transition: all 0.5s;
}
.list-enter,
.list-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
