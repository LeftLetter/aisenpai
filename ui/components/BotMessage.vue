<template>
  <div class="d-flex justify-start">
    <div class="bot-icon-div">
      <v-img
        :src="require('~/assets/_c_choju32_0023_s512_choju32_0023_11.png')"
        height="50px"
        width="50px"
        aspect-ratio="1"
        class="bot-icon"
      ></v-img>
    </div>
    <v-card class="msgbox bot-msg ml-5 mb-4 pa-2"
      ><template v-if="message.words && message.words.length > 0">
        こんな単語で検索してみたらどうかな？<br />
        <span
          v-for="(similarWord, index) in message.words[0].similarWords"
          :key="index"
        >
          <v-chip label class="mr-2">
            {{ similarWord.word }}
          </v-chip></span
        ></template
      ><template v-else>{{ message.message }}</template></v-card
    >
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.bot-icon-div {
  border-radius: 50%;
  height: 50px;
  width: 50px;
  margin-left: 5pt;
}
.bot-icon {
  border-radius: 50%;
}
.msgbox {
  min-height: 50px;
  width: 80%;
  border-radius: 8px !important;
  position: relative;
}
.bot-msg:before {
  position: absolute;
  content: '';
  top: 10px;
  right: 100%;
  border: 5px solid transparent;
  border-right: 15px solid white;
}
</style>
