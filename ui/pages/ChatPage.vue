<template>
  <div class="bg">
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
        ref="msgArea"
        v-model="input"
        label="質問を入力してみよう"
        required
        :disabled="sending"
        @keyup.enter="send"
        @keypress="setCanMessageSubmit"
      ></v-text-field>
      <v-btn color="primary" class="ml-5" :disabled="sending" @click="send"
        >送信</v-btn
      >
    </v-footer>
  </div>
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
  data: () => ({
    chat: [],
    input: '',
    num: 0,
    socket: null,
    canMessageSubmit: false,
    sending: false,
  }),
  mounted() {
    this.socket = io('/socket.io')

    // ウェルカムメッセージの送信
    this.socket.emit('welcome', { user: uuidv4() })

    // メッセージ受信
    this.socket.on('message', (data) => {
      this.showBotInput(data)
      this.sending = false
    })
  },
  methods: {
    setCanMessageSubmit() {
      this.canMessageSubmit = true
    },
    send() {
      if (!this.canMessageSubmit) {
        return
      }
      this.showUserInput()
      // send message to server
      this.socket.emit('message', this.input)
      this.sending = true
      this.input = ''
    },
    showUserInput() {
      this.chat.push({
        message: this.input,
        isUser: true,
        num: this.num++,
      })
      this.$nextTick(() => {
        window.scrollTo(0, document.body.clientHeight)
      })
    },
    showBotInput(data) {
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
.bg {
  height: 100vh;
  background-color: #f9f9f9;
}

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
