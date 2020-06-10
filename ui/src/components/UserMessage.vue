<template>
  <div class="d-flex justify-end">
    <v-card
      transition="slide-x-transition"
      class="msgbox user-msg mb-4 mr-5 pa-2"
      color="blue lighten-5"
      >{{ message.message }}</v-card
    >
  </div>
</template>

<script>
export default {
  props: ['message'],
}
</script>

<style scoped>
.msgbox {
  min-height: 50px;
  width: 80%;
  border-radius: 8px !important;
  position: relative;
}
.user-msg:before {
  position: absolute;
  content: '';
  top: 10px;
  left: 100%;
  border: 5px solid transparent;
  border-left: 15px solid #e3f2fd;
}
</style>
