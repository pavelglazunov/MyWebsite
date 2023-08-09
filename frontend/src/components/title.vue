<template>
  <div class="title_block">
    <p>{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: "TitleText",
  props: {
    text: String
  }
}
</script>

<style scoped>
.title_block {
  border-bottom: 1px #C32A7C solid;
  width: 60%;

}
p {

  margin: 0;
  color: #FFF;
  font-family: 'Source Code Pro', monospace;

  font-size: 5vh;
  /*max-width: 20vw;*/
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}
</style>