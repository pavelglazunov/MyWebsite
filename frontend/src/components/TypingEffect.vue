<template>
  <h1 class="main_text">{{ main_text }}</h1>
  <p class="main_small_text"> {{ small_text }}</p>
</template>

<script>
export default {
  data() {
    return {
      main_text: '',
      small_text: '',
      main_message: "Pavel Glazunov",
      small_message: "My website",
      typingDelay: 100,
      currentIndex_1: 0,
      currentIndex_2: 0
    };
  },
  mounted() {
    this.typingEffect();
  },
  methods: {
    typingEffect() {
      console.log(555)
      if (this.currentIndex_1 < this.main_message.length) {
        this.main_text += this.main_message.charAt(this.currentIndex_1);
        this.currentIndex_1++;
        setTimeout(this.typingEffect, this.typingDelay);
      }
      else {
        if (this.currentIndex_2 < this.small_message.length) {
          this.small_text += this.small_message.charAt(this.currentIndex_2);
          this.currentIndex_2++;
          setTimeout(this.typingEffect, this.typingDelay);
        }
      }
    }
  }
};
</script>

<style scoped>
.main_text {
  margin: 0;

  font-size: 9vh;

  word-wrap: break-word;

}

.main_small_text {
  margin: 0;

  color: #FFF;
  font-size: 3vh;
}

</style>
